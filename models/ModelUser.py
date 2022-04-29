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
            flash("Admin Profile Updated Successfully!", "success")


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
                title = 'Admin Profile'
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
                    flash('Admin Created Successfully', 'success')
                    return render_template('/store/admin_profile.html', title = title)
                elif count == 0 and apassword != aconfirmpassword:
                    flash('Password and Confirm Password Dont Match...!!!!', 'danger')
                    return render_template('/store/admin_profile.html', title = title)
                else:
                    flash('Admin Found...!!!!', 'danger')
                    return render_template('/store/admin_profile.html', title = title)
            except Exception as e:
                print(e)
