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
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM providers p JOIN companies c ON c.id = p.id_company ORDER BY p.nome ASC')
            response = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Provider Not Found...!!!!', 'danger')
            return render_template('/store/provider/provider_list.html', response=response, companies=companies, title=title)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route("/providerrecords",methods=["POST","GET"])
def providerrecords():
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        query = request.form['query']
        if query == '':
            cursor.execute("SELECT * FROM providers ORDER BY nome ASC")
            responselist = cursor.fetchall()
        else:
            search_text = request.form['query']
            print(search_text)
            cursor.execute("SELECT * FROM providers WHERE id_company IN (%s) ORDER BY nome ASC", [search_text])
            responselist = cursor.fetchall()  
    return jsonify({'htmlresponse': render_template('/store/provider/provider_response.html', responselist=responselist)})


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


@app.route('/delete_providers/<string:id>', methods = ['GET', 'POST'])
def delete_providers(id):
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM providers'
            cursor.execute(query)
            data = cursor.fetchall()
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