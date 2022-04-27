from main import *
from flask import Flask, render_template, flash, request
from flask_mail import Mail, Message
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())
usermail = os.getenv('mailuser')
userpassword = os.getenv('mailpassword')


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = usermail
app.config['MAIL_PASSWORD'] = userpassword
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
