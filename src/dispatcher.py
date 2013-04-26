from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import request
import mock_database
import database
import os
import sys
app = Flask(__name__)

db = None

@app.route("/favicon.ico")
def favicon():
	return send_from_directory(
		os.path.join(app.root_path, "static"),
		"favicon.ico", mimetype="image/vnd.microsoft.icon")

@app.route("/")
def mainpage():
	return showStatisticsMenu()

@app.route("/visualisation/wordcloud")
def wordcloud():
	args = {}
	args["name"] = request.args.get("name")
	args["width"] = int(request.args.get("width"))
	args["height"] = int(request.args.get("height"))
	args["data"] = db.get_coauthor_details(args["name"])
	return render_template("word_cloud.html", args=args)

@app.route("/visualisation/forcelayout")
def forcelayout():
	args = {}
	args["name"] = request.args.get("name")
	level = int(request.args.get("level"))
	args["width"] = int(request.args.get("width"))
	args["height"] = int(request.args.get("height"))
	data = db.get_forcelayout_data(args["name"], level)
	args["nodes"] = data[0]
	args["links"] = data[1]
	return render_template("force_layout.html", args=args)

@app.route("/visualisation/network")
def forcelayout2():
	args = {}
	args["width"] = int(request.args.get("width"))
	args["height"] = int(request.args.get("height"))
	data = db.get_network_data()
	args["nodes"] = data[0]
	args["links"] = data[1]
	return render_template("network.html", args=args)

def format_data(data):
	fmt = "%.2f"
	result = []
	for item in data:
		if type(item) is list:
			result.append(", ".join([ (fmt % i).rstrip('0').rstrip('.') for i in item ]))
		else:
			result.append((fmt % item).rstrip('0').rstrip('.'))
	return result

@app.route("/averages")
def showAverages():
	args = {}
	args['title'] = "Averaged Data"
	tables = []
	headers = ["Average", "Conference Paper", "Journal", "Book", "Book Chapter", "All Publications"]
	averages = [ database.Stat.MEAN, database.Stat.MEDIAN, database.Stat.MODE ]
	print db.get_average_authors_per_publication(0)[1] 
	tables.append( {
		"id":1,
		"title":"Average Authors per Publication",
		"header":headers,
		"rows":[
			[ database.Stat.STR[i] ]
			+ format_data(db.get_average_authors_per_publication(i)[1])
			for i in averages ] } )
	print tables
	tables.append( {
		"id":2,
		"title":"Average Publications per Author",
		"header":headers,
		"rows":[
			[ database.Stat.STR[i] ]
			+ format_data(db.get_average_publications_per_author(i)[1])
			for i in averages ] } )
	tables.append( {
		"id":3,
		"title":"Average Publications in a Year",
		"header":headers,
		"rows":[
			[ database.Stat.STR[i] ]
			+ format_data(db.get_average_publications_in_a_year(i)[1])
			for i in averages ] } )
	tables.append( {
		"id":4,
		"title":"Average Authors in a Year",
		"header":headers,
		"rows":[
			[ database.Stat.STR[i] ]
			+ format_data(db.get_average_authors_in_a_year(i)[1])
			for i in averages ] } )
	
	args['tables'] = tables
	return render_template("averages.html", args=args)

@app.route("/coauthors")
def showCoAuthors():
	args = {}
	args["title"] = "Co-Authors"
	start_year = db.min_year
	if "start_year" in request.args:
		start_year = int(request.args.get("start_year"))
	end_year = db.max_year
	if "end_year" in request.args:
		end_year = int(request.args.get("end_year"))
	pub_type = 4
	if "pub_type" in request.args:
		pub_type = int(request.args.get("pub_type"))
	args["data"] = db.get_coauthor_data(start_year, end_year, pub_type)
	args["start_year"] = start_year
	args["end_year"] = end_year
	args["pub_type"] = pub_type
	args["min_year"] = db.min_year
	args["max_year"] = db.max_year
	return render_template("coauthors.html", args=args)

@app.route("/statistics")
def showStatisticsMenu():
	return render_template('statistics.html')

@app.route("/statisticsdetails/<status>")
def showPublicationSummary(status):
	args = {}
	if (status == "publication_summary"):
		args["title"] = "Publication Summary"
		args["data"] = db.get_publication_summary()
	
	if (status == "publication_author"):
		args["title"] = "Author Publication"
		args["data"] = db.get_publications_by_author()

	if (status == "publication_year"):
		args["title"] = "Publication by Year"
		args["data"] = db.get_publications_by_year()

	if (status == "author_year"):
		args["title"] = "Author by Year"
		args["data"] = db.get_author_totals_by_year()

	return render_template('statistics_details.html',args=args)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Using MockDatabase"
		db = mock_database.MockDatabase()
	else:
		print "Database:", sys.argv[1]
		db = database.Database()
		if db.read(sys.argv[1]) == False:
			sys.exit(1)
	app.run(debug=True)
	app.run(debug=False)
