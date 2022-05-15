from models.ModelClient import *
from models.Form import *


@app.route('/client_register', methods=['GET', 'POST'])
def client_register():
    title = 'Client Register'
    form = ModelFormPeople()
    ClientRegister()
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
            response = cursor.fetchall()
            return render_template('/store/client/client_register.html', response=response, title=title, form=form)
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route('/client_list')
def client_list():
    title = 'View Clients'
    company = 4
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, nome, cidade, uf FROM clients ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM clients cl JOIN companies c ON c.id = cl.id_company ORDER BY cl.nome ASC'
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Client Not Found...!!!!', 'danger')
            return render_template('/store/client/client_list.html', response = data, companies = companies, title = title, company = company)
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route('/client_edit/<string:id>')
def client_edit(id):
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


@app.route('/update_client', methods = ['GET','POST'])
def update_client():
    #ModelProvider.ProviderUpdate(self)
    return redirect(url_for('provider_list'))