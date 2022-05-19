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


@app.route("/companyrecords",methods=["POST","GET"])
def companyrecords():
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        query = request.form['query']
        if query == '':
            cursor.execute("SELECT * FROM companies ORDER BY nome ASC")
            responselist = cursor.fetchall()
        else:
            search_text = request.form['query']
            print(search_text)
            cursor.execute("SELECT * FROM companies ORDER BY nome ASC", [search_text])
            responselist = cursor.fetchall()  
    return jsonify({'htmlresponse': render_template('/store/company/company_response.html', responselist=responselist)})


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


@app.route('/delete_companies/<string:id>', methods = ['GET', 'POST'])
def delete_companies(id):
    try:
        if session['amail'] != '' and session['companies'] == 1:
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM companies'
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 1:
                flash('Last Company Cant Be Deleted...!!!!', 'danger')
            else:
                cursor = mysql.connection.cursor()
                cursor.execute('DELETE FROM companies WHERE id = %s', [id])
                mysql.connection.commit()
                flash('Company Deleted Successfully...!!!', 'success')
        elif session['amail'] != '' and session['companies'] == 0:
            flash('Dont Have Access To This functionality...!!!!', 'danger')
            return render_template('/layout/store.html', title = 'Store')
    except Exception as e:
        print(e)
    return redirect(url_for('company_list'))