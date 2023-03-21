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
import datetime
import time

from syuclass.config.ConfigManager import ConfigManager
from syuclass.process.ProcessManager import ProcessManager

CONFIG_OPTIONS = ConfigManager().onRun()
DEBUGGER = False # Default: False

start = time.time()

PROCESSMANAGER = ProcessManager(CONFIG_OPTIONS, DEBUGGER)
PROCESSMANAGER.onRun()

end = time.time()

sec = (end - start)

result = datetime.timedelta(seconds=sec)
print(result)