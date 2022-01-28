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
logged = False
        
def SignIn(user, password, num):
    global maxcount
    global logged
    if(logged == False):
        maxcount = 0
        with open('Lists/'+num+'.csv', 'r') as lista:
                csv_dict_reader = csv.DictReader(lista, delimiter='¿')
                for row in csv_dict_reader:
                    maxcount += 1
                    print(maxcount)
        driver.get('https://quizlet.com/es')
        Signin_button = driver.find_element_by_xpath('//*[@id="TopNavigationReactTarget"]/header/div/div[2]/div[3]/button[1]')
        Signin_button.click()
        user_blank = driver.find_element_by_id('username')
        pass_blank = driver.find_element_by_id('password')
        user_blank.send_keys(user)
        pass_blank.send_keys(password)
        pass_blank.send_keys(Keys.ENTER)
        time.sleep(3)
        logged = True
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
def solvewrite(nombreL):
    with open('Lists/'+nombreL+'.csv', 'r') as lista:
            driver.implicitly_wait(3)
            csv_dict_reader = csv.DictReader(lista, delimiter='¿')
            try:
                definition = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[1]/div/div[2]/div/div/div')
            except NoSuchElementException:
                button = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/div/div/div/div[2]/div/button')
                button.click()
                time.sleep(1.5)
            definition = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[1]/div/div[2]/div/div/div')
            for row in csv_dict_reader:
                if row['definition'] == definition.text:
                    palabra = row['word']
                
            inputElement = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[2]/form/div[1]/label/input')
            inputElement.send_keys(palabra)
            time.sleep(.5)
            inputElement.send_keys(Keys.ENTER)  
            time.sleep(.5)
       

def solvemultiple(nombreL):
    driver.implicitly_wait(5)
    with open('Lists/'+nombreL+'.csv', 'r') as lista:
            csv_dict_reader = csv.DictReader(lista, delimiter='¿')
            try:
                option1 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[2]/div/section[1]')
                option2 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[2]/div/section[2]')
                option3 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[2]/div/section[3]')
                option4 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[2]/div/section[4]')
            except NoSuchElementException:
                driver.implicitly_wait(10)
                option1 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[2]/div/section[1]/div[2]/div')
                option2 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[2]/div/section[2]/div[2]/div/div')
                option3 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[2]/div/section[3]/div[2]/div/div')
                option4 = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/div[2]/div/section[4]/div[2]/div/div')
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
        continue1 = driver.find_element_by_xpath('//*[@id="StudyPathTarget"]/div/div[2]/div/div/div/div/div/button')
    except NoSuchElementException:
        continue1 = None
        print("Continue not there")
    if continue1 != None:
        continue1.click()
    try:
        skip = driver.find_element_by_xpath('//*[@id="StudyPathTarget"]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/button')
    except NoSuchElementException:
        skip = None
        print("Skip not there")
    if skip != None:
        skip.click()
    try:
        Continuar = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/article/button')
    except NoSuchElementException:
        Continuar = None
        print("Continuar not there")
    if Continuar != None:
        Continuar.click()      
    while True:
        try:
            end = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div[2]/div/div/div/div/div[1]/img')
            if(end != None):
                break
        except NoSuchElementException:
            print("Not yet")    
        try:
            try:
                solvemultiple(nombreL)
            except NoSuchElementException:
                solvewrite(nombreL)
        except NoSuchElementException:
            print("Trying to find continue")
            driver.implicitly_wait(2)
            try:
                boton = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div[2]/div/div/div/div[3]/div/div/button')
            except:
                boton = None
                print("NO button")
            if boton != None:
                boton.click()
    print('Solved!')
def SolveSpell(url,nombreL):
    percentage = 0
    driver.get(url)
    palabra=""
    time.sleep(2)
    while percentage < 100:
        percentageElement = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div/div[1]/div/div/aside/div[2]/div[2]/div[1]/div/div[2]/div[2]')
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
                try:
                    button = driver.find_element_by_xpath('//*[@id="AssistantModeTarget"]/div/div/div/div[2]/div/div/div[1]/div/button')
                    button.click()
                except NoSuchElementException:
                    if(percentage == 100):
                        print("Solved!")
        intper = percentageElement.text.replace("%","")
        percentage = int(intper)
    print('Solved!') 


