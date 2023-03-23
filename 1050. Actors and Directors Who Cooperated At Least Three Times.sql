select actor_id, director_id
from ActorDirector
group by actor_id, director_id, concat(actor_id, director_id)
having count(concat(actor_id, director_id)) >= 3
