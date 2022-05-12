from models.ModelMail import *
from models.ModelUser import *

self = 'self'


@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    title = 'Admin'
    ModelUser.AdminLogin(self)
    try:
        if session['amail'] != '':
            return render_template('/layout/store.html', title = 'Store')
    except Exception as e:
        print(e)
    try:
        if session['umail'] != '':
            return render_template('/pages/home.html', title = 'Home')
    except Exception as e:
        print(e)
    return render_template('/store/admin/admin.html', title = title)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/admin_profile/<string:id>')
def admin_profile(id):
    title = 'Admin Profile'
    try:
        if session['amail'] != '' and session['admins'] == 1:
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM admins WHERE aid = %s'
            cursor.execute(query,[id])
            data = cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count != 0:
                return render_template('/store/admin/admin_profile.html', res = data, title = title)
        elif session['amail'] != '' and session['admins'] == 0:
            flash('Dont Have Access To This functionality...!!!!', 'danger')
            return render_template('/layout/store.html', title = 'Store')
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
            return render_template('/store/admin/admin_register.html', title = title)
        elif session['amail'] != '' and session['admins'] == 0:
            flash('Dont Have Access To This functionality...!!!!', 'danger')
            return render_template('/layout/store.html', title = 'Store')
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
            return render_template('/store/admin/admin_list.html', res = data, title = title)
        elif session['amail'] != '' and session['admins'] == 0:
            flash('Dont Have Access To This functionality...!!!!', 'danger')
            return render_template('/layout/store.html', title = 'Store')
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route('/delete_admins/<string:id>', methods = ['GET', 'POST'])
def delete_admins(id):
    try:
        if session['amail'] != '' and session['admins'] == 1:
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM admins'
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 1:
                flash('Admin Cant Be Deleted...!!!!', 'danger')
            else:
                cursor = mysql.connection.cursor()
                cursor.execute('DELETE FROM admins WHERE aid = %s', [id])
                mysql.connection.commit()
                flash('Admin Deleted Successfully...!!!', 'danger')
        elif session['amail'] != '' and session['admins'] == 0:
            flash('Dont Have Access To This functionality...!!!!', 'danger')
            return render_template('/layout/store.html', title = 'Store')
    except Exception as e:
        print(e)
    return redirect(url_for('admin_list'))


@app.route('/admin_pass_change')
def admin_pass_change():
    title = 'Change Password'
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            id = session['aid']
            query = 'SELECT * FROM admins WHERE aid = %s'
            cursor.execute(query,[id])
            data = cursor.fetchone()
            cursor.close()
            return render_template('/store/admin/admin_pass_change.html', res = data, title = title)
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route('/update_password', methods = ['GET', 'POST'])
def update_password():
    ModelUser.AdminUpdatePass(self)
    return redirect(url_for('admin_pass_change'))


@app.route('/admin_pass_forgot')
def admin_pass_forgot():
    title = 'Forgot Password'
    try:
        if session['amail'] != '':
            return render_template('/layout/store.html', title = 'Store')
    except Exception as e:
        print(e)
    try:
        if session['umail'] != '':
            return render_template('/pages/home.html', title = 'Home')
    except Exception as e:
        print(e)
    return render_template('/store/admin/admin_pass_forgot.html', title = title)
    

@app.route('/send_message_passforgot', methods = ['GET', 'POST'])
def send_message_passforgot():
    forgot = 'Forgot Password'
    redefine = 'Redefine Password'
    try:
        if request.method == 'POST':
            code = ModelUser.gerar_codigo_verificacao(self)
            email = request.form['amail']
            subject = 'Forgot Password'
            msg = f'''Sent Verification Code: 
            {code}
            Link Redefine Password
            '''

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

                    message = Message(subject, sender = app.config.get('MAIL_USERNAME'), recipients = [email])
                    message.body = msg
                    mail.send(message)
                    
                    flash('Mail Sent Successfully...!!!', 'success')
                    return render_template('/store/admin/admin_pass_redefine.html', title = redefine)
                else:
                    flash('Admin Not Found...!!!', 'danger')
                    return render_template('/store/admin/admin_pass_forgot.html', title = forgot)
            except Exception as e:
                print(e)
    except:
        flash('Mail Dont Sent...!!!', 'danger')
        pass
    return render_template('/store/admin/admin_pass_forgot.html')


@app.route('/admin_pass_redefine')
def admin_pass_redefine():
    title = 'Redefine Password'
    try:
        if session['amail'] != '':
            return render_template('/layout/store.html', title = 'Store')
    except Exception as e:
        print(e)
    try:
        if session['umail'] != '':
            return render_template('/pages/home.html', title = 'Home')
    except Exception as e:
        print(e)
    return render_template('/store/admin/admin_pass_redefine.html', title = title)


@app.route('/redefine_password', methods = ['GET', 'POST'])
def redefine_password():
    ModelUser.AdminRedefinePass(self)
    return redirect(url_for('admin_pass_redefine'))
