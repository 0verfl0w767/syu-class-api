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
from syuclass.process.start.StartProcess import StartProcess
from syuclass.process.login.LoginProcess import LoginProcess
from syuclass.process.lecture.LectureInfoProcess import LectureInfoProcess
from syuclass.process.lecture.LectureScanProcess import LectureScanProcess
from syuclass.utils.logger import Logger

class ProcessManager:
  def __init__(self, OPTIONS: dict, DEBUGGER: bool):
    self.OPTIONS = OPTIONS
    
    self.LOGGER = Logger(DEBUGGER)
      
  def onRun(self) -> None:
    SP = StartProcess(self.OPTIONS, self.LOGGER)
    SP.onRun()
    
    LP = LoginProcess(SP.DRIVER, self.OPTIONS, self.LOGGER)
    LP.onRun()
    
    LIP = LectureInfoProcess(SP.DRIVER, self.LOGGER)
    LIP.onRun()
    
    LSP = LectureScanProcess(SP.DRIVER, self.OPTIONS, self.LOGGER)
    LSP.onRun()