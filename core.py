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
  
  def api(self, classRealInfo) -> None:
    self.API_DATA["api"].append({
      "순번": classRealInfo[0],
      "강좌번호": classRealInfo[2],
      "과목코드": classRealInfo[3],
      "과목명": classRealInfo[4],
      "학부(과)": classRealInfo[5],
      "학년": classRealInfo[7],
      "이수구분": classRealInfo[8],
      "영역구분": classRealInfo[9],
      "학점": classRealInfo[10],
      "교수명": "" if not classRealInfo[13] else classRealInfo[13],
      "수업시간/장소": "" if not classRealInfo[14] else classRealInfo[14],
    })
  
  def run(self) -> None:
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
        
        self.LOGGER.progress(int(classRealInfo[0]), MAX, "Progress:", 1, 50)
        self.LOGGER.debuggerInfo(msg)
        
        self.api(classRealInfo)
  
    with open("./syu_api.json", "w", encoding = "utf-8") as f:
      json.dump(self.API_DATA, f, ensure_ascii = False, indent = 2)