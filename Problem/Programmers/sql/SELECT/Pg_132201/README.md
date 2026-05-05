# 132201, 12세 이하인 여자 환자 목록 출력하기

- CASE를 활용해서 조건을 설정할 수 있음
  - ```
    CASE
        WHEN [COL] IS [condition] THEN [return]
        ELSE [return_not]
    END AS COL_NAME
    ```
  - 위 조건으로 COL의 상태가 참이면 return을 출력하고, 아닌 경우 return_not을 출력함.
  - 마지막으로 COL_NAME으로 이름을 설정