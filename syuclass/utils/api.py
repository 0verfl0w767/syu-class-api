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

from syuclass.utils.logger import Logger

class API:
  def __init__(self, LOGGER: Logger, DIR_NAME: str, PATH_NAME: str):
    self.LOGGER = LOGGER
    
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "../../data/" + DIR_NAME)):
      os.makedirs(os.path.join(os.path.dirname(__file__), "../../data/" + DIR_NAME))
    
    self.API_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/" + DIR_NAME + "/" + PATH_NAME + ".json"))
    self.API_DATA = []
  
  def apiWrite(self, rawClassInfo: str) -> None:
    self.API_DATA.append({
      "순번": rawClassInfo[0],
      "강좌번호": rawClassInfo[2],
      "과목코드": rawClassInfo[3],
      "과목명": rawClassInfo[4],
      "학부(과)": rawClassInfo[5],
      "학년": rawClassInfo[7],
      "이수구분": rawClassInfo[8],
      "영역구분": rawClassInfo[9],
      "학점": rawClassInfo[10],
      "교수명": "" if not rawClassInfo[13] else rawClassInfo[13],
      "수업시간/장소": "" if not rawClassInfo[14] else rawClassInfo[14],
    })
  
  def jsonWrite(self) -> None:
    API_JSON = {}
    API_JSON["time"] = self.LOGGER.getTime()
    API_JSON["api"] = self.API_DATA
    
    with open(self.API_PATH, "w", encoding = "utf-8") as f:
      json.dump(API_JSON, f, ensure_ascii = False, indent = 2)
    
    self.LOGGER.info("Check the API file: " + self.API_PATH)