import smtplib

smtObj=smtplib.SMTP('smtp.gmail.com',587)
smtObj.ehlo()
smtObj.startls()
smtObj.login('emailid', 'password')
smtObj.sendmail("sendermail","sendermail","subject")
smtObj.quit()