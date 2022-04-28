from models.ModelUser import *
self = 'self'


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    title = 'Admin'
    ModelUser.AdminLogin(self)
    try:
        if session['aname'] != '':
            return render_template('/pages/about.html', title = 'About')
    except Exception as e:
        print(e)
    try:
        if session['name'] != '':
            return render_template('/pages/home.html', title = 'Home')
    except Exception as e:
        print(e)
    return render_template('/store/admin.html', title = title)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/admin_profile')
def admin_profile():
    title = 'Admin Profile'
    try:
        if session['aname'] != '':
            cursor = mysql.connection.cursor()
            id = session['aid']
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
        if session['aname'] != '':
            return render_template('/pages/about.html', title = 'About')
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route('/update_admin',methods=['GET','POST'])
def update_admin():
    ModelUser.AdminUpdate(self)
    return redirect('admin_profile')
