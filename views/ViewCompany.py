from models.ModelCompany import *
from models.Form import *


@app.route('/company_register', methods=['GET', 'POST'])
def company_register():
    title = 'Company Register'
    form = ModelFormPeople()
    try:
        if session['amail'] != '' and session['companies'] == 1:
            return render_template('/store/company/company_register.html', title=title, form=form)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/create_company', methods=['GET','POST'])
def create_company():
    CompanyRegister()
    return redirect(url_for('company_list'))


@app.route('/company_list')
def company_list():
    title = 'Companies List'
    try:
        if session['amail'] != '' and session['companies'] == 1:
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM companies ORDER BY nome'
            cursor.execute(query)
            response = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Company Not Found...!!!!', 'danger')
            return render_template('/store/company/company_list.html', response=response, title=title)
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route("/company_search", methods=["POST","GET"])
def company_search():
    try:
        cursor = mysql.connection.cursor()
        if request.method == 'POST':
            search_word = request.form['query']
            print(search_word)
            if search_word != '':
                query = """SELECT * from companies WHERE nome LIKE '%{}%' OR email LIKE '%{}%' 
                OR telefone1 LIKE '%{}%' OR telefone2 LIKE '%{}%' 
                ORDER BY nome ASC LIMIT 20""".format(search_word,search_word,search_word,search_word)
                cursor.execute(query)   
                numrows = int(cursor.rowcount)
                response = cursor.fetchall()
                print(numrows)
                return jsonify({'htmlcompanyresponse': render_template('/store/company/company_response.html', response=response, numrows=numrows)})
    except Exception as error:
        print(error)        
    return render_template('/store/company/company_response.html')


@app.route('/company_edit/<string:id>')
def company_edit(id):
    title = 'Company Edit'
    form = ModelFormPeople()
    try:
        if session['amail'] != '' and session['companies'] == 1:
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM companies WHERE id = %s'
            cursor.execute(query,[id])
            response = cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count != 0:
                return render_template('/store/company/company_edit.html', response=response, title=title, form=form)
        elif session['amail'] != '' and session['companies'] == 0:
            flash('Dont Have Access To This functionality...!!!!', 'danger')
            return render_template('/layout/store.html', title='Store')
    except Exception as error:
        print(error)
    return render_template('/pages/home.html', title='Home')


@app.route('/update_company', methods=['GET','POST'])
def update_company():
    CompanyUpdate()
    return redirect(url_for('company_list'))