from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.add_argument("--headless")

assert options.headless

browser = Chrome(options=options)
browser.get('https://bandcamp.com')
browser.find_element_by_class_name('playbutton').click()

tracks = browser.find_elements_by_class_name('discover-item')
len(tracks)
tracks[3].click()
