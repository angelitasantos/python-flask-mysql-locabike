from flask import Flask, render_template, url_for, redirect, flash, session, request
from conexao_mysql import *


class ModelUser:

    def __init__(self) -> None:
        pass     


    def AdminLogin(self):
        if request.method == 'POST':
            amail = request.form['amail']
            apassword = request.form['apassword']        

            try:
                cursor = mysql.connection.cursor()
                cursor.execute('SELECT * FROM admins WHERE amail = %s', [amail])
                res = cursor.fetchone()
                if res:
                    pw_hash = res['apassword']
                    if bcrypt.check_password_hash(pw_hash, apassword):
                        session['aname'] = res['aname']
                        session['amail'] = res['amail']
                        session['sitedata'] = res['sitedata']
                        session['companies'] = res['companies']
                        session['stores'] = res['stores']
                        session['admins'] = res['admins']
                        session['aid'] = res['aid']
                        return redirect(url_for('home'))
                    else:
                        flash("Invalid Username or Password!", "danger")
                else:
                    flash("Username Not Found!", "danger")
            except Exception as e:
                print(e)
