from email.message import EmailMessage
from smtplib import SMTP_SSL
import ssl




class EmailSender:

    user = "Xplora.mailbot@gmail.com"
    password = "Xplora16!"
    default_body = "Hey, Marketing Ninja. " \
                   "It's me the X_Bot and I'm sending you the" \
                   " requested ScreenCapture file. Enjoy!"

    def build_mail(self,recipient,attachment,body=default_body):
        self.message = EmailMessage()
        self.message["From"] = self.user
        self.message["To"] = recipient
        self.message['Subject'] = "Competitors Analysis"
        self.message.set_content(body)
        self._attach_file(attachment)

    def send_mail(self):
        context = ssl.create_default_context()
        mail_server = SMTP_SSL('smtp.gmail.com',465,context=context)
        mail_server.login(self.user,self.password)
        mail_server.send_message(self.message)
        mail_server.quit()



    def _attach_file(self,attachment):
        with open(attachment,"rb") as file:
            self.message.add_attachment(file.read(),
                                        maintype="application",
                                        subtype="pdf",
                                        filename="Competitor_Analysis")


if __name__ == "__main__":
    email_sender=EmailSender()
    email_sender.build_mail(recipient="mussashi50@gmail.com",
                            attachment="D:\Programming\Work_Projects\ScreenShotApp(new)\Project\Ad_library_screens\screenshots_09_10\Ads_Preview_09_10.pdf",
                             )
    email_sender.send_mail()

