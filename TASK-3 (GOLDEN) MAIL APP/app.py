from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'personal'

mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'pythontut23@gmail.com'
# use the app password created
app.config['MAIL_PASSWORD'] = os.environ.get("PYTHON_EMAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail.init_app(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        email = request.form.get("email")
        rec_email = request.form.get("rec-email")
        subject = request.form.get("subject")
        message_body = request.form.get("message")

        # Constructing the message body
        body = f"From: {email}\nTo: {rec_email}\nSubject: {subject}\n\n{message_body}"

        msg = Message(
            subject=subject,
            body=body,
            sender=email,
            recipients=[rec_email]
        )
        try:
            mail.send(msg)
            flash("Message Sent ..!", 'success')
        except Exception as e:
            flash(f"Some error happened: {str(e)}", "danger")

        # Redirect back to the same page after processing the form
        return redirect(url_for('home'))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
