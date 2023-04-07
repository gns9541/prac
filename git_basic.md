# Git basic

- `git init`
  - 깃 레포 만들기
- `git add`
  - staging area에 추가
- `git commit -m {message}`
  - 커밋(기록 남기기)

- `git status`
  - 변경사항이 마지막 commit으로 부터 존재하나 상태 확인

- `git restore --staged ()`
  - stage로 ()를 내린다

- `git log --oneline`
  - 변경사항을 한눈에 본다

- `git remote add origin {url}`
  - local git 과 git hub 원격 연결
  
- `git remote -v`
  - 연결 확인
- ` git push origin master`
  - git hub에 올리기
  - `git push -u origin master`  
   
- `git config --global user.name {name}`
- `git config --global user.email{email`

- `git clone {url}`
  - 깃 허브에서 로컬로 가져오기
  
- `git clone {url}`
	- 깃허브에 있는 깃 새로 가져오기
- `git pull origin master`
	- 이미 연결된 상태에서 당겨오기


- vim .bash_profile 

- `git reset --hard {}`
  - head를 옮긴다
- `git reflog` 
  - 커밋들이 어떻게 변경됐는지