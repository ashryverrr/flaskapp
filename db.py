from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_PORT"]="81"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="myflaskapp"
app.config["MYSQL_CURSORCLASS"]="Dictcursor"