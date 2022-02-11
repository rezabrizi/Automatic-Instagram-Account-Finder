
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#variables
chrome = webdriver.Chrome("/Users/rezatabrizi/Downloads/chromedriver")
#Open chrome
def openChrome():
    chrome.maximize_window()
    chrome.get("https://www.instagram.com/")

#Login
def logIn(username, password):
    WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    usern = chrome.find_element_by_name("username")
    usern.send_keys(username)
    passw = chrome.find_element_by_name("password")
    passw.send_keys(password)
    WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")))
    log_cl = chrome.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
    log_cl.click()
    WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")))
    saveInfo = chrome.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    saveInfo.click()
    WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")))
    Notif = chrome.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
    Notif.click()

def findAcc(accName):
    searchB = chrome.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
    searchB.send_keys(accName)
    WebDriverWait(chrome, 10).until(EC.element_to_be_clickable(
        (By.XPATH,
         "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div")))
    utdB = chrome.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div")
    utdB.click()

def findMatrixRow(totalPost):
    return totalPost//3

def lastCol(totalPost):
    return totalPost%3

def openPost(i, j):
    WebDriverWait(chrome, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[{}]/div[{}]/a/div[1]/div[2]".format(i, j))))
    postToOpen = chrome.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[{}]/div[{}]/a/div[1]/div[2]".format(i, j))
    postToOpen.click()

def getCaption():
    WebDriverWait(chrome, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/div[6]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]")))
    return (chrome.find_element_by_xpath(
        "/html/body/div[6]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]").text).lower()

def getUsername():
    tag = chrome.find_element_by_xpath(
        "/html/body/div[6]/div[2]/div/article/div[2]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[2]/button")
    tag.click()
    WebDriverWait(chrome, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/div[6]/div[2]/div/article/div[2]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[3]/a/span/span")))
    tagB = chrome.find_element_by_xpath(
        "/html/body/div[6]/div[2]/div/article/div[2]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[3]/a/span/span")
    tagB.click()
    time.sleep(1)
    WebDriverWait(chrome, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/div[1]/section/main/div/header/section/div[1]/h2")))
    userN =  chrome.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/h2").text
    chrome.back()
    time.sleep(2)
    chrome.back()
    return userN

def interest(caption, interest):
    caption = caption.lower()
    interest = interest.lower()
    if interest in caption:
        return True
    else:
        return False

openChrome()
logIn("rezabrizi", "Reza2003!")
findAcc("utdclass")

rows = findMatrixRow(583)
col = lastCol(583)

for i in range(rows):
   for j in range(3):
        if (i+1 != rows):
            openPost(i+1, j+1)
            if interest(getCaption(), "Computer Science"):
                print(getUsername())
            else:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[6]/div[3]/button")))
                backP = chrome.find_element_by_xpath("/html/body/div[6]/div[3]/button")
                backP.click()
        else:
            openPost(i+1, col)
            if interest(getCaption(), "Computer Science"):
                print(getUsername())
            else:
                chrome.back()
