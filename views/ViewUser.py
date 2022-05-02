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

