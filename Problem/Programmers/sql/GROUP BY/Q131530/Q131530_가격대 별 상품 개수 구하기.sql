-- 만원 단위로, 가격을 그룹화 해야 함
-- 0 ~ 9999원 안의 가격을 하나로 묶으려면 0부터 9999원 모두를 0으로 처리해야 함
-- 10000으로 나누고, 몫만 사용하기 = FLOOR(PRICE / 10000), 이후 만원 단위로 정리하기 위해서 * 10000
SELECT FLOOR(PRICE / 10000) * 10000 AS PRICE_GROUP,
COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP ASC