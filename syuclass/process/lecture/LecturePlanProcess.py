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
from selenium.webdriver.common.keys import Keys

from syuclass.process.BaseProcess import BaseProcess
from syuclass.utils.Logger import Logger

class LecturePlanProcess(BaseProcess):
  def __init__(self, DRIVER: webdriver.Chrome, OPTIONS: dict, LOGGER: Logger, COLLEGE: str, UNDERGRADUATE: str):
    self.DRIVER = DRIVER
    self.OPTIONS = OPTIONS
    self.LOGGER = LOGGER
    self.COLLEGE = COLLEGE
    self.UNDERGRADUATE = UNDERGRADUATE
  
  def setYear(self, year) -> None:
    GET_YEAR = self.DRIVER.find_element(By.XPATH, "//*[@id=\"ipF_ENTR_YY\"]")
    GET_YEAR.click()
    
    GET_YEAR.send_keys(Keys.ARROW_RIGHT)
    GET_YEAR.send_keys(Keys.ARROW_RIGHT)
    GET_YEAR.send_keys(Keys.BACK_SPACE)
    GET_YEAR.send_keys(year[-1])

    self.DRIVER.implicitly_wait(2)
    #time.sleep(1)
  
  def setSemester(self, semester) -> None:
    self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_SHTM\"]").click()
    
    SEMESTER_NUM = {
      "1학기 정규": "0",
      "1학기 계절": "1",
      "2학기 정규": "2",
      "2학기 계절": "3",
    }
    
    semester = "//*[@id=\"sbF_SHTM_itemTable_" + SEMESTER_NUM[semester] +"\"]"
    
    self.DRIVER.find_element(By.XPATH, semester).click()

    self.DRIVER.implicitly_wait(2)
    # time.sleep(1)
  
  def setCollege(self, college) -> None:
    self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_COLG_CD\"]").click()
    
    self.DRIVER.find_element(By.XPATH, college).click()

    self.DRIVER.implicitly_wait(2)
    # time.sleep(1)
  
  def setUndergraduate(self, undergraduate) -> None:
    self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_FCLT_CD\"]").click()
    
    self.DRIVER.find_element(By.XPATH, undergraduate).click()
    
    self.DRIVER.implicitly_wait(2)
    # time.sleep(1)
  
  def setGrade(self, grade) -> None:
    self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_GRDE\"]").click()
    
    self.DRIVER.find_element(By.XPATH, grade).click()
    
    self.DRIVER.implicitly_wait(2)
    # time.sleep(1)
  
  def onRun(self) -> None:
    # LOADING ISSUE -> Page not loaded
    # self.DRIVER.implicitly_wait(3)
    # time.sleep(2)

    # self.DRIVER.switch_to.frame("iframe1")
    # self.DRIVER.switch_to.frame("ifrForm")

    self.setYear(self.OPTIONS["year"])
    self.setSemester(self.OPTIONS["semester"])
    self.setCollege("//*[@id=\"" + self.COLLEGE + "\"]")
    self.setUndergraduate("//*[@id=\"" + self.UNDERGRADUATE + "\"]")
    self.setGrade("//*[@id=\"sbF_GRDE_itemTable_0\"]")

    self.DRIVER.switch_to.default_content()
    self.DRIVER.switch_to.frame("iframe1")

    self.DRIVER.find_element(By.XPATH, "//*[@id=\"tgSelect\"]").click()
    
    self.LOGGER.debuggerInfo("LecturePlanProcess succeeded...")
    