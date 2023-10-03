import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "kit.23.19bec068@gmail.com"
    password = "jvxv luoy clkl vefv"

    receiver = "arsacharis@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)