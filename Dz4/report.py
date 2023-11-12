import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import yaml
import os

def send_email(subject, body, attachment_path=None):
    with open("testdata.yaml") as f:
        testdata = yaml.safe_load(f)

    fromaddr = testdata.get("report_mail")
    toaddr = testdata.get("report_mail")
    api_key = testdata.get("report_passwd")

    msg = MIMEMultipart()
    msg['from'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))


    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, 'rb') as attachment:
            part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            msg.attach(part)

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.ehlo()
    server.login(fromaddr, api_key)

    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()




