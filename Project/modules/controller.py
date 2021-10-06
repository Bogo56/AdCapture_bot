from Project.modules.web_driver import AdLibCapture,BuildWebDriver
from Project.modules.to_pdf import PdfBuilder

##
# - Capture by Page - redundant
# - Capture all Pages in DB
# - Capture Bulk Pages
# - Capture by Keyword##


page_queue=set()

class CaptureBot():

    driver = BuildWebDriver()

    def capture_pages(self,pages,country="ALL",scrolls=3):
        driver=self.driver.build_driver()
        ad_bot=AdLibCapture(driver)
        res = ad_bot.capture_bulk_pages(pages_list=pages,
                                  country="ALL",
                                  scrolls=scrolls)
        return res

    def capture_keyword(self,keyword,country="BG",scrolls=3):
        driver = self.driver.build_driver()
        ad_bot = AdLibCapture(driver,type=keyword)
        res = ad_bot.capture_by_keyword(keyword=keyword,
                                  country=country,
                                  scrolls=scrolls
                                  )
        return res

    def capture_from_database(self,scrolls=3,country="ALL"):
        driver = self.driver.build_driver()
        ad_bot = AdLibCapture(driver)
        res= ad_bot.capture_all_pages(scrolls=scrolls
                                      ,country=country)
        return res

    @staticmethod
    def to_pdf(default=True,quality=90,specify_folder=None):
        res = PdfBuilder.convert_to_pdf(default=default,
                                  quality=quality,
                                  specify_folder=specify_folder)
        return res

if __name__ == "__main__":

    # res=Model.get_all()
    # res = [page[1:] for page in res ]
    # res_2 = [("SanaMedic", 312617136169551),("Sofia Opera",195756373912776),("Sport Vision",181039705377403)]
    # res_3 = [("Sofia Opera", 195756373912776)]
    CaptureBot().capture_from_database()
    # CaptureBot().capture_keyword("Гуми")
    CaptureBot.to_pdf(quality=95)