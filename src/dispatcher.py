from flask import Flask
from flask import render_template
import mock_database
import database
import sys
app = Flask(__name__)

db = None

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

	return render_template('statistics_details.html',args = args)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Using MockDatabase"
		db = mock_database.MockDatabase()
	else:
		print "Database:", sys.argv[1]
		db = database.Database()
		db.read(sys.argv[1])
	app.run(debug=True)
