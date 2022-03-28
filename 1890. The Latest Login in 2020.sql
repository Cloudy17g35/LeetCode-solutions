SELECT user_id, max(time_stamp) last_stamp
from  logins
WHERE YEAR(time_stamp) = 2020
GROUP BY user_id;
