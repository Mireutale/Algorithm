# 301651_멸종위기의 대장균 찾기

- 세대별로 재귀를 사용해서, 세대를 구분
  - 이를 UNION ALL을 활용해서, 연속해서 찾은 값들을 하나로 이어 붙임(중복 허용)

- 이제, 새롭게 만든 GENERATION에서 세대를 구분해야 함
```

    (SELECT PARENT_ID
    FROM ECOLI_GENERATION
    WHERE PARENT_ID IS NOT NULL) AS SUBQUERY
```
- 이 구문을 활용해서, 부모 ID를 전부 추출
  - 이후, WHERE ID NOT IN SUBQUERY를 활용
  - 부모 ID에 포함되지 않는 모든 ID를 추출
  - 세대별 갯수를 세야하므로 GROUP BY GENERATION을 해서 개수를 구해야 함