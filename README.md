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

<br>

# syu-class-api

A syu-class crawling software for su-wings lecture information in Python.

<br>

비공식 삼육대학교 강의계획서 조회 크롤링 엔진 입니다. ([syu-class.kro.kr](http://syu-class.kro.kr))

```
C:.
│  config.json
│  LICENSE
│  main.py
│  README.md
│  requirements.txt
│
└─syuclass
    │  Setup.py
    │
    ├─config
    │  │  ConfigManager.py
    │  │
    │  └─__pycache__
    │          ConfigManager.cpython-311.pyc
    │
    ├─process
    │  │  BaseProcess.py
    │  │  ProcessManager.py
    │  │
    │  ├─lecture
    │  │  │  LectureCoreProcess.py
    │  │  │  LectureInfoProcess.py
    │  │  │  LecturePlanProcess.py
    │  │  │  LectureScanProcess.py
    │  │  │
    │  │  └─__pycache__
    │  │          LectureCoreProcess.cpython-311.pyc
    │  │          LectureInfoProcess.cpython-311.pyc
    │  │          LecturePlanProcess.cpython-311.pyc
    │  │          LectureScanProcess.cpython-311.pyc
    │  │
    │  ├─login
    │  │  │  LoginProcess.py
    │  │  │
    │  │  └─__pycache__
    │  │          LoginProcess.cpython-311.pyc
    │  │
    │  ├─start
    │  │  │  StartProcess.py
    │  │  │
    │  │  └─__pycache__
    │  │          StartProcess.cpython-311.pyc
    │  │
    │  └─__pycache__
    │          BaseProcess.cpython-311.pyc
    │          LoginProcess.cpython-311.pyc
    │          ProcessManager.cpython-311.pyc
    │          StartProcess.cpython-311.pyc
    │
    └─utils
        │  api.py
        │  Logger.py
        │  rawclassinfo.txt
        │
        └─__pycache__
                api.cpython-311.pyc
                logger.cpython-311.pyc

```
