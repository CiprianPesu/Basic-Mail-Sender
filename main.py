#pip3 install pandas openpyxl
import pandas

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib , ssl

import json

print("Starting")

f = open('conf.json')
conf = json.load(f)

print("Loading Config")

context = ssl.create_default_context()
smtp = smtplib.SMTP(conf["SMTP"], conf["SMTPport"])
smtp.connect(conf["SMTP"], conf["SMTPport"])
smtp.ehlo()
smtp.login(conf["LoginEmail"], conf["LoginPass"])

subject= conf["Subject"]

with open(conf["TextFile"]) as f:
    contents = f.read()

df = pandas.read_excel('Emailuri.xlsx')

count=0
for i in range(df.shape[0]):
    try:
        numar=str(df.iloc[i]["Numar"])
        email=str(df.iloc[i]["Email"])

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = conf["LoginEmail"]
        msg['To'] = email

        msg.attach(MIMEText(contents.replace("{NUMAR}",numar)))

        smtp.sendmail(from_addr=conf["LoginEmail"],
                    to_addrs=email, msg=msg.as_string())

        print("Trimis la : ", email)
        count+=1

        if(count==15):
            print("Reset")
            count=0
            smtp.quit()
            smtp = smtplib.SMTP(conf["SMTP"], conf["SMTPport"])
            smtp.connect(conf["SMTP"], conf["SMTPport"])
            smtp.ehlo()
            smtp.login(conf["LoginEmail"], conf["LoginPass"])

    except Exception as e:
        print("Eroare la randul :",i,"Email: ",email)
        print(e)
    
print("Finalized")
smtp.quit()