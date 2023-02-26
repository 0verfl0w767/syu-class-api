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

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ClassSearchProcess:
  def __init__(self, DRIVER, LOGGER):
    self.DRIVER = DRIVER
    self.LOGGER = LOGGER
  
  def onRun(self) -> None:
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
    