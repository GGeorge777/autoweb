import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

import time

arquivo_excel = 'Flow.xlsx'
url = "https://www.rpachallenge.com/"

chrome = webdriver.Chrome()
chrome.get(url)

time.sleep(12)

df= pd.read_excel(arquivo_excel)

for index,row in df.iterrows():
    print("Index: " + str(index) + " email: " + str(row["Email"]))
    print("Index: " + str(index) + " primeiro nome: " + str(row["First Name"]))
    print("Index: " + str(index) + " ultimo nome: " + str(row["Last Name "]))
    print("Index: " + str(index) + " empresa nome: " + str(row["Company Name"]))
    print("Index: " + str(index) + " telefone: " + str(row["Phone Number"]))
    print("Index: " + str(index) + " papel da empresa: " + str(row["Role in Company"]))
    print("Index: " + str(index) + " Endereco: " + str(row["Address"]))

    chrome.find_element(By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button").click()

    
    elemento_texto_Email = chrome.find_element(By.XPATH,"//input[@ng-reflect-name='labelEmail']")
    elemento_texto_Email.send_keys(row["Email"])

    elemento_texto_FirstName = chrome.find_element(By.XPATH,"//input[@ng-reflect-name='labelFirstName']")
    elemento_texto_FirstName.send_keys(row["First Name"])

    elemento_texto_LastName = chrome.find_element(By.XPATH,"//input[@ng-reflect-name='labelLastName']")
    elemento_texto_LastName.send_keys(row["Last Name "])

    elemento_texto_CompanyName = chrome.find_element(By.XPATH,"//input[@ng-reflect-name='labelCompanyName']")
    elemento_texto_CompanyName.send_keys(row["Company Name"])

    elemento_texto_PhoneName= chrome.find_element(By.XPATH,"//input[@ng-reflect-name='labelPhone']")
    elemento_texto_PhoneName.send_keys(row["Phone Number"])

    
    elemento_texto_RoleInCompany = chrome.find_element(By.XPATH,"//input[@ng-reflect-name='labelRole']")
    elemento_texto_RoleInCompany.send_keys(row["Role in Company"])

    
    elemento_texto_Address = chrome.find_element(By.XPATH,"//input[@ng-reflect-name='labelAddress']")
    elemento_texto_Address.send_keys(row["Address"])

    # Enviar o formulário
    enviar_button = chrome.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input")
    enviar_button.click()


print(df)

