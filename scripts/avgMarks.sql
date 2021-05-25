# 1
select distinct new_marks.disciplines_id,
                round(avg(mark), 3) as 'Средняя оценка'
from new_marks
join new_disciplines on new_marks.disciplines_id = new_disciplines.disciplines_id
where mark REGEXP '^-?[0-9]+$'
group by new_marks.disciplines_id;
# 2
select distinct new_marks.disciplines_id,
                round(avg(CONVERT(SUBSTRING_INDEX(mark,'-',-1),UNSIGNED INTEGER)),3)
from new_marks
join new_disciplines on new_marks.disciplines_id = new_disciplines.disciplines_id
where mark REGEXP '^-?[0-9]+$'
group by new_marks.disciplines_id;
# заполнение средней оценки по дисциплине
UPDATE new_disciplines
JOIN (
        select distinct new_marks.disciplines_id as 'id',
                        round(avg(mark), 3) as 'avgMark'
        from new_marks
        join new_disciplines on new_marks.disciplines_id = new_disciplines.disciplines_id
        group by new_marks.disciplines_id)
    AS temp
    ON new_disciplines.disciplines_id = temp.id
SET new_disciplines.avgMark = temp.avgMark;