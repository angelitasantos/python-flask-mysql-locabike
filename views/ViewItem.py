from models.ModelItem import *
from models.Form import *


select_company = '''SELECT id, nome, cidade, uf 
                    FROM companies 
                    ORDER BY nome ASC'''
select_companies = '''  SELECT *, c.nome 
                        FROM items i 
                        JOIN companies c 
                        ON c.id = i.id_company 
                        GROUP BY 27'''


@app.route('/item_register', methods=['GET', 'POST'])
def item_register():
    title = 'Item Register'
    form = ModelFormItem()
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute(select_company)
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
        cursor.execute(select_companies)
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


@app.route('/company_item_select/<string:id>')
def company_item_select(id):
    title = 'Item for Company'
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(select_companies)
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = ''' SELECT * FROM items i 
                        WHERE i.id_company = %s'''
            cursor.execute(query,[id])
            company = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count != 0:
                return render_template('/store/item/item_list.html', companies=companies, company=company, title=title)
            else:
                return render_template('/store/item/item_list.html', companies=companies, company=company, title=title)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/item_edit/<string:id>')
def item_edit(id):
    title = 'Item Edit'
    form = ModelFormItem()
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(select_company)
        companies = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = ''' SELECT * FROM items i 
                        JOIN companies c ON c.id = i.id_company 
                        WHERE i.id = %s'''
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
            cursor.execute('SELECT * FROM items')
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