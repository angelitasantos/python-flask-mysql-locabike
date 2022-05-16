from models.ModelProvider import *
from models.Form import *


@app.route('/provider_register', methods=['GET', 'POST'])
def provider_register():
    title = 'Provider Register'
    form = ModelFormPeople()
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
            response = cursor.fetchall()
            return render_template('/store/provider/provider_register.html', response=response, title=title, form=form)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/create_provider', methods=['GET','POST'])
def create_provider():
    ProviderRegister()
    return redirect(url_for('provider_list'))


@app.route('/provider_list')
def provider_list():
    title = 'Providers List'
    company = 1
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM providers p JOIN companies c ON c.id = p.id_company ORDER BY p.nome ASC'
            cursor.execute(query)
            response = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Provider Not Found...!!!!', 'danger')
            return render_template('/store/provider/provider_list.html', response=response, companies=companies, title=title, company=company)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/provider_edit/<string:id>')
def provider_edit(id):
    title = 'Provider Edit'
    form = ModelFormPeople()
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM providers p JOIN companies c ON c.id = p.id_company WHERE p.id = %s'
            cursor.execute(query,[id])
            response = cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count != 0:
                return render_template('/store/provider/provider_edit.html', response=response, companies=companies, title=title, form=form)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/update_provider', methods=['GET','POST'])
def update_provider():
    ProviderUpdate()
    return redirect(url_for('provider_list'))