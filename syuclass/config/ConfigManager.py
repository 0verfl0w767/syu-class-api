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
import json

class ConfigManager:
  def __init__(self):
    pass
  
  def onRun(self) -> dict:
    DATA_PATH = "../../"
    REAL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), DATA_PATH + "/config.json"))
    
    with open(REAL_PATH, "r", encoding = "utf-8") as f:
      JSON_DATA = json.load(f)
      
      return {
        "userid": JSON_DATA["userid"],
        "passwd": JSON_DATA["passwd"],
        "check_year": JSON_DATA["check_year"],
        "check_semester": JSON_DATA["check_semester"],
        "check_grade": JSON_DATA["check_grade"],
        "year": JSON_DATA["year"],
        "semester": JSON_DATA["semester"],
        "grade": JSON_DATA["grade"],
      }