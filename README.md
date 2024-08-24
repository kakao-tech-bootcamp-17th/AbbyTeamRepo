# 카테부 실습 과제  
---

### Git 사용법
<b>Forked Repository에 Push</b>

0. 현재 git branch 확인
1. 오늘 날짜 branch 생성
2. 해당 branch 이동
3. git add, commit, push 진행
```
git branch
git branch MMDD
git checkout MMDD
git add .
git commit -m "commit message"
git push origin MMDD
```

<b>Origin Repository에 Pull & Request</b>

0. 해당 Forked Repo Github 사이트 들어가기
(https://github.com/abby-kimm/KTB_Abby) 
1. Open Pull & Request
2. Reviewer 지정
3. Pull & Request
4. Merge Request

<b>Forked Repository의 Main Branch 갱신</b>
1. Sync fork 누르고 Update
2. 터미널에서 브랜치 삭제
3. Origin Repo에서 Pull 땡겨와서 Forked Repository 업데이트
```
git checkout main
git branch -D MMDD
git pull origin main
```

* Origin (Parent) Repo: kakao-tech-bootcamp-17th/KTB_Abby