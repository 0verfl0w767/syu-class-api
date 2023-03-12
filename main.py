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

SYU_API_OPTIONS = {
  "userid": "test1234",
  "passwd": "test1234",
  "year": "2023",
  "semester": "1학기 정규",
  # 1학기 정규, 1학기 계절, 2학기 정규, 2학기 계절
}

DEBUGGER = False # Default: False

PROCESSMANAGER = ProcessManager(SYU_API_OPTIONS, DEBUGGER)
PROCESSMANAGER.onRun()