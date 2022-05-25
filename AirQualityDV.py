from flask import Flask, render_template
from Read_TCEQ_Data import df_reporting

app = Flask(__name__)

aqtodayTable = df_reporting.to_html(index=False, na_rep='*')
table_file = open("./templates/todayTable.html","w")
table_file.write(aqtodayTable)
table_file.close()

@app.route("/")
def welcome():
    return render_template(
        "welcome.html"
    )

@app.route("/aqtoday")
def aqtoday():
    return render_template(
        "aqtoday.html",
        report_table=df_reporting.to_html()
    )

@app.route("/todayTable")
def todaytable():
    return render_template(
        "todayTable.html"
    )
