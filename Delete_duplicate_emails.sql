-- Self join

DELETE P1 FROM Person AS P1
INNER JOIN PERSON AS P2 
WHERE P1.id > P2.id AND P1.email = P2.email;  
