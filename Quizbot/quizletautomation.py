from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import csv
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
actions = ActionChains(driver)
maxcount = 0

        
def SignIn(user, password, num):
    global maxcount
    with open('Lists/'+num+'.csv', 'r') as lista:
            csv_dict_reader = csv.DictReader(lista, delimiter='¿')
            for row in csv_dict_reader:
                maxcount += 1 
    driver.get('https://quizlet.com/es')
    Signin_button = driver.find_element_by_xpath('//*[@id="TopNavigationReactTarget"]/header/div/div[2]/div[3]/button[1]')
    Signin_button.click()
    user_blank = driver.find_element_by_id('username')
    pass_blank = driver.find_element_by_id('password')
    user_blank.send_keys(user)
    pass_blank.send_keys(password)
    pass_blank.send_keys(Keys.ENTER)
    time.sleep(3)
def SolveWrite(url,nombreL):
    count = 0
    driver.get(url)
    palabra=""
    time.sleep(2)
    while count < maxcount:
        with open('Lists/'+nombreL+'.csv', 'r') as lista:
            csv_dict_reader = csv.DictReader(lista, delimiter='¿')
            definition = driver.find_element_by_class_name('WriteQuestionElements')
            for row in csv_dict_reader:
                if row['definition'] == definition.text:
                    palabra = row['word']

            inputElement = driver.find_element_by_class_name('AutoExpandTextarea-textarea')
            inputElement.send_keys(palabra)
            time.sleep(.5)
            inputElement.send_keys(Keys.ENTER)  
            time.sleep(.5)
        count += 1
    driver.close()
def solvewrite(nombreL):
    with open('Lists/'+nombreL+'.csv', 'r') as lista:
            driver.implicitly_wait(3)
            csv_dict_reader = csv.DictReader(lista, delimiter='¿')
            try:
                definition = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div')
            except NoSuchElementException:
                button = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/div/div/div/div[2]/div/button')
                button.click()
                time.sleep(1.5)
            definition = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div')
            for row in csv_dict_reader:
                if row['definition'] == definition.text:
                    palabra = row['word']
                
            inputElement = driver.find_element_by_class_name('AutoExpandTextarea-textarea')
            inputElement.send_keys(palabra)
            time.sleep(.5)
            inputElement.send_keys(Keys.ENTER)  
            time.sleep(.5)
       

def solvemultiple(nombreL):
    driver.implicitly_wait(5)
    with open('Lists/'+nombreL+'.csv', 'r') as lista:
            csv_dict_reader = csv.DictReader(lista, delimiter='¿')
            try:
                option1 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[1]')
                option2 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[2]')
                option3 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[3]')
                option4 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[4]')
            except NoSuchElementException:
                driver.implicitly_wait(10)
                option1 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[2]/div/div[1]')
                option2 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[2]/div/div[2]')
                option3 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[2]/div/div[3]')
                option4 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[2]/div/div[4]')
            try:
                definition = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[1]/div[2]/div/div/div')
            except NoSuchElementException:
                definition = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div')
            time.sleep(1)
            for row in csv_dict_reader:
                if row['definition'] == definition.text:
                    palabra = row['word']
            print('Correcta:'+palabra)
            if  palabra in option1.text :
                option1.click()
            if  palabra in option2.text:
                option2.click()
            if  palabra in option3.text:
                option3.click()
            if  palabra in option4.text:
                option4.click()
            time.sleep(2)
def SolveLearn(url,nombreL):
    count = 0
    palabra = ""
    driver.get(url)
    time.sleep(3)
    try:
        Continuar = driver.find_element_by_class_name('OnboardingView-gotItButton')
    except NoSuchElementException:
        Continuar = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/button')
    Continuar.click()      
    while count < maxcount*2:
        try:
            try:
                solvemultiple(nombreL)
            except NoSuchElementException:
                solvewrite(nombreL)
        except NoSuchElementException:
            try:
                boton = driver.find_element_by_class_name('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/div/div/div/button')
            except:
                boton = driver.find_element_by_class_name('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/div/div/div/div[2]/div/button')
            boton.click()
    print('Solved!')
    driver.close()
def SolveSpell(url,nombreL):
    count = 0
    driver.get(url)
    palabra=""
    time.sleep(2)
    while count < maxcount*2:
        
        with open('Lists/'+nombreL+'.csv', 'r') as lista:
            csv_dict_reader = csv.DictReader(lista, delimiter='¿')
            time.sleep(2)
            try:
                definition = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div/div[2]/div/div/div[2]/div')
            except NoSuchElementException:
                button = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div/div[2]/div/div/div[1]/div/button')
                button.click()
            for row in csv_dict_reader:
                if row['definition'] == definition.text:
                    palabra = row['word']
            try:
                inputElement = driver.find_element_by_class_name('AutoExpandTextarea-textarea')
                inputElement.send_keys(palabra)
                time.sleep(.5)
                inputElement.send_keys(Keys.ENTER)  
                time.sleep(.5)
            except NoSuchElementException:
                button = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div/div[2]/div/div/div[1]/div/button')
                button.click()
        count += 1
    print('Solved!') 
    driver.close()


