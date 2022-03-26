from email.message import EmailMessage
from smtplib import SMTP_SSL
import ssl, os 
from dotenv import load_dotenv

load_dotenv()




class EmailSender:
    """
    This class is used for attaching the screenshots of the pages and sending them to an email
    """

    user = os.environ["email"]
    password = os.environ["pass"]
    default_body = "Hey, Marketing Ninja. " \
                   "It's me the X_Bot and I'm sending you the" \
                   " requested ScreenCapture file. Enjoy!"

    # First we construct the mail and then we send it
    @classmethod
    def build_mail(cls, recipient, attachment, body=default_body):
        cls.message = EmailMessage()
        cls.message["From"] = cls.user
        cls.message["To"] = recipient
        cls.message['Subject'] = "Competitors Analysis"
        cls.message.set_content(body)
        cls._attach_file(attachment)

    @classmethod
    def send_mail(cls):
        context = ssl.create_default_context()
        mail_server = SMTP_SSL('smtp.gmail.com',465,context=context)
        mail_server.login(cls.user, cls.password)
        mail_server.send_message(cls.message)
        mail_server.quit()

    # Private method used only by the build_mail method for attaching of a file
    @classmethod
    def _attach_file(cls, attachment):
        with open(attachment,"rb") as file:
            cls.message.add_attachment(file.read(),
                                       maintype="application",
                                       subtype="pdf",
                                       filename="Competitor_Analysis")


if __name__ == "__main__":

    # Used for testing during development

    email_sender=EmailSender
    email_sender.build_mail(recipient="email",
                            attachment="Ads_Preview_10_10.pdf",
                             )
    email_sender.send_mail()

