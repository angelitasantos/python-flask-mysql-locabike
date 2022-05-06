from flask import Flask, render_template, url_for, redirect, flash, session, request, jsonify
from conexao_mysql import *


class ModelCompany:

    def __init__(self) -> None:
        pass


    def CompanyRegister(self):
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
                    cursor.execute('''INSERT INTO admins (aname, apassword, amail, sitedata, companies, stores, admins) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)''',[aname, password_hash, amail, sitedata, companies, stores, admins])
                    mysql.connection.commit()
                    flash('Admin Created Successfully...!!!', 'success')
                elif count == 0 and apassword != aconfirmpassword:
                    flash('Password and Confirm Password Dont Match...!!!', 'danger')
                else:
                    flash('Admin Found...!!!', 'danger')
            except Exception as e:
                print(e)