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

class API:
  def __init__(self, PATH_NAME, LOGGER):
    self.LOGGER = LOGGER
    
    self.API_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/' + PATH_NAME + '.json'))
    self.API_DATA = {}
    self.API_DATA["time"] = LOGGER.getTime()
    self.API_DATA["api"] = []
  
  def apiWrite(self, rawClassInfo) -> None:
    
    ########### rawClassInfo data
    # rawClassInfo[0]: 순번
    # rawClassInfo[1]: 알 수 없음
    # rawClassInfo[2]: 강좌번호
    # rawClassInfo[3]: 과목코드
    # rawClassInfo[4]: 과목명
    # rawClassInfo[5]: 학부(과)
    # rawClassInfo[6]: 공백
    # rawClassInfo[7]: 학년
    # rawClassInfo[8]: 이수구분
    # rawClassInfo[9]: 영역구분
    # rawClassInfo[10]: 학점
    # rawClassInfo[11]: 알 수 없음
    # rawClassInfo[12]: 알 수 없음
    # rawClassInfo[13]: 교수명
    # rawClassInfo[14]: 수업시간/장소
    # rawClassInfo[15]: 수업시간
    # rawClassInfo[16]: 장소
    # rawClassInfo[17]: 출력
    # rawClassInfo[18]: 공백
    # rawClassInfo[19]: 평가조회
    # rawClassInfo[20]: 공백
    # rawClassInfo[21]: 공백
    # rawClassInfo[22]: 공백
    # rawClassInfo[23]: 공백
    # rawClassInfo[24]: 알 수 없음
    # rawClassInfo[25]: 알 수 없음
    # rawClassInfo[26]: 알 수 없음
    # rawClassInfo[27]: 개설년도
    # rawClassInfo[28]: 개설학기
    # rawClassInfo[29]: 알 수 없음
    # rawClassInfo[30]: 알 수 없음
    # rawClassInfo[31]: 알 수 없음
    # rawClassInfo[32]: 알 수 없음
    # rawClassInfo[33]: 알 수 없음
    ########### rawClassInfo data
    
    self.API_DATA["api"].append({
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
    self.LOGGER.info("Check the API file: " + self.API_PATH)
    
    with open(self.API_PATH, "w", encoding = "utf-8") as f:
      json.dump(self.API_DATA, f, ensure_ascii = False, indent = 2)