# syu-class-api

비공식 삼육대학교 공통교양 조회 크롤링 엔진 입니다. ([syu-class.kro.kr](http://syu-class.kro.kr))

Python 3.11 버전에서 테스트가 진행되었습니다.

# how to use

본 파일을 실행하기 앞서 Chromium, Python [Selenium, BeautifulSoup] 이 필요합니다.

먼저 main.py를 실행하기 전 main.py 안에 있는 코드를 확인하고

```python
CHROMIUM_PATH = "C:\\Users\\kim\\Desktop\\Chromium.exe" # Your chromium path
TARGET_URL = "https://suwings.syu.ac.kr/sso/login.jsp"

SUWINGS_USERID = "test1234" # Your suwings userid
SUWINGS_PASSWD = "test1234!@#" # Your suwings passwd

DEBUGGER = False # Default: False
```

알맞게 수정하고 실행합니다.

# core.py - 1

기존에 코어 파일에서 selenium 모듈만을 사용했으나 속도 이슈로 인한 심각한 문제가 있었습니다.

이전 코드는 deprecated 되었으며 새롭게 작성된 코드는 selenium + beautifulSoup 모듈을 활용했습니다.

# core.py - 2

따라서 개선된 코드로 다시 실행한 결과로

```
Before:

공통교양 검색 239건, 262.0012초 소요

After:

공통교양 검색 239건, 16.0068초 소요
```

속도가 약 1,537% 로 향상이 되었습니다.
