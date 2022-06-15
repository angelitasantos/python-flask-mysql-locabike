from models.ModelClient import *
from models.Form import *


select_company = '''SELECT id, nome, cidade, uf 
                    FROM companies 
                    ORDER BY nome ASC'''
select_companies = '''  SELECT *, c.nome 
                        FROM clients cl 
                        JOIN companies c 
                        ON c.id = cl.id_company 
                        GROUP BY 22'''


@app.route('/client_register', methods=['GET', 'POST'])
def client_register():
    title = 'Client Register'
    form = ModelFormPeople()
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute(select_company)
            response = cursor.fetchall()
            return render_template('/store/client/client_register.html', response=response, title=title, form=form)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/create_client', methods=['GET','POST'])
def create_client():
    ClientRegister()
    return redirect(url_for('client_list'))


@app.route('/client_list')
def client_list():
    title = 'Clients List'
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(select_companies)
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('''  SELECT * FROM clients cl 
                                JOIN companies c ON c.id = cl.id_company 
                                ORDER BY cl.nome ASC''')
            response = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Client Not Found...!!!!', 'danger')
            return render_template('/store/client/client_list.html', response=response, companies=companies, title=title)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/company_client_select/<string:id>')
def company_client_select(id):
    title = 'Client for Company'
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(select_companies)
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = ''' SELECT * FROM clients cl 
                        WHERE cl.id_company = %s'''
            cursor.execute(query,[id])
            company = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count != 0:
                return render_template('/store/client/client_list.html', companies=companies, company=company, title=title)
            else:
                return render_template('/store/client/client_list.html', companies=companies, company=company, title=title)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/client_edit/<string:id>')
def client_edit(id):
    title = 'Client Edit'
    form = ModelFormPeople()
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(select_company)
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = ''' SELECT * FROM clients cl 
                        JOIN companies c ON c.id = cl.id_company 
                        WHERE cl.id = %s'''
            cursor.execute(query,[id])
            response = cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count != 0:
                return render_template('/store/client/client_edit.html', response=response, companies=companies, title=title, form=form)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/update_client', methods=['GET','POST'])
def update_client():
    ClientUpdate()
    return redirect(url_for('client_list'))


@app.route('/delete_clients/<string:id>', methods = ['GET', 'POST'])
def delete_clients(id):
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM clients')
            cursor.close()
            count = cursor.rowcount
            if count == 1:
                flash('Last Client Cant Be Deleted...!!!!', 'danger')
            else:
                cursor = mysql.connection.cursor()
                cursor.execute('DELETE FROM clients WHERE id = %s', [id])
                mysql.connection.commit()
                flash('Client Deleted Successfully...!!!', 'success')
        elif session['amail'] != '' and session['companies'] == 0:
            flash('Dont Have Access To This functionality...!!!!', 'danger')
            return render_template('/layout/store.html', title = 'Store')
    except Exception as error:
        print(error)
    return redirect(url_for('client_list'))