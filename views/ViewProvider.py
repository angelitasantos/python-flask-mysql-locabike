from models.ModelProvider import *

self = 'self'


@app.route('/provider_list')
def provider_list():
    title = 'View Providers'
    company = 4
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM providers p JOIN companies c ON c.id = p.id_company ORDER BY p.nome ASC'
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Provider Not Found...!!!!', 'danger')
            return render_template('/store/provider/provider_list.html', response = data, companies = companies, title = title, company = company)
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route('/provider_register', methods = ['GET', 'POST'])
def provider_register():
    title = 'Provider Register'
    ModelProvider.ProviderRegister(self)
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
            data = cursor.fetchall()
            return render_template('/store/provider/provider_register.html', data = data, title = title)
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')



@app.route('/provider_edit/<string:id>')
def provider_edit(id):
    title = 'Provider Edit'
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM providers p JOIN companies c ON c.id = p.id_company WHERE p.id = %s'
            cursor.execute(query,[id])
            data = cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count != 0:
                return render_template('/store/provider/provider_edit.html', res = data, companies = companies, title = title)
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route('/update_provider', methods = ['GET','POST'])
def update_provider():
    ModelProvider.ProviderUpdate(self)
    return redirect(url_for('provider_list'))