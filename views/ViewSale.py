from models.ModelSale import *
from models.Form import *


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


@app.route('/product_list')
def product_list():
    title = 'Products List'
    try:
        cursor = mysql.connection.cursor()
        query = 'SELECT * FROM brands'
        cursor.execute(query)
        brands = cursor.fetchall()
        cursor = mysql.connection.cursor()
        query = 'SELECT * FROM categories'
        cursor.execute(query)
        categories = cursor.fetchall()
        if session['amail'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM products'
            cursor.execute(query)
            response = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Product Not Found...!!!!', 'danger')
            return render_template('/store/sale/product_list.html', response=response, brands=brands, categories=categories, title=title)
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route("/product_search", methods = ["POST","GET"])
def product_search():
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)
        if search_word != '':
            query = "SELECT * from products WHERE name LIKE '%{}%' OR description LIKE '%{}%' ORDER BY name ASC LIMIT 20".format(search_word,search_word)
            cursor.execute(query)
            numrows = int(cursor.rowcount)
            response = cursor.fetchall()
            print(numrows)
    return jsonify({'htmlresponse': render_template('/store/sale/product_response.html', response=response, numrows=numrows)})


@app.route('/brand_select/<string:id>')
def brand_select(id):
    title = 'Product for Brand'
    try:
        cursor = mysql.connection.cursor()
        query = 'SELECT * FROM brands'
        cursor.execute(query)
        brands = cursor.fetchall()
        cursor = mysql.connection.cursor()
        query = 'SELECT * FROM categories'
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
        query = 'SELECT * FROM brands'
        cursor.execute(query)
        brands = cursor.fetchall()
        cursor = mysql.connection.cursor()
        query = 'SELECT * FROM categories'
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



