from selenium.webdriver import Firefox
from time import sleep
browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/aula_03.html'
browser.get(url)
sleep(5)
a = browser.find_element_by_tag_name('a')

a.click()
for click in range(10):
    ps = browser.find_elements_by_tag_name('p')
    a.click()
    print(f'Valor do ultimo p: {ps[-1].text}. Valor do click: {click}')
print(f'texto de a: {a.text}')

browser.quit()
