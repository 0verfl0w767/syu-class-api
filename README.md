# SYU-CLASS-PROJECT

`Unofficial su-wings (SAHMYOOK UNIV.) lecture information system.`

---

The project started on January 29, 2023.

Planner: [@0verfl0w767](https://github.com/0verfl0w767)

Developer: [@0verfl0w767](https://github.com/0verfl0w767)

---

SYU-CLASS-API: [@syu-class-api](https://github.com/0verfl0w767/syu-class-api)

SYU-CLASS.KRO.KR: [@syu-class.kro.kr](https://github.com/0verfl0w767/syu-class.kro.kr)

SYU-CLASS-CONVERTER: [@syu-class-converter](https://github.com/0verfl0w767/syu-class-converter)

SYU-CLASS-EXE: [@syu-class-exe](https://github.com/0verfl0w767/syu-class-exe)

# syu-class-api

1. 엔진 구동에 앞서 4개의 모듈을 설치합니다.

```
pip install beautifulsoup4==4.11.1
pip install bs4==0.0.1
pip install chromedriver-autoinstaller==0.4.0
pip install selenium==4.8.0
```

2. 엔진을 실행하고 생성된 config.json를 알맞게 수정합니다.

```
{
  "dev": false,
  "userid": "your su-wings id", // 아이디
  "passwd": "your su-wings pwd", // 비밀번호
  "check_year": false,
  "check_semester": false,
  "check_college": false,
  "check_grade": false,
  "year": "2023", // 년도
  "semester": "1학기 정규", // 학기
  "grade": "전체"
}
```

3. 엔진을 다시 실행하여 data 폴더에 저장 값들을 확인합니다.
