SELECT FE.SCORE, FE.EMP_NO, HE.EMP_NAME, HE.POSITION, HE.EMAIL
FROM HR_EMPLOYEES HE JOIN (SELECT EMP_NO, SUM(SCORE) AS SCORE
                           FROM HR_GRADE
                           GROUP BY EMP_NO
                           ORDER BY SCORE DESC
                           LIMIT 1) AS FE 
                           ON HE.EMP_NO = FE.EMP_NO

-- RANK 활용
WITH GRADE_RANK AS (
    SELECT 
        EMP_NO, 
        SUM(SCORE) AS TOTAL_SCORE,
        RANK() OVER (ORDER BY SUM(SCORE) DESC) AS RNK -- 점수 순으로 순위 부여
    FROM HR_GRADE
    GROUP BY EMP_NO
)
SELECT 
    R.TOTAL_SCORE AS SCORE, 
    E.EMP_NO, 
    E.EMP_NAME, 
    E.POSITION, 
    E.EMAIL
FROM HR_EMPLOYEES E
JOIN GRADE_RANK R ON E.EMP_NO = R.EMP_NO
WHERE R.RNK = 1; -- 1위인 사람만 필터링