import smtplib, ssl

class sm:
    sender = "senderemail@gmail.com"
    receiver = "sumitpatidarec18@acropolis.in"
    password = "9713126944"
    message = "hey"
    def send_mail(self, msg):
        context = ssl.create_default_context()
        port = 465
        with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as smtObj:
            smtObj.login(self.sender, self.password)
            smtObj.sendmail(self.sender, self.receiver, msg)
        

