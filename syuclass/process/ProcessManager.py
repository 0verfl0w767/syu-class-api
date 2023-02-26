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

from syuclass.process.LoginProcess import LoginProcess
from syuclass.process.ClassInfoProcess import ClassInfoProcess
from syuclass.process.ClassSearchProcess import ClassSearchProcess
from syuclass.process.CoreProcess import CoreProcess
from syuclass.utils.logger import Logger

class ProcessManager:
  def __init__(self, CHROMIUM_PATH, TARGET_URL, SUWINGS_USERID, SUWINGS_PASSWD, DEBUGGER):
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
    CLASSINFOP = ClassInfoProcess(self.DRIVER, self.LOGGER)
    CLASSINFOP.onRun()
    CLASSSEARCHP = ClassSearchProcess(self.DRIVER, self.LOGGER)
    CLASSSEARCHP.onRun()
    COREP = CoreProcess(self.DRIVER, self.LOGGER)
    COREP.onRun()