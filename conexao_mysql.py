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


app.config['MYSQL_HOST'] = 'us-cdbr-east-05.cleardb.net'
app.config['MYSQL_USER'] = 'be0928c1b1043c'
app.config['MYSQL_PASSWORD'] = '03ad0ed9'
app.config['MYSQL_DB'] = 'heroku_b1c0a9f2a3d0817'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
bcrypt = Bcrypt(app)
