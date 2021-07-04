from selenium import webdriver
import time
import random
import csv
print("Nombre de lista?")
nombre = input()
nombre = nombre+'.csv'
print("Url de la lista")
url = input()
diccionario = {
    }
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get(url)
altura = driver.execute_script("return document.body.scrollHeight")
count = 0
while altura > 100:
  driver.execute_script("window.scrollBy(0,"+str(count)+");")
  time.sleep(1)
  count += 500
  altura -= 500
print('Something Else')
definition = driver.find_elements_by_class_name('SetPageTerm-definitionText')
words = driver.find_elements_by_class_name('SetPageTerm-wordText')
for i,j in zip(definition,words):
 diccionario[j.text] = i.text

with open(nombre, 'w') as new_file:
   field_names = ['word', 'definition']
   csv_writer = csv.DictWriter(new_file, fieldnames = field_names, delimiter='¿' )
   csv_writer.writeheader()
   for key in diccionario.keys():
      new_file.write(("%s¿%s\n"%(key,diccionario[key])))


driver.close()

