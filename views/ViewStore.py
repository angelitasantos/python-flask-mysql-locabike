from models.ModelStore import *

self = 'self'


@app.route('/store_list')
def store_list():
    title = 'View Stores'
    company = 4
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '' and session['stores'] == 1:
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM stores s JOIN companies c ON c.id = s.id_company ORDER BY s.nome ASC'
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Store Not Found...!!!!', 'danger')
            return render_template('/store/store/store_list.html', response = data, companies = companies, title = title, company = company)
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route('/store_register', methods = ['GET', 'POST'])
def store_register():
    title = 'Store Register'
    ModelStore.StoreRegister(self)
    try:
        if session['amail'] != '' and session['stores'] == 1:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
            data = cursor.fetchall()
            return render_template('/store/store/store_register.html', data = data, title = title)
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')



@app.route('/store_edit/<string:id>')
def store_edit(id):
    title = 'Store Edit'
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '' and session['stores'] == 1:
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM stores s JOIN companies c ON c.id = s.id_company WHERE s.id = %s'
            cursor.execute(query,[id])
            data = cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count != 0:
                return render_template('/store/store/store_edit.html', res = data, companies = companies, title = title)
        elif session['amail'] != '' and session['stores'] == 0:
            flash('Dont Have Access To This functionality...!!!!', 'danger')
            return render_template('/layout/store.html', title = 'Store')
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route('/update_store', methods = ['GET','POST'])
def update_store():
    ModelStore.StoreUpdate(self)
    return redirect(url_for('store_list'))