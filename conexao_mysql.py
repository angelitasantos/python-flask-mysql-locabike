from main import *
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())
mysql_host = os.getenv('MYSQL_HOST')
mysql_user = os.getenv('MYSQL_USER')
mysql_password = os.getenv('MYSQL_PASSWORD')
mysql_database = os.getenv('MYSQL_DB')


app.config['MYSQL_HOST'] = mysql_host
app.config['MYSQL_USER'] = mysql_user
app.config['MYSQL_PASSWORD'] = mysql_password
app.config['MYSQL_DB'] = mysql_database
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
bcrypt = Bcrypt(app)
