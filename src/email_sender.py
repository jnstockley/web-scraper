import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import StringIO

import toml
from pandas import DataFrame


def read_config(path: str = '../config.toml'):
    return toml.load(path)


def send_email(new_cars: DataFrame):
    config = read_config()
    sender_email = config['sender_email']
    receiver_email = config['receiver_email']
    password = config['password']
    smtp_server = config['smtp_server']
    smtp_port = config['smtp_port']

    message = MIMEMultipart('related')
    message["Subject"] = "New Car Listings!"
    message["From"] = sender_email
    message["To"] = receiver_email

    csv_buf = StringIO()

    new_cars.to_csv(csv_buf, index=False)

    html_part = MIMEMultipart('related')

    html = f"""
    <html>
        <body>
            {new_cars.to_html()}
        </body>
    </html>"""

    html_part.attach(MIMEText(html, 'html'))
    message.attach(html_part)

    attach_part = MIMEMultipart('mixed')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(csv_buf.getvalue())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename='new_cars.csv')
    attach_part.attach(part)
    message.attach(attach_part)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
