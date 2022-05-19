from models.ModelClient import *
from models.Form import *


@app.route('/client_register', methods=['GET', 'POST'])
def client_register():
    title = 'Client Register'
    form = ModelFormPeople()
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
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
        cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM clients cl JOIN companies c ON c.id = cl.id_company ORDER BY cl.nome ASC')
            response = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Client Not Found...!!!!', 'danger')
            return render_template('/store/client/client_list.html', response=response, companies=companies, title=title)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route("/clientrecords",methods=["POST","GET"])
def clientrecords():
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        query = request.form['query']
        if query == '':
            cursor.execute("SELECT * FROM clients ORDER BY nome ASC")
            responselist = cursor.fetchall()
        else:
            search_text = request.form['query']
            print(search_text)
            cursor.execute("SELECT * FROM clients WHERE id_company IN (%s) ORDER BY nome ASC", [search_text])
            responselist = cursor.fetchall()  
    return jsonify({'htmlresponse': render_template('/store/client/client_response.html', responselist=responselist)})


@app.route('/client_edit/<string:id>')
def client_edit(id):
    title = 'Client Edit'
    form = ModelFormPeople()
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM clients cl JOIN companies c ON c.id = cl.id_company WHERE cl.id = %s'
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
            query = 'SELECT * FROM clients'
            cursor.execute(query)
            data = cursor.fetchall()
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
    except Exception as e:
        print(e)
    return redirect(url_for('client_list'))