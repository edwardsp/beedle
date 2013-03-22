from flask import Flask
from flask import render_template
import mock_database as db
app = Flask(__name__)

@app.route("/publication_summary")
def showPublicationSummary():
	args = {}
	tempdb = db.get_publication_summary()
	return render_template('statistics.html',args)
