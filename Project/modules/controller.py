from Project.modules.web_driver import AdLibCapture,BuildWebDriver
from Project.modules.to_pdf import PdfBuilder
from Project.model.model import Model
from Project.modules.email_sender import EmailSender


# Storing the retrieved pages from database in a set (contains only unique values)
# It gets cleared after every new retrieval#
page_queue=set()


class CaptureBot():
    """
     This is a higher level class for managing all the functionality in the app, made available trough all the different
     modules in the modules folder:
     - different types of screen capturing(by page, keyword, database etc.)
     - executing CRUD operations on the DB

    """

    driver = BuildWebDriver()

    @classmethod
    def capture_pages(self,pages,country="ALL",scrolls=3):
        driver=self.driver.build_driver()
        ad_bot=AdLibCapture(driver)
        res = ad_bot.capture_bulk_pages(pages_list=pages,
                                  country="ALL",
                                  scrolls=scrolls)
        return res

    @classmethod
    def capture_keyword(self,keyword,country="BG",scrolls=3):
        driver = self.driver.build_driver()
        ad_bot = AdLibCapture(driver,type=keyword)
        res = ad_bot.capture_by_keyword(keyword=keyword,
                                        country=country,
                                        scrolls=scrolls
                                        )
        return res

    @classmethod
    def capture_from_database(self,scrolls=3,country="ALL"):
        all_pages = Model.get_all()
        data_size = len(all_pages)
        batch_size = 5
        status = ""
        # When making screenshots of all pages from DB in bulk, they are being split into batches of 5
        # The main reason is to reduce the probability of the browser getting overloaded and crashing
        # This way it restart every 5 iterations, so theoretically it can process unlimited number of pages#
        for batch in range(0, data_size, batch_size):
            pages_list = all_pages[batch:batch+batch_size]
            driver = self.driver.build_driver()
            ad_bot = AdLibCapture(driver)
            res = ad_bot.capture_all_pages(scrolls=scrolls,
                                           country=country,
                                           pages_list=pages_list)
            status += res
            print(f"Batch from {batch} to {batch+batch_size} ready")
        return status

    @classmethod
    def insert_user_to_db(cls,email,email_body):
        try:
            Model.insert_user(email=email,
                              email_body=email_body)
            return "Profile Added"
        except:
            return "DB Error"

    @classmethod
    def insert_page_to_db(cls,page_id,page_name):
        try:
            Model.insert_page(id=page_id,
                              name=page_name)
            return f"Page / {page_name} / added"
        except:
            return f"Page already in the DataBase"

    @classmethod
    def find_page(cls,page_name):
        res = Model.get_page(name=page_name)
        return res

    @classmethod
    def delete_page(cls,page_id):
        Model.delete_page(id=page_id)
        return "Page removed"

    @classmethod
    def delete_all_pages(cls):
        Model.delete_all()
        return "All Pages Removed"

    @staticmethod
    def to_pdf(default=True,quality=90,specify_folder=None):
        res = PdfBuilder.convert_to_pdf(default=default,
                                        quality=quality,
                                        specify_folder=specify_folder)
        return res

    @classmethod
    def send_email(cls,file):
        user = Model.get_user()
        email_sender = EmailSender
        email_sender.build_mail(recipient=user[1],
                                attachment=file,
                                body=user[2])
        email_sender.send_mail()




if __name__ == "__main__":

    # USED FOR TESTING DURING DEVELOPMENT

    # res=Model.get_all()
    # res = [page[1:] for page in res ]
    # res_2 = [("SanaMedic", 312617136169551),("Sofia Opera",195756373912776),("Sport Vision",181039705377403)]
    # res_3 = [("Sofia Opera", 195756373912776)]
    CaptureBot.capture_from_database()
    # CaptureBot.capture_keyword("Гуми")
    CaptureBot.to_pdf(quality=95)