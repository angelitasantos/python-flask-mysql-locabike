from models.ModelMail import *


@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    title = 'Formulário de Contato'
    try:
        if request.method == 'POST':
            nome = request.form['name']
            email = request.form['mail']
            subject = request.form['subject']
            msg = request.form['message']

            message = Message(subject, sender = app.config.get('MAIL_USERNAME'), recipients = [email])
            message.body = msg
            mail.send(message)

            flash('Contact Sent Successfully', 'success')
            return render_template('/pages/home.html', title = title)
    except:
        flash('Contact Dont Sent', 'danger')
        pass
    return render_template('/pages/home.html')
