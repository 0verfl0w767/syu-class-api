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
import math
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from syuclass.process.BaseProcess import BaseProcess
from syuclass.utils.api import API
from syuclass.utils.logger import Logger

class LectureCoreProcess(BaseProcess):
  def __init__(self, DRIVER: webdriver.Chrome, LOGGER: Logger):
    self.DRIVER = DRIVER
    self.LOGGER = LOGGER
    
    self.API = API('syu_api', LOGGER)
  
  # Selenium + BeautifulSoup
  def onRun(self) -> None:
    time.sleep(3)
    
    self.DRIVER.switch_to.frame("ifrForm")
    
    MAX = int(self.DRIVER.find_element(By.XPATH, "//*[@id=\"gdM0_F0_total_cnt\"]").text[:-1]) # [:3] -> [:-1]
    X = math.floor((MAX - 1) / 21)

    around_time = -1
    
    self.LOGGER.debuggerInfo(f"{MAX} classes were searched...")
    self.LOGGER.debuggerInfo(f"It will run around {X} times...")

    while True:
      tr_count = 0
      around_time += 1
      maxStatus = False
      
      self.LOGGER.debuggerInfo(f"Around {around_time} times...")
      
      if around_time > X:
        self.LOGGER.debuggerInfo("Exit the process...")
        break
      
      soup = BeautifulSoup(self.DRIVER.page_source, 'html.parser')
      
      for tr in soup.select("tbody[id=\"gdM0_F0_body_tbody\"] tr"):
        tr_count += 1
        td_index = -1
        rawClassInfo = []
        text = ""
        
        if (tr_count == 22):
          self.DRIVER.find_element(By.XPATH, "//*[@id=\"gdM0_F0\"]").send_keys(Keys.PAGE_DOWN)
          tr_count = 0
          
          if around_time < X:
            break
        
        if maxStatus:
          break
        
        for td in tr.select("td"):
          td_index += 1
          rawClassInfo.append(td.text)
          
          if rawClassInfo[0] == "":
            break
          
          if around_time == X and int(rawClassInfo[0]) <= around_time * 21:
            break
          
          if int(rawClassInfo[0]) == MAX:
            maxStatus = True
          
          if td_index == 1 or td_index == 6 or td_index == 11 or td_index == 12 or td_index > 14:
            continue
          
          text += td.text + " "
        
        if not text:
          continue
        
        self.API.apiWrite(rawClassInfo)
        
        self.LOGGER.progress(int(rawClassInfo[0]), MAX, "Progress:", 1, 50)
        self.LOGGER.debuggerInfo(text)
    
    self.API.jsonWrite()