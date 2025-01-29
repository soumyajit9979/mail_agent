import smtplib
from langchain.tools import tool
import json

class SendMail:
    @tool("create mail")
    def send_mail(data):
        """
        the input of the function should be a entire string format and no json format or dict format
        The input to this tool should be a pipe (|) separated text
        of length 3 (three), representing who to send the email to,
        the subject of the email and the actual message.
        For example, `lorem@ipsum.com|Nice To Meet You|Hey it was great to meet you.`.
        """
        print("------------------------------------------------------------------_!@_#!+@)#(+!@)#(@!+#)")
        print(data)
        email="soumyajit94298@gmail.com"
        reciever, subject, message = data.split("|")
        print("will sennd")

        text=f"Subject : {subject}\n\n{message}"

        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()

        server.login(email, "pplp bxss wgbw byft")

        server.sendmail(email,reciever,text)

        print("email has been sent to "+reciever)
        return "mail sent"

# SendMail.send_mail("{\"data\": \"principal@hbkschool.com|Introduction|Hello, I am the principal of HBK School.\"}")