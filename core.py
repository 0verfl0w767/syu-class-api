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
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import math
import json

import logger

class Core:
  def __init__(self, DRIVER, DEBUGGER):
    self.DRIVER = DRIVER
    self.DEBUGGER = DEBUGGER
    
    self.LOGGER = logger.Logger(DEBUGGER)
    
    self.API_DATA = {}
    self.API_DATA["time"] = self.LOGGER.getTime()
    self.API_DATA["api"] = []
  
  def api(self, rawClassInfo) -> None:
    self.API_DATA["api"].append({
      "순번": rawClassInfo[0],
      "강좌번호": rawClassInfo[2],
      "과목코드": rawClassInfo[3],
      "과목명": rawClassInfo[4],
      "학부(과)": rawClassInfo[5],
      "학년": rawClassInfo[7],
      "이수구분": rawClassInfo[8],
      "영역구분": rawClassInfo[9],
      "학점": rawClassInfo[10],
      "교수명": "" if not rawClassInfo[13] else rawClassInfo[13],
      "수업시간/장소": "" if not rawClassInfo[14] else rawClassInfo[14],
    })
  
  # Selenium + BeautifulSoup
  def run(self) -> None:
    MAX = int(self.DRIVER.find_element(By.XPATH, "//*[@id=\"gdM0_F0_total_cnt\"]").text[:-1]) # [:3] -> [:-1]
    X = math.floor((MAX - 1) / 21)

    around_time = -1
    
    self.LOGGER.info(f"Debugger Mode: {self.DEBUGGER}...")
    self.LOGGER.debuggerInfo(f"{MAX} classes were searched...")
    self.LOGGER.debuggerInfo(f"It will run around {X} times...")

    while True:
      tr_count = 0
      around_time += 1
      maxStatus = False
      
      self.LOGGER.debuggerInfo(f"Around {around_time} times...")
      
      if around_time > X:
        self.LOGGER.info("Check the file: syu_api.json")
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
          
          if (around_time < X):
            break
        
        if (maxStatus):
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
        
        self.api(rawClassInfo)
        
        self.LOGGER.progress(int(rawClassInfo[0]), MAX, "Progress:", 1, 50)
        self.LOGGER.debuggerInfo(text)
    
    with open("./syu_api.json", "w", encoding = "utf-8") as f:
      json.dump(self.API_DATA, f, ensure_ascii = False, indent = 2)
  
  # Selenium ( DEPRECATED )
  def deprecated_run(self) -> None:
    MAX = int(self.DRIVER.find_element(By.XPATH, "//*[@id=\"gdM0_F0_total_cnt\"]").text[:-1]) # [:3] -> [:-1]
    X = math.floor((MAX - 1) / 21)

    ccc = -1 # tbody count check
    
    self.LOGGER.info(f"Debugger Mode: {self.DEBUGGER}...")
    self.LOGGER.debuggerInfo(f"{MAX} classes were searched...")
    self.LOGGER.debuggerInfo(f"It will run around {X} times...")

    while True:
      classReal_tbody = self.DRIVER.find_element(By.XPATH, "//*[@id=\"gdM0_F0_body_tbody\"]")
      
      cc = 0 # tr count check
      ccc += 1 # tbody count check
      
      self.LOGGER.debuggerInfo(f"Around {ccc} times...")
      
      if ccc > X: # tbody count check
        self.LOGGER.debuggerInfo("Exit the process...")
        break
      
      for tr in classReal_tbody.find_elements(By.TAG_NAME, "tr"):
        cc += 1 # tr count check
        
        if (cc == 22): # 1 + 21 + 21 + 21 + ... + 21
          self.DRIVER.find_element(By.XPATH, "//*[@id=\"gdM0_F0\"]").send_keys(Keys.PAGE_DOWN)
          cc = 0 # tr count check
          
          if (ccc < X): # tbody count check
            break
        
        classReal_td = tr.find_elements(By.TAG_NAME, "td")
        classRealInfo = []
        msg = ""
        count = -1 # classInfo index check
        
        for td in classReal_td:
          count += 1 # classInfo index check
          classRealInfo.append(td.text)
          
          if classRealInfo[0] == "":
            break
          
          if ccc == X and int(classRealInfo[0]) <= ccc * 21: # tbody count check
            break
          
          if not td.text:
            continue
          
          if td.text == "출력" or td.text == "평가조회":
            continue
          
          msg += td.text + " "
        
        if not msg:
          continue
        
        self.api(classRealInfo)
        
        self.LOGGER.progress(int(classRealInfo[0]), MAX, "Progress:", 1, 50)
        self.LOGGER.debuggerInfo(msg)
  
    with open("./syu_api.json", "w", encoding = "utf-8") as f:
      json.dump(self.API_DATA, f, ensure_ascii = False, indent = 2)