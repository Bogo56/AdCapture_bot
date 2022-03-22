from selenium import webdriver
from Project.modules.dir_maker import create_dir
from selenium.webdriver.common.keys import Keys
from Project.model.model import Model
import time,datetime
import random,re
import urllib
from pathlib import Path


'''
This module contains the classes for navigating chrome browser in headless mode and creating screenshots of the desired
pages. It is based on the selenium framework. It supports different types of capturing:  by page id / by keyword
'''

# These are core assets needed (url, file and driver locations) for the classes to function

today = datetime.datetime.today().strftime("%d_%m")
fb_url = "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country={}" \
       "&view_all_page_id={}&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped" \
       "&search_type=page&media_type=all"
keyword_url = "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country={}" \
              "&q={}&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered" \
              "&media_type=all"
screen_dir = create_dir()
condition = "\s0 резултата"
driver_loc = Path.cwd().parent.parent.joinpath("Drivers","chromedriver.exe")


class BuildWebDriver:

    """
    This time we're using the class with standard instance methods. Because the class can be instantiated
    with different browser options. And It needs to be instantiated anew every time we're creating a new batch
    of pages to be captured in the current session of the browser - e.g in the current instance of the driver class.
    """

    default_driver = driver_loc

    def __init__(self,headless=True):
        self._options = webdriver.ChromeOptions()
        if headless:
            self._options.add_argument("headless")
            self._options.add_argument("disable-gpu")

    # adding additional options to the instance if needed
    def add_options(self,*args):
        if args:
            for arg in args:
                self._options.add_argument(arg)

    # Creating the driver (chrome session) to be used for screenshots
    def build_driver(self, webdriver_dir=default_driver):
        cur_driver=webdriver.Chrome(executable_path=webdriver_dir,
                                    options=self._options)
        cur_driver.implicitly_wait(15)

        return cur_driver



class AdLibCapture:

    def __init__(self, driver, type="page"):
        self._driver = driver
        if type != "page":
            self.base_url = keyword_url
        else:
            self.base_url = fb_url

    # This method takes care of starting the chrome session(headless/normal) using the driver from the
    # previous class, navigate to the facebook pages and take screenshots of their ads
    # It uses randomized time intervals between each interaction with the web page to mimic human behaviour and
    # avoid blocking from FB servers
    # Private method used internally by the other methods in this class
    def _construct_capture_flow(self, page_name=None, page_id=None, scrolls=3, policy=True, country="ALL", keyword="marketing"):
        if page_id:
            entity = page_name
            final_url = self.base_url.format(country,page_id)
            filename = f"{screen_dir}\{today}_apage_{entity}.png"
        else:
            entity = keyword
            final_url = self.base_url.format(country, keyword)
            entity = urllib.parse.unquote(entity)
            filename = f"{screen_dir}\{today}_key_{entity}.png"
        self._driver.get(final_url)

        # Clicking the privacy policy button to allow page scrolling
        if policy:
            button=self._driver.find_element_by_css_selector("button[data-testid='cookie-policy-manage-dialog-accept-button']")
            button.click()
        # Randomizing time between actions to mimic human behaviour
        time.sleep(random.randint(4,6))
        get_body = self._driver.find_element_by_tag_name('body')
        text_in_body = get_body.text

        # Regular Expression pattern for defining if a page has any ads running at the moment
        if re.search(condition, text_in_body):
            print(f"No Ads Found For /{entity}/")
            return f"No Ads Found For /{entity}/ \n"

        for n in range(scrolls):
            get_body.send_keys(Keys.END)
            time.sleep(random.randint(1,3))
        self._driver.set_window_size(1920,1080)
        size = get_body.size
        self._driver.set_window_size(size["width"], size["height"])
        self._driver.get_screenshot_as_file(filename)
        return f"Screenshot for/ {entity} / captured \n"

    def capture_page(self, page_id, page_name, scrolls=3, country="ALL"):
        self._construct_capture_flow(page_id=page_id,
                                     page_name=page_name,
                                     scrolls=scrolls,
                                     policy=True,
                                     country=country)
        self._driver.close()

    def capture_all_pages(self, pages_list, scrolls=3, country="ALL"):
        pages = pages_list
        status = ""
        res = self._construct_capture_flow(page_id=pages[0][2],
                                           page_name=pages[0][1],
                                           scrolls=scrolls,
                                           policy=True,
                                           country=country)
        status += res

        for page in pages[1:]:
            res = self._construct_capture_flow(page_id=page[2],
                                               page_name=page[1],
                                               scrolls=scrolls,
                                               policy=False,
                                               country=country)
            status += res
        self._driver.close()
        return status

    def capture_bulk_pages(self,pages_list,country="ALL",scrolls=3):
        status = ""
        res = self._construct_capture_flow(page_id=pages_list[0][1],
                                           page_name=pages_list[0][0],
                                           scrolls=scrolls,
                                           policy=True,
                                           country=country)
        status += res

        for page in pages_list[1:]:
            time.sleep(random.randint(1,3))
            res = self._construct_capture_flow(page_id=page[1],
                                               page_name=page[0],
                                               scrolls=scrolls,
                                               policy=False,
                                               country=country)
            status += res
        self._driver.close()
        return status

    def capture_by_keyword(self, keyword, country="BG",scrolls=3):
        keyword = urllib.parse.quote(keyword)
        res = self._construct_capture_flow(keyword=keyword,
                                           country=country,
                                           scrolls=scrolls)
        self._driver.close()
        return res


if __name__ == "__main__":

    # Used fot testing in Development

    # driver=BuildWebDriver().build_driver()
    # page_bot=AdLibCapture(driver)
    #
    # ## Bulk Capture
    # pages=[(0,3859501477945,"Kaufland"),(1,312617136169551,"SanaMedic"),(2,24078343402632998,"GoSport"),(3,11839230704429977,'Dev.bg'),(4,475170749544771,"Body_Aesthetics"),(5,513523225491395,"Viessman")]
    # page_bot.capture_bulk_pages(pages)

    ## Capture By Keyword
    driver = BuildWebDriver()
    ready_driver = driver.build_driver()
    keyword_bot = AdLibCapture(ready_driver,type="keyword")
    keyword_bot.capture_by_keyword(keyword="Technology",scrolls=7)