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
import sys
import datetime

class Logger:
  def __init__(self, DEBUGGER = False):
    self.DEBUGGER = DEBUGGER
  
  def getTime(self) -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
  def info(self, text) -> None:
    sys.stdout.write('[' + self.getTime() + '] [INFO] ' + text + "\n")
  
  def debuggerInfo(self, text) -> None:
    if self.DEBUGGER == True:
      sys.stdout.write('[' + self.getTime() + '] [DEBUGGER] ' + text + "\n")
  
  def progress(self, iteration, total, prefix = "", decimals = 1, barLength = 100) -> None:
    if self.DEBUGGER == False:
      formatStr = "{0:." + str(decimals) + "f}"
      percent = formatStr.format(100 * (iteration / float(total)))
      filledLength = int(round(barLength * iteration / float(total)))
      bar = "#" * filledLength + "-" * (barLength - filledLength)
      
      sys.stdout.write("\r%s [%s] %s%s" % (prefix, bar, percent, "%"))
      
      if iteration == total:
        sys.stdout.write("\n")
        sys.stdout.flush()