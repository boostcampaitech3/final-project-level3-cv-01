## Prerequisite

- react v18.1.0
- Node.js v16.15.0
- npm v8.5.5
- npx v8.5.5
- Package : package.json 참고

## Usage
### npm 초기화
```
npm init
```
### git clone
```
git clone https://github.com/boostcampaitech3/final-project-level3-cv-01.git
```
### react start
```
cd frontend
npm install
npm start
```

## Directory
```bash
app
├── public
│   ├── index.html
│   └── manifest.json
├── src
│   ├── components
│   │    ├── Home
│   │    │    └── Home.jsx
│   │    ├── Log
│   │    │    ├── Log.jsx
│   │    │    ├── LogBox.jsx
│   │    │    └── LogDateBox.jsx
│   │    ├── LogDetail
│   │    │    └── LogDetail.jsx
│   │    ├── Login
│   │    │    └── Login.jsx
│   │    └── Navigator
│   │    │    └── Navigator.jsx
│   ├── App.js
│   ├── index.css
│   └── index.js
├── package.json
├── package-lock.json
└── README.md
```
## Files

#### LogDetail.jsx
- 로그 페이지에서 각 박스 아래에 있는 상세정보 버튼 클릭 시 나오는 Component

#### LogBox.jsx
- 로그 Page에서 생성되는 로그 Box Component

#### LogDateBox.jsx
- LogBox(Detection 각 로그 Box Component), LogDetail(상세정보 page) 모두 사용되는 날짜 Select Box Component