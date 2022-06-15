from models.ModelProvider import *
from models.Form import *


select_company = '''SELECT id, nome, cidade, uf 
                    FROM companies 
                    ORDER BY nome ASC'''
select_companies = '''  SELECT *, c.nome 
                        FROM providers p 
                        JOIN companies c 
                        ON c.id = p.id_company 
                        GROUP BY 22'''


@app.route('/provider_register', methods=['GET', 'POST'])
def provider_register():
    title = 'Provider Register'
    form = ModelFormPeople()
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute(select_company)
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
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(select_companies)
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('''  SELECT * FROM providers p 
                                JOIN companies c ON c.id = p.id_company 
                                ORDER BY p.nome ASC''')
            response = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Provider Not Found...!!!!', 'danger')
            return render_template('/store/provider/provider_list.html', response=response, companies=companies, title=title)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/company_provider_select/<string:id>')
def company_provider_select(id):
    title = 'Provider for Company'
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(select_companies)
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = ''' SELECT * FROM providers p 
                        WHERE p.id_company = %s'''
            cursor.execute(query,[id])
            company = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count != 0:
                return render_template('/store/provider/provider_list.html', companies=companies, company=company, title=title)
            else:
                return render_template('/store/provider/provider_list.html', companies=companies, company=company, title=title)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/provider_edit/<string:id>')
def provider_edit(id):
    title = 'Provider Edit'
    form = ModelFormPeople()
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(select_company)
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


@app.route('/delete_providers/<string:id>', methods = ['GET', 'POST'])
def delete_providers(id):
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM providers')
            cursor.close()
            count = cursor.rowcount
            if count == 1:
                flash('Last Provider Cant Be Deleted...!!!!', 'danger')
            else:
                cursor = mysql.connection.cursor()
                cursor.execute('DELETE FROM providers WHERE id = %s', [id])
                mysql.connection.commit()
                flash('Provider Deleted Successfully...!!!', 'success')
        elif session['amail'] != '' and session['companies'] == 0:
            flash('Dont Have Access To This functionality...!!!!', 'danger')
            return render_template('/layout/store.html', title = 'Store')
    except Exception as e:
        print(e)
    return redirect(url_for('provider_list'))