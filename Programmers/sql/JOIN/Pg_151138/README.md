# 151138_자동차 대여 기록에서 장기&단기 대여 구분하기

- 날짜간의 일 수의 차이는 DATEDIFF함수를 활용
  - DATEDIFF(expr1, expr2)를 수행하면, expr1-expr2를 계산한다.
    - expr1~expr2의 일자를 알고싶다면 DATEDIFF(expr2, expr1) + 1를 해줘야, expr2의 당일날 도 포함된다.