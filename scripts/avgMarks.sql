# 1
select distinct marks.disciplines_id,
                round(avg(mark), 3) as 'Средняя оценка'
from marks
join disciplines on marks.disciplines_id = disciplines.disciplines_id
where mark REGEXP '^-?[0-9]+$'
group by marks.disciplines_id;
# 2
select distinct marks.disciplines_id,
                round(avg(CONVERT(SUBSTRING_INDEX(mark,'-',-1),UNSIGNED INTEGER)),3)
from marks
join disciplines on marks.disciplines_id = disciplines.disciplines_id
where mark REGEXP '^-?[0-9]+$'
group by marks.disciplines_id;
