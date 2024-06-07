## This python script uses ping to test if a server is live. If the server is not reachable an email is sent via Office 365 SMTP

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#################################################################################################
message_to = ""
server_account = ""
server_password = ''
servernames = 'j:/scripts/serverlist.txt'  ## populate text file with server name on each line
#################################################################################################

with open(servernames,'r') as file:
    servers = file.readlines()

for server in servers:
    respond = os.system("ping -n 1 " + server + " > nul")
    if respond == 1:
        msg = MIMEMultipart()
        msg["Subject"] = server + " is down"
        msg["From"] = server_account
        msg["To"] = message_to
        body = MIMEText(server + " is down")
        msg.attach(body)
        smtp = smtplib.SMTP('smtp.office365.com',587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(server_account, server_password)
        smtp.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
        smtp.quit()
