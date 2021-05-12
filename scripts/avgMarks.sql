select distinct disciplines.name,
                round(avg(mark), 3) as 'Средняя оценка'
from marks
join disciplines on marks.disciplines_id = disciplines.disciplines_id
where mark REGEXP '^-?[0-9]+$'
group by name;