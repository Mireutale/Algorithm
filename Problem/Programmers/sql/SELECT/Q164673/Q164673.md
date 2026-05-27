# 164673, 조건에 부합하는 중고거래 댓글 조회하기

- 2022년 10월 데이터를 찾기위해서 아래 3가지 방법을 쓸 수 있다.
  - 가장 간단한 코드
    - WHERE B.CREATED_DATE LIKE '2022-10%'
  - 가독성이 좋은 코드
    - WHERE YEAR(B.CREATED_DATE) = 2022 AND MONTH(B.CREATED_DATE) = 10
  - 성능이 가장 우수한 코드
    - WHERE B.CREATED_DATE >= '2022-10-01' AND B.CREATED_DATE < '2022-11-01'