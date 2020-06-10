from selenium.webdriver import Firefox
from time import sleep
browser = Firefox()
url = 'https://selenium.dunossauro.live/aula_04.html'
browser.get(url)
sleep(5)
a = browser.find_element_by_tag_name('a')

browser.quit()
