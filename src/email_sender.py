import smtplib
from email.mime.text import MIMEText


def send_email(secret_santa, debug):
    sender_email = creds.sender_email
    receiver_email = secret_santa['Gifter']['Email']
    password = creds.password
    message = MIMEMultipart("alternative")
    message["Subject"] = "Your Secret Santa has Arrived!"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f"""
    Hello {secret_santa['Gifter']['Name']},
    You are shopping for {secret_santa['Giftee']['Name']}.
    There requested gists are
    1. {secret_santa['Giftee']['Gifts'][0]}
    2. {secret_santa['Giftee']['Gifts'][1]}
    3. {secret_santa['Giftee']['Gifts'][2]}
    Please let me know if you have any questions.
    Love, Jack
    """

    html = f"""\
    <html>
        <body>
            <p> Hello {secret_santa['Gifter']['Name']},<br>
                You are shopping for {secret_santa['Giftee']['Name']}.<br>
                There requested gifts are<br><br>
                1. <a href={secret_santa['Giftee']['Gifts'][0]}>{secret_santa['Giftee']['Gifts'][0]}</a><br>
                2. <a href={secret_santa['Giftee']['Gifts'][1]}>{secret_santa['Giftee']['Gifts'][1]}</a><br> 
                3. <a href={secret_santa['Giftee']['Gifts'][2]}>{secret_santa['Giftee']['Gifts'][2]}</a><br> 
                <br>
                Please let me know if you have any questions.<br>
                Love, Jack
            </p>
        </body>
    </html>
    """
    print(f"Sending email to {secret_santa['Gifter']['Name']} -> {message['To']}")
    if not debug:
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
    else:
        print(text)

