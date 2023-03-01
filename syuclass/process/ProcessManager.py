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

from syuclass.process.login.LoginProcess import LoginProcess
from syuclass.process.lecture.LectureInfoProcess import LectureInfoProcess
from syuclass.process.lecture.LecturePlanProcess import LecturePlanProcess
from syuclass.process.lecture.LectureCoreProcess import LectureCoreProcess
from syuclass.process.lecture.LectureScanProcess import LectureScanProcess
from syuclass.utils.logger import Logger

class ProcessManager:
  def __init__(self, CHROMIUM_PATH: str, TARGET_URL: str, SUWINGS_USERID: str, SUWINGS_PASSWD: str, DEBUGGER: bool):
    self.SUWINGS_USERID = SUWINGS_USERID
    self.SUWINGS_PASSWD = SUWINGS_PASSWD
    self.DEBUGGER = DEBUGGER
    
    self.LOGGER = Logger(DEBUGGER)
    
    options = Options()
    options.add_argument("headless")
    options.add_argument("disable-gpu")
    # options.add_argument("disable-infobars")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--start-maximized")

    self.DRIVER = webdriver.Chrome(CHROMIUM_PATH, options = options)
    self.DRIVER.get(TARGET_URL)
      
  def onRun(self) -> None:
    LOGINP = LoginProcess(self.DRIVER, self.LOGGER, self.SUWINGS_USERID, self.SUWINGS_PASSWD)
    LOGINP.onRun()
    
    CLASSINFOP = LectureInfoProcess(self.DRIVER, self.LOGGER)
    CLASSINFOP.onRun()
    
    SCANP = LectureScanProcess(self.DRIVER, self.LOGGER)
    SCANP.onRun()