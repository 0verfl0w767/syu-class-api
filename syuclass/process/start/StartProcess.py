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
import os
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from syuclass.process.BaseProcess import BaseProcess
from syuclass.utils.Logger import Logger

class StartProcess(BaseProcess):
  def __init__(self, OPTIONS: dict, LOGGER: Logger):
    self.OPTIONS = OPTIONS
    self.LOGGER = LOGGER
  
  def onRun(self) -> None:
    # Not work: os.path.exists("C:\\Users\\kim\\Desktop\\Chromium.exe")
    
    CHROMIUM_VER = chromedriver_autoinstaller.get_chrome_version().split(".")[0]
    CHROMIUM_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../" + CHROMIUM_VER + "/chromedriver.exe"))
    
    if not os.path.exists(CHROMIUM_PATH):
      
      self.LOGGER.info("Chromedriver is not found...")
      self.LOGGER.info("Start a manual download...")
      
      chromedriver_autoinstaller.install(True)
      
      self.LOGGER.info("Check the chromedriver.exe: " + CHROMIUM_PATH)
    
    options = Options()
    options.add_argument("headless")
    options.add_argument("disable-gpu")
    # options.add_argument("disable-infobars")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--start-maximized")
      
    self.DRIVER = webdriver.Chrome(CHROMIUM_PATH, options = options)
    self.DRIVER.get("https://suwings.syu.ac.kr/sso/login.jsp")
    
    self.LOGGER.info("StartProcess succeeded...")