from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("--start-maximized")
# options.add_argument(r"print-to-pdf='D:\Programming\Work_Projects\ad_lib.pdf'")

driver=webdriver.Chrome("../../Drivers/chromedriver.exe", options=options)
driver.implicitly_wait(10)


driver.get("https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=BG&view_all_page_id=195756373912776&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=page&media_type=all")
button = driver.find_element_by_css_selector("button[data-testid='cookie-policy-dialog-accept-button']")
button.click()
time.sleep(4)
get_body = driver.find_element_by_tag_name('body')

text = get_body.text
print ("0 резултата" in text)
print(text)

get_body.send_keys(Keys.END)
time.sleep(2)
get_body.send_keys(Keys.END)
time.sleep(2)
get_body.send_keys(Keys.END)
driver.set_window_size(1920,1080)
size = get_body.size


# driver.get("https://www.mc-sanamedic.com/")
# func = lambda x: driver.execute_script("return document.body.parentNode.scroll"+x)
driver.set_window_size(size["width"],size["height"])
# driver.get_screenshot_as_file('test.png')
# driver.get("https://www.mc-sanamedic.com/")
# ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()
# driver.get_screenshot_as_file()
# print(driver.title)
# button.click()
# element = driver.find_element_by_tag_name("body")
# element.page_screenshots("body.png")
print(driver.get_window_size())
driver.close()