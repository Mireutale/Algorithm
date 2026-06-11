# AGENTS.md

## 커밋 작성 규칙

커밋 메시지는 Conventional Commits 형식을 사용합니다.

```text
<type>: <summary>
```

요약은 짧게 작성하고, 기본적으로 한국어를 사용합니다.

## 커밋 타입

- `feat`: 새로운 문제 풀이를 추가하거나, 기존 문제에 새 언어/버전 풀이를 추가할 때 사용합니다.
- `fix`: 오답 풀이, 실행 설정 오류, 의미가 바뀌는 오탈자, 저장소 설정 문제를 수정할 때 사용합니다.
- `refactor`: 풀이 동작은 바꾸지 않고 파일 구조, 폴더명, 코드 구조를 정리할 때 사용합니다.
- `docs`: README, 풀이 설명, 주석 등 문서만 수정할 때 사용합니다.
- `chore`: 저장소 관리용 변경, 생성물 정리, 기타 유지보수성 변경에 사용합니다.

## 커밋 메시지 예시

```text
feat: 리트코드 Q1 Java_v1 풀이 추가
feat: 백준 1000 Python_v1 풀이 추가
fix: Q1 Two Sum Java 실행 설정 수정
refactor: 문제별 Java 버전 폴더 구조 정리
docs: README 사용 언어 배지 수정
chore: 불필요한 class 파일 제거
```

## 커밋 전 확인 사항

- 서로 관련 있는 변경만 하나의 커밋에 묶습니다.
- 특별한 이유가 없다면 생성된 `.class` 파일은 커밋하지 않습니다.
- 문제 폴더와 풀이 파일명은 `Q문제번호` 형식을 사용합니다.
- 문제 설명 파일은 `README.md` 대신 `Q문제번호.md` 형식을 사용합니다.
- Java 풀이는 `Java_v1/`처럼 버전 폴더 안에 소스 파일을 둡니다.
- 로컬 실행 코드가 필요하면 `Main.java`와 `Solution.java`를 분리합니다.
- 가능하면 커밋 전에 해당 풀이를 한 번 실행해 확인합니다.

## 권장 폴더 및 파일명 규칙

Programmers Python 풀이는 다음 형식을 사용합니다.

```text
Problem/Programmers/python/Q42586/
  Q42586.md
  Q42586_기능개발.py
```

Programmers SQL 풀이는 카테고리 폴더 아래에 다음 형식을 사용합니다.

```text
Problem/Programmers/sql/SELECT/Q276013/
  Q276013.md
  Q276013_Python 개발자 찾기.sql
```

Baekjoon 풀이는 기존 분류 폴더 아래에 문제별 폴더를 둡니다. 기존에 설명 파일이 없던 문제는 새 설명 파일을 만들지 않습니다.

```text
Problem/Baekjoon/Solved/class1/Q1000/
  Q1000.py

Problem/Baekjoon/Barkingdog/17.그리디/Q11399/
  Q11399.md
  Q11399_ATM.py
```

Java 풀이는 버전별 폴더를 사용합니다.

```text
Problem/LeetCode/Q1_TwoSum/
  Java_v1/
    Main.java
    Solution.java
```

Java 컴파일 결과물인 `bin/` 폴더와 `.class` 파일은 GitHub에 포함하지 않습니다. 소스의 기준은 항상 `.java` 파일입니다.
