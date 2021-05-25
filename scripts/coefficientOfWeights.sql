# коэффициент весов между дисциплинами
select smth.disciplines_id as 'dis_1', smth.avgMark as 'avg_1', new_disciplines.disciplines_id as 'dis_2', new_disciplines.avgMark as 'avg_2',
       smth.avgMark / new_disciplines.avgMark as 'coefficient'
from new_disciplines
cross join (
    select disciplines_id, avgMark
    from new_disciplines
    ) as smth
where new_disciplines.disciplines_id <> smth.disciplines_id and new_disciplines.avgMark is not null
    and smth.disciplines_id in
      (
          select new_disciplines.disciplines_id
          from new_marks
          join new_disciplines on new_marks.disciplines_id = new_disciplines.disciplines_id
          group by disciplines_id
          # having count(new_marks.disciplines_id) > 9      # ограничение "больше 9 оценок за предмет", иначе скрипт долго работает
          )
    and new_disciplines.disciplines_id in
        (
            select new_disciplines.disciplines_id
            from new_marks
            join new_disciplines on new_marks.disciplines_id = new_disciplines.disciplines_id
            group by disciplines_id
            # having count(new_marks.disciplines_id) > 9
            );