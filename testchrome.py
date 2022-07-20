from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.add_argument("--headless")

assert options.headless

browser = Chrome(options=options)
browser.get('https://duckduckgo.com')

search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('bitrix24')
search_form.submit()

results = browser.find_elements_by_class_name('result')
print(results[0].text)
