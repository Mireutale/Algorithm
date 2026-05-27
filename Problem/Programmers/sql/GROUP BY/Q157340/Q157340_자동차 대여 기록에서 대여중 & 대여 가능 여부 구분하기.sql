-- Table: CAR_RENTAL_COMPANY_RENTAL_HISTORY
-- Att: HISTORY_ID, CAR_ID, START_DATE, END_DATE

-- 직관적인 코드
SELECT CAR_ID, CASE
                WHEN CAR_ID IN (
                    SELECT CAR_ID 
                    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                    WHERE '2022-10-16' BETWEEN START_DATE AND END_DATE
                ) THEN '대여중'
                ELSE '대여가능'
               END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC

-- MAX 활용, 한글 순서상 '대여중'이 '대여가능'보다 뒤에 있으므로, MAX를 활용해서 '대여중'이 하나라도 있으면 대여 중을 우선시 하도록
SELECT CAR_ID,  
       MAX(CASE 
            WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE THEN '대여중'
            ELSE '대여가능'
           END) AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;
