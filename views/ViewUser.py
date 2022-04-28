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
