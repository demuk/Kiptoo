import os
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Message, Mail
import uuid


app = Flask(__name__)


# app.config.update(DEBUG=True, MAIL_SERVER='smtp.gmail.com',
#                   MAIL_PORT=587, MAIL_USE_SSL=False, MAIL_USE_TLS=True, MAIL_USERNAME='kdennsmutai@gmail.com',
#                   MAIL_PASSWORD="KIPTOODENNIS123")
# mail = Mail(app)
#
# app.config['MAIL_SERVER']='smtp.mailtrap.io'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'a01094e891d635'
# app.config['MAIL_PASSWORD'] = '86c28bc9a8074e'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False

app.config['SECRET_KEY'] = 'top-secret!'
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = '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'
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
mail = Mail(app)




@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html',id=uuid.uuid4())


@app.route('/policy')
def policy():
    return render_template('policy.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/kapsuchai')
def kapsuchai():
    return render_template('kapsuchai.html')

@app.route('/pointofsale')
def pointofsale():
    return render_template('pointofsale.html')


@app.route('/darthorama')
def darthorama():
    return render_template('darthorama.html')

@app.route('/bookorama')
def bookorama():
    return render_template('bookorama.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        sender = 'denysmutay@gmail.com'
        recipients = ['denysmutay@gmail.com']
        msg = Message(body=f"Name: {name}\n EMail: {email}\n Subject:{subject}\n Message:{message}",
                      recipients=recipients, sender=sender)
        mail.send(msg)
        return redirect(url_for('thankyou'))
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
