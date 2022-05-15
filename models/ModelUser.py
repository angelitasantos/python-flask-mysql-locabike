from flask import Flask, render_template, url_for, redirect, flash, session, request
import random
from conexao_mysql import *


class ModelUser:

    def __init__(self) -> None:
        pass 
        

    def gerar_codigo_verificacao(self):
        digits = '0123456789'
        qnt = 6
        qntInt = int(qnt)
        length = qntInt
        all = digits
        id = "".join(random.sample(all, length))
        return id


    def AdminRegister(self):
        if request.method == 'POST':
            aname = request.form['aname']
            apassword = request.form['apassword']
            aconfirmpassword = request.form['aconfirmpassword']
            password_hash = bcrypt.generate_password_hash(apassword).decode('utf-8')

            amail = request.form['amail']
            sitedata = request.form['sitedata']
            companies = request.form['companies']
            stores = request.form['stores']
            admins = request.form['admins']

            try:
                cursor = mysql.connection.cursor()
                cursor.execute('SELECT * FROM admins WHERE amail = %s', [amail])
                cursor.fetchone()
                cursor.close()
                count = cursor.rowcount
                if count == 0 and apassword == aconfirmpassword:
                    cursor = mysql.connection.cursor()
                    cursor.execute('''INSERT INTO admins 
                    (aname, apassword, amail, sitedata, companies, stores, admins) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                    [aname, password_hash, amail, sitedata, companies, stores, admins])
                    mysql.connection.commit()
                    flash('Admin Created Successfully...!!!', 'success')
                elif count == 0 and apassword != aconfirmpassword:
                    flash('Password and Confirm Password Dont Match...!!!', 'danger')
                else:
                    flash('Admin Found...!!!', 'danger')
            except Exception as error:
                print(error)


    def AdminLogin(self):
        if request.method == 'POST':
            amail = request.form['amail']
            apassword = request.form['apassword']        
            try:
                cursor = mysql.connection.cursor()
                cursor.execute('SELECT * FROM admins WHERE amail = %s', [amail])
                response = cursor.fetchone()
                if response:
                    password_hash = response['apassword']
                    if bcrypt.check_password_hash(password_hash, apassword):
                        session['aname'] = response['aname']
                        session['apassword'] = response['apassword']
                        session['amail'] = response['amail']
                        session['sitedata'] = response['sitedata']
                        session['companies'] = response['companies']
                        session['stores'] = response['stores']
                        session['admins'] = response['admins']
                        session['acode'] = response['acode']
                        session['aid'] = response['aid']
                    else:
                        flash("Invalid Username or Password...!!!", "danger")
                else:
                    flash("Username Not Found...!!!", "danger")
            except Exception as error:
                print(error)


    def AdminUpdate(self):
        if request.method == 'POST':
            name = request.form['aname']
            sitedata = request.form['sitedata']
            companies = request.form['companies']
            stores = request.form['stores']
            admins = request.form['admins']
            aid = request.form['aid']
            
            cursor = mysql.connection.cursor()
            cursor.execute('''UPDATE admins 
            SET aname = %s, sitedata = %s, companies = %s, stores = %s, admins = %s
            WHERE aid = %s''',[name, sitedata, companies, stores, admins, aid])
            mysql.connection.commit()
            flash("Admin Profile Updated Successfully...!!!", "success")


    def AdminUpdatePass(self):
        if request.method == 'POST':
            amail = request.form['amail']
            apassword = request.form['apassword']

            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM admins WHERE amail = %s', [amail])
            response = cursor.fetchone()
            if response:
                password_hash = response['apassword']
                if bcrypt.check_password_hash(password_hash, apassword):
                    anewpassword = request.form['anewpassword']
                    aconfirmnewpassword = request.form['aconfirmnewpassword']
                    newpassword_hash = bcrypt.generate_password_hash(anewpassword).decode('utf-8')
                    if anewpassword == aconfirmnewpassword:
                        cursor.execute('''UPDATE admins 
                        SET apassword = %s
                        WHERE amail = %s''',[newpassword_hash, amail])
                        mysql.connection.commit()
                        flash("Password Updated Successfully...!!!", "success")
                    elif anewpassword != aconfirmnewpassword:
                        flash('Password and Confirm Password Dont Match...!!!!', 'danger')
                else:
                    flash("Invalid Current Password...!!!", "danger")


    def AdminRedefinePass(self):
        if request.method == 'POST':
            amail = request.form['amail']
            acode = request.form['acode']

            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM admins WHERE amail = %s and acode = %s', [amail, acode])
            response = cursor.fetchone()

            if response:
                anewpassword = request.form['anewpassword']
                aconfirmnewpassword = request.form['aconfirmnewpassword']
                newpassword_hash = bcrypt.generate_password_hash(anewpassword).decode('utf-8')

                if request.form['acode'] == response['acode']:
                    if anewpassword == aconfirmnewpassword:
                        cursor.execute('''UPDATE admins 
                        SET apassword = %s
                        WHERE amail = %s''',[newpassword_hash, amail])
                        mysql.connection.commit()
                        flash('Password Redefined Successfully...!!!', 'success')
                    elif anewpassword != aconfirmnewpassword:
                        flash('New Password and Confirm New Password Dont Match...!!!', 'danger')
            else:
                flash('Username or Verification Code Dont Correct...!!!', 'danger')