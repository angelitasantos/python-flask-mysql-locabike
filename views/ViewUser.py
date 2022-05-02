from models.ModelMail import *
from models.ModelUser import *

self = 'self'


@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    title = 'Admin'
    ModelUser.AdminLogin(self)
    try:
        if session['amail'] != '':
            return render_template('/pages/about.html', title = 'About')
    except Exception as e:
        print(e)
    try:
        if session['umail'] != '':
            return render_template('/pages/home.html', title = 'Home')
    except Exception as e:
        print(e)
    return render_template('/store/admin.html', title = title)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/admin_profile/<string:id>')
def admin_profile(id):
    title = 'Admin Profile'
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM admins WHERE aid = %s'
            cursor.execute(query,[id])
            data = cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Users Not Found...!!!!', 'danger')
                return render_template('/store/admin_profile.html', res = data, title = title)
            else:
                return render_template('/store/admin_profile.html', res = data, title = title)
    except Exception as e:
        print(e)
    try:
        if session['umail'] != '':
            return render_template('/pages/about.html', title = 'About')
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route('/update_admin', methods = ['GET','POST'])
def update_admin():
    ModelUser.AdminUpdate(self)
    return redirect(url_for('admin_list'))


@app.route('/admin_register', methods = ['GET', 'POST'])
def admin_register():
    title = 'Admin Register'
    ModelUser.AdminRegister(self)
    try:
        if session['amail'] != '' and session['admins'] == 1:
            return render_template('/store/admin_register.html', title = title)
    except Exception as e:
        print(e)
    try:
        if session['umail'] != '':
            return render_template('/pages/about.html', title = 'About')
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route('/admin_list')
def admin_list():
    title = 'View Admins'
    try:
        if session['amail'] != '' and session['admins'] == 1:
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM admins'
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Admins Not Found...!!!!', 'danger')
            return render_template('/store/admin_list.html', res = data, title = title)
        else:
            redirect(url_for('home'))
    except Exception as e:
        print(e)
    return render_template('/pages/home.html')


@app.route('/delete_admins/<string:id>', methods = ['GET', 'POST'])
def delete_admins(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM admins WHERE aid = %s', [id])
    mysql.connection.commit()
    flash('Admin Deleted Successfully', 'danger')
    return redirect(url_for('admin_list'))


@app.route('/admin_passchange')
def admin_passchange():
    title = 'Change Password'
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            id = session['aid']
            query = 'SELECT * FROM admins WHERE aid = %s'
            cursor.execute(query,[id])
            data = cursor.fetchone()
            cursor.close()
            return render_template('/store/admin_passchange.html', res = data, title = title)
    except Exception as e:
        print(e)
    try:
        if session['umail'] != '':
            return render_template('/pages/about.html', title = 'About')
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route('/update_password', methods = ['GET', 'POST'])
def update_password():
    ModelUser.AdminUpdatePass(self)
    session.clear()
    flash("Password Updated Successfully! Please, Login Again!", "success")
    return redirect(url_for('admin'))


@app.route('/admin_passforgot')
def admin_passforgot():
    title = 'Forgot Password'
    try:
        if session['amail'] != '':
            return render_template('/pages/about.html', title = 'About')
    except Exception as e:
        print(e)
    try:
        if session['umail'] != '':
            return render_template('/pages/about.html', title = 'About')
    except Exception as e:
        print(e)
    return render_template('/store/admin_passforgot.html', title = title)
    

@app.route('/send_message_passforgot', methods = ['GET', 'POST'])
def send_message_passforgot():
    title = 'Forgot Password'
    try:
        if request.method == 'POST':
            code = ModelUser.gerar_codigo_verificacao(self)
            email = request.form['amail']
            subject = 'Forgot Password'
            msg = f'''Sent Verification Code: 
            {code}
            Link Redefine Password
            '''

            message = Message(subject, sender = app.config.get('MAIL_USERNAME'), recipients = [email])
            message.body = msg
            mail.send(message)

            try:
                cursor = mysql.connection.cursor()
                cursor.execute('SELECT * FROM admins WHERE amail = %s', [email])
                cursor.fetchone()
                cursor.close()
                count = cursor.rowcount
                if count != 0:
                    cursor = mysql.connection.cursor()
                    cursor.execute('''UPDATE admins 
                    SET acode = %s
                    WHERE amail = %s''',[code, email])
                    mysql.connection.commit()
                    flash('Mail Sent Successfully!', 'success')
                    return render_template('/store/admin_passforgot.html', title = title)
                else:
                    flash('Admin Not Found...!!!!', 'danger')
                    return render_template('/store/admin_passforgot.html', title = title)
            except Exception as e:
                print(e)
    except:
        flash('Mail Dont Sent', 'danger')
        pass
    return render_template('/store/admin_passforgot.html')


@app.route('/admin_passredefine')
def admin_passredefine():
    title = 'Redefine Password'
    try:
        if session['amail'] != '' or session['umail'] != '':
            return render_template('/pages/about.html', title = 'About')
    except Exception as e:
        print(e)
    return render_template('/store/admin_passredefine.html', title = title)


@app.route('/redefine_password', methods = ['GET', 'POST'])
def redefine_password():
    ModelUser.AdminRedefinePass(self)
    return redirect(url_for('admin_passredefine'))
