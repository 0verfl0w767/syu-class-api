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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from syuclass.process.BaseProcess import BaseProcess
from syuclass.utils.logger import Logger

class LecturePlanProcess(BaseProcess):
  def __init__(self, DRIVER: webdriver.Chrome, LOGGER: Logger):
    self.DRIVER = DRIVER
    self.LOGGER = LOGGER
  
  def setYear(self, year) -> None:
    GETYEAR = self.DRIVER.find_element(By.XPATH, "//*[@id=\"ipF_ENTR_YY\"]")
    GETYEAR.click()
    
    GETYEAR.send_keys(Keys.ARROW_RIGHT)
    GETYEAR.send_keys(Keys.ARROW_RIGHT)
    GETYEAR.send_keys(Keys.BACK_SPACE)
    GETYEAR.send_keys(year)

    self.DRIVER.implicitly_wait(2)
    #time.sleep(1)
  
  def setSemester(self, semester) -> None:
    self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_SHTM\"]").click()
    
    # 1학기 정규 //*[@id="sbF_SHTM_itemTable_0"]
    # 1학기 계절 //*[@id="sbF_SHTM_itemTable_1"]
    # 2학기 정규 //*[@id="sbF_SHTM_itemTable_2"]
    # 2학기 계절 //*[@id="sbF_SHTM_itemTable_3"]
    
    self.DRIVER.find_element(By.XPATH, semester).click()

    self.DRIVER.implicitly_wait(2)
    # time.sleep(1)
  
  def setCollege(self, college) -> None:
    self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_COLG_CD\"]").click()
    
    # 신학대학 //*[@id="sbF_COLG_CD_itemTable_1"]
    # 인문사회대학 //*[@id="sbF_COLG_CD_itemTable_2"]
    # 보건복지대학 //*[@id="sbF_COLG_CD_itemTable_3"]
    # 간호대학 //*[@id="sbF_COLG_CD_itemTable_4"]
    # 약학대학 //*[@id="sbF_COLG_CD_itemTable_5"]
    # 과학기술대학 //*[@id="sbF_COLG_CD_itemTable_6"]
    # 미래융합대학 //*[@id="sbF_COLG_CD_itemTable_7"]
    # 자유전공학부 //*[@id="sbF_COLG_CD_itemTable_8"]
    # 스미스교양대학 //*[@id="sbF_COLG_CD_itemTable_9"]
    # 믄화예술대학 //*[@id="sbF_COLG_CD_itemTable_10"]
    # 스미스학부대학 //*[@id="sbF_COLG_CD_itemTable_11"]
    
    self.DRIVER.find_element(By.XPATH, college).click()

    self.DRIVER.implicitly_wait(2)
    # time.sleep(1)
  
  def setUndergraduate(self, undergraduate) -> None:
    self.DRIVER.find_element(By.XPATH, "//*[@id=\"sbF_FCLT_CD\"]").click()
    
    self.DRIVER.find_element(By.XPATH, undergraduate).click()
    
    self.DRIVER.implicitly_wait(2)
    # time.sleep(1)
  
  def onRun(self) -> None:
    # LOADING ISSUE -> Page not loaded
    # self.DRIVER.implicitly_wait(3)
    time.sleep(2)

    self.DRIVER.switch_to.frame("iframe1")
    self.DRIVER.switch_to.frame("ifrForm")

    self.setYear("3")
    self.setSemester("//*[@id=\"sbF_SHTM_itemTable_0\"]")
    self.setCollege("//*[@id=\"sbF_COLG_CD_itemTable_2\"]")
    self.setUndergraduate("//*[@id=\"sbF_FCLT_CD_itemTable_13\"]")

    self.DRIVER.switch_to.default_content()
    self.DRIVER.switch_to.frame("iframe1")

    self.DRIVER.find_element(By.XPATH, "//*[@id=\"tgSelect\"]").click()
    