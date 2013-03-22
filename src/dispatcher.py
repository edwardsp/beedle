from flask import Flask
from flask import render_template
import mock_database as db
app = Flask(__name__)

@app.route("/statistics")
def showStatisticsMenu():
	return render_template('statistics.html')

@app.route("/statisticsdetails/<status>")
def showPublicationSummary(status):
	args = {}
	tempdb = db.getdb()
	if (status == "publication_summary"):
		args["title"] = "Publication Summary"
		args["data"] = tempdb.get_publication_summary()
	
	if (status == "publication_author"):
		args["title"] = "Author Publication"
		args["data"] = tempdb.get_publications_by_author()

	if (status == "publication_year"):
		args["title"] = "Publication by Year"
		args["data"] = tempdb.get_publications_by_year()

	if (status == "author_year"):
		args["title"] = "Author by Year"
		args["data"] = tempdb.get_author_totals_by_year()

	return render_template('statistics_details.html',args = args)

if __name__ == "__main__":
    app.run(debug=True)
