import smtplib
from langchain.tools import tool


class SendMail:
    @tool("create mail")
    def send_mail(data):
        """
        Useful to create an email.
        the input should be a entire string
        The input to this tool should be a pipe (|) separated text
        of length 3 (three), representing who to send the email to,
        the subject of the email and the actual message.
        For example, `lorem@ipsum.com|Nice To Meet You|Hey it was great to meet you.`.
        """
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