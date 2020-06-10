from selenium.webdriver import Firefox
from time import sleep
browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser.get(url)
sleep(5)
para=False
a = browser.find_element_by_tag_name('a')
while para == False:
    a.click()
    ps = browser.find_elements_by_tag_name('p')
    for ii in range(len(ps)):
        if 'ganhou' in ps[ii].text:
            para = True
            break
print('acabou')
#browser.quit()
