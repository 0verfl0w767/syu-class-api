#
#     ____                  __________
#    / __ \_   _____  _____/ __/ / __ \_      __
#   / / / / | / / _ \/ ___/ /_/ / / / / | /| / /
#  / /_/ /| |/ /  __/ /  / __/ / /_/ /| |/ |/ /
#  \____/ |___/\___/_/  /_/ /_/\____/ |__/|__/
# 
#  The copyright indication and this authorization indication shall be
#  recorded in all copies or in important parts of the Software.
# 
#  @author 0verfl0w767
#  @link https://github.com/0verfl0w767
#  @license MIT LICENSE
#
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

import logger
import core

class Process:
  def __init__(self, CHROMIUM_PATH, TARGET_URL, SUWINGS_USERID, SUWINGS_PASSWD, DEBUGGER):
    self.CHROMIUM_PATH = CHROMIUM_PATH
    self.TARGET_URL = TARGET_URL
    self.SUWINGS_USERID = SUWINGS_USERID
    self.SUWINGS_PASSWD = SUWINGS_PASSWD
    self.DEBUGGER = DEBUGGER
    
    self.LOGGER = logger.Logger(DEBUGGER)
    
    options = Options()
    options.add_argument("headless")
    options.add_argument("disable-gpu")
    # options.add_argument("disable-infobars")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--start-maximized")
    
    self.DRIVER = webdriver.Chrome(self.CHROMIUM_PATH, options=options)
    self.DRIVER.get(self.TARGET_URL)
  
  def login(self) -> None:
    # LOADING ISSUE -> Cannot read properties of undefined (reading 'hybridEncrypt') : Not Loading Script..
    # self.DRIVER.implicitly_wait(2)
    time.sleep(2)
    
    userid = self.DRIVER.find_element(By.XPATH, "//*[@id=\"edId\"]")
    password = self.DRIVER.find_element(By.XPATH, "//*[@id=\"edPass\"]")

    userid.click()
    userid.send_keys(self.SUWINGS_USERID)

    self.DRIVER.implicitly_wait(2)
    # time.sleep(1)

    password.click()
    password.send_keys(self.SUWINGS_PASSWD)

    self.DRIVER.implicitly_wait(2)
    # time.sleep(1)
    
    login_button = self.DRIVER.find_element(By.XPATH, "//*[@id=\"imgLogin\"]")
    login_button.click()

    self.LOGGER.debuggerInfo("Login completed...")
  
  def classInfo(self) -> None:
    self.DRIVER.implicitly_wait(4)
    # time.sleep(4)

    classInfo_1 = self.DRIVER.find_element(By.XPATH, "//*[@id=\"treeview1_node_24\"]")
    classInfo_1.click()

    self.DRIVER.implicitly_wait(2)
    # time.sleep(1)

    classInfo_2 = self.DRIVER.find_element(By.XPATH, "//*[@id=\"treeview1_node_25\"]/tbody/tr/td[3]")
    classInfo_2.click()
    
    self.LOGGER.debuggerInfo("ClassInfo completed...")
  
  def classSearch(self) -> None:
    # LOADING ISSUE -> Page not loaded
    # self.DRIVER.implicitly_wait(3)
    time.sleep(2)

    self.DRIVER.switch_to.frame("iframe1")
    self.DRIVER.switch_to.frame("ifrForm")

    classSearch_1 = self.DRIVER.find_element(By.XPATH, "//*[@id=\"ipF_ENTR_YY\"]")
    classSearch_1.click()
    classSearch_1.send_keys(Keys.ARROW_RIGHT)
    classSearch_1.send_keys(Keys.ARROW_RIGHT)
    classSearch_1.send_keys(Keys.BACK_SPACE)
    classSearch_1.send_keys("3")

    self.DRIVER.implicitly_wait(2)
    #time.sleep(1)

    classSearch_2_1 = self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_SHTM\"]")
    classSearch_2_1.click()
    classSearch_2_2 = self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_SHTM_itemTable_0\"]")
    classSearch_2_2.click()

    self.DRIVER.implicitly_wait(2)
    # time.sleep(1)

    classSearch_3_1 = self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_COLG_CD\"]")
    classSearch_3_1.click()
    classSearch_3_2 = self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_COLG_CD_itemTable_2\"]")
    classSearch_3_2.click()

    self.DRIVER.implicitly_wait(2)
    # time.sleep(1)

    classSearch_4_1 = self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_FCLT_CD\"]")
    classSearch_4_1.click()
    classSearch_4_2 = self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_FCLT_CD_itemTable_13\"]")
    classSearch_4_2.click()

    self.DRIVER.implicitly_wait(2)
    # time.sleep(1)

    self.DRIVER.switch_to.default_content()
    self.DRIVER.switch_to.frame("iframe1")

    classSearch_5 = self.DRIVER.find_element(By.XPATH, "//*[@id=\"tgSelect\"]")
    classSearch_5.click()
    
    self.LOGGER.debuggerInfo("ClassSearch completed...")
  
  def core(self) -> None:
    # LOADING ISSUE -> Page not loaded
    # self.DRIVER.implicitly_wait(3)
    time.sleep(3)
    
    self.DRIVER.switch_to.frame("ifrForm")
    
    CORE = core.Core(self.DRIVER, self.DEBUGGER)
    CORE.run()
  
  def run(self) -> None:
    self.LOGGER.info("syu-class-api script running...")
    
    self.login() # LOGIN PROCESS
    self.classInfo() # CLASSINFO PROCESS
    self.classSearch() # CLASSSEARCH PROCESS
    self.core() # CORE PROCESS