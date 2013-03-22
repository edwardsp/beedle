from flask import Flask
from flask import render_template
import mock_database as db
app = Flask(__name__)

@app.route("/publication_summary")
def showPublicationSummary():
	args = {}
	tempdb = db.getdb()
	return render_template('statistics.html',args = args)

if __name__ == "__main__":
    app.run(debug=True)
