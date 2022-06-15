from models.ModelSale import *
from models.Form import *
import math


@app.route('/brand_register', methods=['GET', 'POST'])
def brand_register():
    title = 'Brand Register'
    form = ModelFormGroup()
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM brands ORDER BY description ASC')
            response = cursor.fetchall()
            return render_template('/store/sale/brand_register.html', response=response, title=title, form=form)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/create_brand', methods=['GET','POST'])
def create_brand():
    BrandRegister()
    return redirect(url_for('brand_register'))


@app.route('/category_register', methods=['GET', 'POST'])
def category_register():
    title = 'Category Register'
    form = ModelFormGroup()
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM categories ORDER BY description ASC')
            response = cursor.fetchall()
            return render_template('/store/sale/category_register.html', response=response, title=title, form=form)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/create_category', methods=['GET','POST'])
def create_category():
    CategoryRegister()
    return redirect(url_for('category_register'))


@app.route('/product_register', methods=['GET', 'POST'])
def product_register():
    title = 'Product Register'
    form = ModelFormProduct()
    try:
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT id, nome, cidade, uf FROM companies ORDER BY nome ASC')
            response = cursor.fetchall()
            cursor.execute('SELECT * FROM brands ORDER BY description ASC')
            brands = cursor.fetchall()
            cursor.execute('SELECT * FROM categories ORDER BY description ASC')
            categories = cursor.fetchall()
            return render_template('/store/sale/product_register.html', response=response, brands=brands, categories=categories, title=title, form=form)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/create_product', methods=['GET','POST'])
def create_product():
    ProductRegister()
    return redirect(url_for('product_register'))


@app.route('/product_list', defaults={'page':1})
@app.route('/product_list/page/<int:page>')
def product_list(page):
    title = 'Products List'
    try:
        cursor = mysql.connection.cursor()
        query = 'SELECT *, b.description FROM products p JOIN brands b ON b.id = p.id_brand GROUP BY 9'
        cursor.execute(query)
        brands = cursor.fetchall()
        query = 'SELECT *, c.description FROM products p JOIN categories c ON c.id = p.id_category GROUP BY 10'
        cursor.execute(query)
        categories = cursor.fetchall()
        if session['amail'] != '':
            perpage = 2
            startat = (page - 1) * perpage

            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM products')
            response = cursor.fetchall()
            cursor.close()
            registers = cursor.rowcount
            total_pages = math.ceil(registers / perpage)

            next = page + 1
            prev = page - 1

            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM products ORDER BY name ASC LIMIT %s, %s', (startat,perpage))
            response = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Product Not Found...!!!!', 'danger')
            return render_template('/store/sale/product_list.html', response=response, page=total_pages, next=next, prev=prev, brands=brands, categories=categories, title=title)
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route('/brand_select/<string:id>')
def brand_select(id):
    title = 'Product for Brand'
    try:
        cursor = mysql.connection.cursor()
        query = 'SELECT *, b.description FROM products p JOIN brands b ON b.id = p.id_brand GROUP BY 9'
        cursor.execute(query)
        brands = cursor.fetchall()
        cursor = mysql.connection.cursor()
        query = 'SELECT *, c.description FROM products p JOIN categories c ON c.id = p.id_category GROUP BY 10'
        cursor.execute(query)
        categories = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM products p WHERE p.id_brand = %s'
            cursor.execute(query,[id])
            brand = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count != 0:
                return render_template('/store/sale/product_list.html', brands=brands, brand=brand, categories=categories, title=title)
            else:
                return render_template('/store/sale/product_list.html', brands=brands, brand=brand, categories=categories, title=title)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/category_select/<string:id>')
def category_select(id):
    title = 'Product for Category'
    try:
        cursor = mysql.connection.cursor()
        query = 'SELECT *, b.description FROM products p JOIN brands b ON b.id = p.id_brand GROUP BY 9'
        cursor.execute(query)
        brands = cursor.fetchall()
        cursor = mysql.connection.cursor()
        query = 'SELECT *, c.description FROM products p JOIN categories c ON c.id = p.id_category GROUP BY 10'
        cursor.execute(query)
        categories = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM products p WHERE p.id_category = %s'
            cursor.execute(query,[id])
            category = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count != 0:
                return render_template('/store/sale/product_list.html', brands=brands, categories=categories, category=category, title=title)
            else:
                return render_template('/store/sale/product_list.html', brands=brands, categories=categories, category=category, title=title)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')
