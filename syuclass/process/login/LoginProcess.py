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
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from syuclass.process.BaseProcess import BaseProcess
from syuclass.utils.logger import Logger

class LoginProcess(BaseProcess):
  def __init__(self, DRIVER: webdriver.Chrome, LOGGER: Logger, SUWINGS_USERID: str, SUWINGS_PASSWD: str):
    self.DRIVER = DRIVER
    self.LOGGER = LOGGER
    self.SUWINGS_USERID = SUWINGS_USERID
    self.SUWINGS_PASSWD = SUWINGS_PASSWD
  
  def isLogined(self) -> bool:
    status = False
    
    try:
      self.LOGGER.info(self.DRIVER.switch_to.alert.text)
      status = False
    except:
      status = True
    
    return status
  
  def onRun(self) -> None:
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
    
    # LOADING ISSUE -> Page not loaded
    time.sleep(2)
    
    if not self.isLogined():
      self.LOGGER.debuggerInfo("LoginProcess failed...")
      self.DRIVER.quit()
      sys.exit() # self.DRIVER.quit() ISSUE -> Driver still running

    self.LOGGER.debuggerInfo("LoginProcess succeeded...")