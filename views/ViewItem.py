from models.ModelItem import *
from models.Form import *


@app.route('/item_register', methods=['GET', 'POST'])
def item_register():
    title = 'Item Register'
    form = ModelFormItem()
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
            response = cursor.fetchall()
            return render_template('/store/item/item_register.html', response=response, title=title, form=form)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/create_item', methods=['GET','POST'])
def create_item():
    ItemRegister()
    return redirect(url_for('item_list'))


@app.route('/item_list')
def item_list():
    title = 'Items List'
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM items i JOIN companies c ON c.id = i.id_company ORDER BY i.nome ASC')
            response = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Item Not Found...!!!!', 'danger')
            return render_template('/store/item/item_list.html', response=response, companies=companies, title=title)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route("/itemrecords",methods=["POST","GET"])
def itemrecords():
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        query = request.form['query']
        if query == '':
            cursor.execute("SELECT * FROM items ORDER BY nome ASC")
            responselist = cursor.fetchall()
        else:
            search_text = request.form['query']
            print(search_text)
            cursor.execute("SELECT * FROM items WHERE id_company IN (%s) ORDER BY nome ASC", [search_text])
            responselist = cursor.fetchall()  
    return jsonify({'htmlresponse': render_template('/store/item/item_response.html', responselist=responselist)})


@app.route('/item_view/<string:id>')
def item_view(id):
    title = 'Item View'
    form = ModelFormItem()
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM items i JOIN companies c ON c.id = i.id_company WHERE i.id = %s'
            cursor.execute(query,[id])
            response = cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count != 0:
                return render_template('/store/item/item_view.html', response=response, companies=companies, title=title, form=form)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/item_edit/<string:id>')
def item_edit(id):
    title = 'Item Edit'
    form = ModelFormItem()
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM items i JOIN companies c ON c.id = i.id_company WHERE i.id = %s'
            cursor.execute(query,[id])
            response = cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count != 0:
                return render_template('/store/item/item_edit.html', response=response, companies=companies, title=title, form=form)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/update_item', methods=['GET','POST'])
def update_item():
    ItemUpdate()
    return redirect(url_for('item_list'))


@app.route('/delete_items/<string:id>', methods = ['GET', 'POST'])
def delete_items(id):
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM items'
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 1:
                flash('Last Item Cant Be Deleted...!!!!', 'danger')
            else:
                cursor = mysql.connection.cursor()
                cursor.execute('DELETE FROM items WHERE id = %s', [id])
                mysql.connection.commit()
                flash('Item Deleted Successfully...!!!', 'success')
        elif session['amail'] != '' and session['companies'] == 0:
            flash('Dont Have Access To This functionality...!!!!', 'danger')
            return render_template('/layout/store.html', title = 'Store')
    except Exception as e:
        print(e)
    return redirect(url_for('item_list'))