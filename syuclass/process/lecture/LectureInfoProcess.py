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
from selenium.webdriver.common.by import By

from syuclass.process.BaseProcess import BaseProcess
from syuclass.utils.logger import Logger

class LectureInfoProcess(BaseProcess):
  def __init__(self, DRIVER: webdriver.Chrome, LOGGER: Logger):
    self.DRIVER = DRIVER
    self.LOGGER = LOGGER
  
  def onRun(self) -> None:
    self.DRIVER.implicitly_wait(4)
    # time.sleep(4)

    classInfo_1 = self.DRIVER.find_element(By.XPATH, "//*[@id=\"treeview1_node_24\"]")
    classInfo_1.click()

    self.DRIVER.implicitly_wait(2)
    # time.sleep(1)

    classInfo_2 = self.DRIVER.find_element(By.XPATH, "//*[@id=\"treeview1_node_25\"]/tbody/tr/td[3]")
    classInfo_2.click()
    
    self.LOGGER.debuggerInfo("LectureInfoProcess succeeded...")