# 284531_노선별 평균 역 사이 거리 조회하기

- TOTAL_DISTANCE를 CONCAT을 활용해서 문자열을 붙였기 때문에, ORDER BY에서 TOTAL_DISTANCE를 그냥 사용하면 문자열 비교가 되는 문제가 생김
  - 따라서, SUM(D_BETWEEN_DIST)를 그대로 써야함