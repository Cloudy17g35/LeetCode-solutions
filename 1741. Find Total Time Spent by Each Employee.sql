SELECT event_day day, emp_id, sum(out_time) - sum(in_time) total_time
  FROM employees
 GROUP BY event_day, emp_id
