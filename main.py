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
from syuclass.process.ProcessManager import ProcessManager

CHROMIUM_PATH = "C:\\Users\\kim\\Desktop\\Chromium.exe" # Your chromium path
TARGET_URL = "https://suwings.syu.ac.kr/sso/login.jsp"

SUWINGS_USERID = "test1234" # Your suwings userid
SUWINGS_PASSWD = "test1234" # Your suwings passwd

DEBUGGER = False # Default: False

PROCESSMANAGER = ProcessManager(CHROMIUM_PATH, TARGET_URL, SUWINGS_USERID, SUWINGS_PASSWD, DEBUGGER)
PROCESSMANAGER.onRun()