-- Write an SQL query to swap all 'f' and 'm' values 
-- (i.e., change all 'f' values to 'm' and vice versa) with a single update statement and no intermediate temp table(s).

UPDATE Salary
SET 
   sex = CASE sex
         WHEN 'm' THEN 'f'
         ELSE 'm'
    END;
