from selenium.webdriver import Firefox
from time import sleep
browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser.get(url)
sleep(5)
h1 = browser.find_element_by_tag_name('h1')
dicionario = {}
dicionario['H1']={}
ps = browser.find_elements_by_tag_name('p')
for ii in range(len(ps)):
    dicionario['H1'].update({ps[ii].get_attribute('atributo') : ps[ii].text})
print(dicionario)
browser.quit()
