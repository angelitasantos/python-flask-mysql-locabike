from flask import Flask, render_template, url_for, redirect, flash, session, request
import random
from conexao_mysql import *


class ModelUser:

    def __init__(self):
        self.aname = request.form['aname']
        self.amail = request.form['amail']
        self.sitedata = request.form['sitedata']
        self.companies = request.form['companies']
        self.stores = request.form['stores']
        self.admins = request.form['admins']
        self.acode = request.form['acode']
        self.aid = request.form['aid']
        
        self.apassword = request.form['apassword']
        self.aconfirmpassword = request.form['aconfirmpassword']
        self.password_hash = bcrypt.generate_password_hash(self.apassword).decode('utf-8')
        self.anewpassword = request.form['anewpassword']
        self.aconfirmnewpassword = request.form['aconfirmnewpassword']
        self.newpassword_hash = bcrypt.generate_password_hash(self.anewpassword).decode('utf-8')
        

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
            try:
                cursor = mysql.connection.cursor()
                cursor.execute('SELECT * FROM admins WHERE amail = %s', [self.amail])
                cursor.fetchone()
                cursor.close()
                count = cursor.rowcount
                if count == 0 and self.apassword == self.aconfirmpassword:
                    cursor = mysql.connection.cursor()
                    cursor.execute('''INSERT INTO admins (aname, apassword, amail, sitedata, companies, stores, admins) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                    [self.aname, self.password_hash, self.amail, self.sitedata, self.companies, self.stores, self.admins])
                    mysql.connection.commit()
                    flash('Admin Created Successfully...!!!', 'success')
                elif count == 0 and self.apassword != self.aconfirmpassword:
                    flash('Password and Confirm Password Dont Match...!!!', 'danger')
                else:
                    flash('Admin Found...!!!', 'danger')
            except Exception as e:
                print(e)


    def AdminLogin(self):
        if request.method == 'POST':
            try:
                cursor = mysql.connection.cursor()
                cursor.execute('SELECT * FROM admins WHERE amail = %s', [self.amail])
                res = cursor.fetchone()
                if res:
                    pw_hash = res['apassword']
                    if bcrypt.check_password_hash(pw_hash, self.apassword):
                        session['aname'] = res['aname']
                        session['amail'] = res['amail']
                        session['apassword'] = res['apassword']
                        session['sitedata'] = res['sitedata']
                        session['companies'] = res['companies']
                        session['stores'] = res['stores']
                        session['admins'] = res['admins']
                        session['aid'] = res['aid']
                    else:
                        flash("Invalid Username or Password...!!!", "danger")
                else:
                    flash("Username Not Found...!!!", "danger")
            except Exception as e:
                print(e)


    def AdminUpdate(self):
        if request.method == 'POST':
            cursor = mysql.connection.cursor()
            cursor.execute('''UPDATE admins 
            SET aname = %s, sitedata = %s, companies = %s, stores = %s, admins = %s
            WHERE aid = %s''',[self.aname, self.sitedata, self.companies, self.stores, self.admins, self.aid])
            mysql.connection.commit()
            flash("Admin Profile Updated Successfully...!!!", "success")


    def AdminUpdatePass(self):
        if request.method == 'POST':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM admins WHERE amail = %s', [self.amail])
            res = cursor.fetchone()
            if res:
                pw_hash = res['apassword']
                if bcrypt.check_password_hash(pw_hash, self.apassword):
                    if self.anewpassword == self.aconfirmnewpassword:
                        cursor.execute('''UPDATE admins 
                        SET apassword = %s
                        WHERE amail = %s''',[self.newpassword_hash, self.amail])
                        mysql.connection.commit()
                        flash("Password Updated Successfully...!!!", "success")
                    elif self.anewpassword != self.aconfirmnewpassword:
                        flash('Password and Confirm Password Dont Match...!!!!', 'danger')
                else:
                    flash("Invalid Current Password...!!!", "danger")


    def AdminRedefinePass(self):
        if request.method == 'POST':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM admins WHERE amail = %s and acode = %s', [self.amail, self.acode])
            res = cursor.fetchone()
            if res:
                if request.form['acode'] == res['acode']:
                    if self.anewpassword == self.aconfirmnewpassword:
                        cursor.execute('''UPDATE admins 
                        SET apassword = %s
                        WHERE amail = %s''',[self.newpassword_hash, self.amail])
                        mysql.connection.commit()
                        flash('Password Redefined Successfully...!!!', 'success')
                    elif self.anewpassword != self.aconfirmnewpassword:
                        flash('New Password and Confirm New Password Dont Match...!!!', 'danger')
            else:
                flash('Username or Verification Code Dont Correct...!!!', 'danger')