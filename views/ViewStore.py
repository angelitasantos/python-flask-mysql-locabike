from models.ModelStore import *
from models.Form import *


@app.route('/store_register', methods=['GET', 'POST'])
def store_register():
    title = 'Store Register'
    form = ModelFormPeople()
    try:
        if session['amail'] != '' and session['stores'] == 1:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
            response = cursor.fetchall()
            return render_template('/store/store/store_register.html', response=response, title=title, form=form)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/create_store', methods=['GET','POST'])
def create_store():
    StoreRegister()
    return redirect(url_for('store_list'))


@app.route('/store_list')
def store_list():
    title = 'Stores List'
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '' and session['stores'] == 1:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM stores s JOIN companies c ON c.id = s.id_company ORDER BY s.nome ASC')
            response = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Store Not Found...!!!!', 'danger')
            return render_template('/store/store/store_list.html', response=response, companies=companies, title=title)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route("/storerecords",methods=["POST","GET"])
def storerecords():
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        query = request.form['query']
        if query == '':
            cursor.execute("SELECT * FROM stores ORDER BY nome ASC")
            responselist = cursor.fetchall()
        else:
            search_text = request.form['query']
            print(search_text)
            cursor.execute("SELECT * FROM stores WHERE id_company IN (%s) ORDER BY nome ASC", [search_text])
            responselist = cursor.fetchall()  
    return jsonify({'htmlresponse': render_template('/store/store/store_response.html', responselist=responselist)})


@app.route('/store_edit/<string:id>')
def store_edit(id):
    title = 'Store Edit'
    form = ModelFormPeople()
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '' and session['stores'] == 1:
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM stores s JOIN companies c ON c.id = s.id_company WHERE s.id = %s'
            cursor.execute(query,[id])
            response = cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count != 0:
                return render_template('/store/store/store_edit.html', response=response, companies=companies, title=title, form=form)
        elif session['amail'] != '' and session['stores'] == 0:
            flash('Dont Have Access To This functionality...!!!!', 'danger')
            return render_template('/layout/store.html', title='Store')
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/update_store', methods=['GET','POST'])
def update_store():
    StoreUpdate()
    return redirect(url_for('store_list'))


@app.route('/delete_stores/<string:id>', methods = ['GET', 'POST'])
def delete_stores(id):
    try:
        if session['amail'] != '' and session['stores'] == 1:
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM stores'
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 1:
                flash('Last Store Cant Be Deleted...!!!!', 'danger')
            else:
                cursor = mysql.connection.cursor()
                cursor.execute('DELETE FROM stores WHERE id = %s', [id])
                mysql.connection.commit()
                flash('Store Deleted Successfully...!!!', 'success')
        elif session['amail'] != '' and session['companies'] == 0:
            flash('Dont Have Access To This functionality...!!!!', 'danger')
            return render_template('/layout/store.html', title = 'Store')
    except Exception as e:
        print(e)
    return redirect(url_for('store_list'))