from main import *
from flask import Flask, render_template, flash, request
from flask_mail import Mail, Message


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'angelju78@gmail.com'
app.config['MAIL_PASSWORD'] = 'dyvrslflszutrlrg'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
