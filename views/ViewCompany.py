from models.ModelCompany import *

self = 'self'


@app.route('/company_list')
def company_list():
    title = 'View Companies'
    try:
        if session['amail'] != '' and session['companies'] == 1:
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM companies'
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Company Not Found...!!!!', 'danger')
            return render_template('/store/company/company_list.html', response = data, title = title)
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


@app.route("/company_search", methods = ["POST","GET"])
def company_search():
    try:
        cursor = mysql.connection.cursor()
        if request.method == 'POST':
            search_word = request.form['query']
            print(search_word)
            if search_word != '':
                query = "SELECT * from companies WHERE nome LIKE '%{}%' OR email LIKE '%{}%' OR telefone1 LIKE '%{}%' ORDER BY nome ASC LIMIT 20".format(search_word,search_word,search_word)
                cursor.execute(query)   
                numrows = int(cursor.rowcount)
                data = cursor.fetchall()
                print(numrows)
                return jsonify({'htmlcompanyresponse': render_template('/store/company/company_response.html', response = data, numrows = numrows)})
    except Exception as e:
        print(e)        
    return render_template('/store/company/company_response.html')


@app.route('/company_register', methods = ['GET', 'POST'])
def company_register():
    title = 'Company Register'
    ModelCompany.CompanyRegister(self)
    try:
        if session['amail'] != '' and session['companies'] == 1:
            return render_template('/store/company/company_register.html', title = title)
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title = 'Home')


