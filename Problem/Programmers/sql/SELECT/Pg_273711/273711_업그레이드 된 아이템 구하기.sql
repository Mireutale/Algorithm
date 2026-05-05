-- ITEM_INFO
-- ITEM_ID, ITEM_NAME, RARITY, PRICE
-- ITEM_TREE
-- ITEM_ID, PARENT_ITEM_ID

## JOIN을 활용한 방식
# SELECT T.ITEM_ID, I.ITEM_NAME, I.RARITY
# FROM ITEM_TREE T
# -- I와 T를 합쳐서 각 아이템의 정보를 모두 불러옴
# JOIN ITEM_INFO I ON T.ITEM_ID = I.ITEM_ID    
# -- P를 활용해서, 부모의 아이템 정보도 불러옴
# JOIN ITEM_INFO P ON T.PARENT_ITEM_ID = P.ITEM_ID 
# WHERE P.RARITY = 'RARE' -- 부모 등급이 'RARE'인 경우만 찾아서 아이템을 추출
# ORDER BY T.ITEM_ID DESC;

## Subquery를 활용한 방식
SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO
WHERE ITEM_ID IN (
    -- 해당 아이템으로 업그레이드가 가능한 아이템 목록을 추출
    SELECT ITEM_ID
    FROM ITEM_TREE
    WHERE PARENT_ITEM_ID IN (
        -- 희귀도가 RARE인 아이템을 추출
        SELECT ITEM_ID
        FROM ITEM_INFO
        WHERE RARITY = 'RARE'))
ORDER BY ITEM_ID DESC;