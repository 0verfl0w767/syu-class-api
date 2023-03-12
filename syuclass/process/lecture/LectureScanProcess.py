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
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from syuclass.process.BaseProcess import BaseProcess
from syuclass.process.lecture.LectureCoreProcess import LectureCoreProcess
from syuclass.process.lecture.LecturePlanProcess import LecturePlanProcess
from syuclass.utils.api import API
from syuclass.utils.logger import Logger

class LectureScanProcess(BaseProcess):
  def __init__(self, DRIVER: webdriver.Chrome, OPTIONS: dict, LOGGER: Logger):
    self.DRIVER = DRIVER
    self.OPTIONS = OPTIONS
    self.LOGGER = LOGGER
    
    self.API = API(OPTIONS, LOGGER)
  
  def onRun(self) -> None:
    # LOADING ISSUE -> Page not loaded
    # self.DRIVER.implicitly_wait(3)
    time.sleep(2)

    self.DRIVER.switch_to.frame("iframe1")
    self.DRIVER.switch_to.frame("ifrForm")

    self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_COLG_CD\"]").click()
    
    soup = BeautifulSoup(self.DRIVER.page_source, 'html.parser')
    identification = 0
    
    for collegeTD in soup.select("table[id=\"sbF_COLG_CD_itemTable_main\"] tbody tr td"):
      if (collegeTD["id"] == "sbF_COLG_CD_itemTable_0"):
        continue
      
      self.DRIVER.find_element(By.XPATH, "//*[@id=\"" + collegeTD["id"] + "\"]").click()
      
      #time.sleep(1)
      
      self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_FCLT_CD\"]").click()
      
      soup = BeautifulSoup(self.DRIVER.page_source, 'html.parser')
      
      for undergraduateTD in soup.select("table[id=\"sbF_FCLT_CD_itemTable_main\"] tbody tr td"):
        if (undergraduateTD["id"] == "sbF_FCLT_CD_itemTable_0"):
          continue
        
        identification += 1
        
        LPP = LecturePlanProcess(self.DRIVER, self.OPTIONS, self.LOGGER, collegeTD["id"], undergraduateTD["id"])
        LPP.onRun()
        
        LCP = LectureCoreProcess(self.DRIVER, self.OPTIONS, self.LOGGER, collegeTD.text, undergraduateTD.text)
        LCP.onRun()
        
        self.API.lectureNameWrite(collegeTD.text, undergraduateTD.text, identification)
      
      self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_COLG_CD\"]").click()
    
    self.API.jsonWrite(".", "학부(과)")
    
    self.LOGGER.debuggerInfo("LectureScanProcess succeeded...")