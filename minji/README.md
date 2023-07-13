## 230712 :runner:
# MarkDown
![이미지 보이지 않을 때 문자열](이미지 주소) : 폴더 내 이미지 사용하려면 파일 이름으로 // 예시-(img/str.jpg)<br>

[나머지는 링크 참조](https://www.markdownguide.org/)<br>

# GitBash
ls : 리스트(파일 목록 조회)<br>
touch 파일이름 : 파일 생성<br>
mkdir 만들 폴더 이름 : 폴더 새로 생성<br>
cd **..** : 상위 폴더로 이동 (..대신 폴더이름 입력하면 그 위치로 이동)<br>
*주소 옆에 master 표시되야 함*

git init : 로컬 저장소 설정<br>
git **add** 파일 : staging area에 추가, . 입력 시 현재 경로에 있는 모든 파일 staging area로 이동<br>
git commit -m "메시지" : :exclamation:커밋시 메시지 반드시 필요:exclamation: / 작성자 정보도 필요<br>
git **push** -u *origin* master : 로컬저장소에서 원격 저장소로 연동하는 명령어<br>
(origin은 별칭이라서 다른 이름으로 변경 가능)<br>

순서 : add -> commit -> push (원격 저장소로 이동)<br>

---

## 230713 :running:
# gitHub :pushpin:
git **remote** add origin url : 로컬 저장소에 원격 저장소 주소 추가<br>
git **pull** (origin master) : 원격 저장소 주소 추가 이후 변경사항 업데이트 시 사용(괄호는 생략 가능)<br>
git **clone** url : 원격 저장소 전체 복제 (이미 git init 되어있음)

# gitIgnore
.gitignore 파일 생성 (확장자 없음)<br>
*이미 git 관리 받은 파일,디렉토리는 나중에 ignore에 작성해도 적용 안됌*<br>
[gitignore 사이트](https://www.toptal.com/developers/gitignore)
