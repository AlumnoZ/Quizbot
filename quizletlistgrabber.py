from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random
import csv
print("Nombre de lista?")
nombre = input()
nombre = nombre+'.csv'
print("Url de la lista")
url = input()
print("User:")
user = input();
print("Pass:")
password = input();
diccionario = {
    }
PATH = 'C:\Program Files (x86)\chromedriver.exe'

def SignIn(user, password):
    driver.get('https://quizlet.com/es')
    Signin_button = driver.find_element_by_xpath('//*[@id="TopNavigationReactTarget"]/header/div/div[2]/div[3]/button[1]')
    Signin_button.click()
    user_blank = driver.find_element_by_id('username')
    pass_blank = driver.find_element_by_id('password')
    user_blank.send_keys(user)
    pass_blank.send_keys(password)
    pass_blank.send_keys(Keys.ENTER)
    time.sleep(3)

driver = webdriver.Chrome(PATH)
SignIn(user, password)

driver.get(url)
driver.implicitly_wait(2)
try:
    cerrar = driver.find_element_by_xpath("/html/body/div[9]/div/div[1]/div/button")
    cerrar.click()
except NoSuchElementException:
        try:
            cerrar2 = driver.find_element_by_xpath("/html/body/div[12]/div/div/div[1]")
            cerrar2.click()
        except NoSuchElementException:
            print("Nothing to close")
    print("Nothing to close")
altura = driver.execute_script("return document.body.scrollHeight")
count = 0
while altura > 100:
  driver.execute_script("window.scrollBy(0,"+str(count)+");")
  time.sleep(1)
  count += 500
  altura -= 500
definition = driver.find_elements_by_class_name('SetPageTerm-definitionText')
words = driver.find_elements_by_class_name('SetPageTerm-wordText')
for i,j in zip(definition,words):
 diccionario[j.text] = i.text

with open("Lists/"+nombre, 'w') as new_file:
   field_names = ['word', 'definition']
   csv_writer = csv.DictWriter(new_file, fieldnames = field_names, delimiter='¿' )
   csv_writer.writeheader()
   for key in diccionario.keys():
      new_file.write(("%s¿%s\n"%(key,diccionario[key])))


driver.close()

