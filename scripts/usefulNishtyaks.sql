# ниже запросы для создания фильтров на дисциплины, которые буду участвовать в запросе на коэффициенты
# и просто полезные запросы

# дисциплины, за которые имеется больше N оценок
select name, count(*)
from new_marks
join new_disciplines d on new_marks.disciplines_id = d.disciplines_id
group by name
having count(*) > 9;

# группировка дисциплин с числами в названии (например, Математика 1.1, Математика 1.2 и пр)
# есть работающий код на питоне, который успешно гурппирует и пересчитывает средние баллы
select name, avgMark
from new_disciplines
    where avgMark is not null and
          (name like '%1%' or
          name like '%2%' or
          name like '%3%' or
          name like '%4%' or
          name like '%5%' or
          name like '%6%' or
          name like '%7%');

# группировка всех дисциплин про иностранные языки
# пока ничего с этим не сделали, но их тоже не мало
select distinct name
from new_disciplines
join new_marks m on new_disciplines.disciplines_id = m.disciplines_id
where mark is not null and name like '%язык%'
and name not like '%программ%'
and name not like '%языкознан%'
and name not like '%теор%'
and name not like '%прилож%'
and name not like '%древн%'
order by name;

# малочисленные дисциплины-старички, которых нет в учебны планах уже 5 лет (НА УДАЛЕНИЕ)
select distinct name, count(name)
from new_disciplines
inner join new_marks m on new_disciplines.disciplines_id = m.disciplines_id
where year in ('2009/2010', '2010/2011', '2011/2012', '2012/2013', '2013/2014', '2014/2015')
and year not in ('2019/2020', '2018/2019','2017/2018','2016/2017','2015/2016')
group by name
#having count(name) < 20
order by count(name) desc;

# дубликаты среди индикаторов
select code, description, count(description), count(code)
from new_indicators
group by description, code
having count(description) > 1;

# все группы бакалавров
select distinct major
from new_groups
where major like '%.03.%'
order by major;

# все имеющиеся в базе дисциплины на конкретное направление
select distinct new_disciplines.disciplines_id, name
from new_disciplines
inner join new_marks nm on new_disciplines.disciplines_id = nm.disciplines_id
inner join new_students ns on nm.students_id = ns.students_id
inner join new_groups ng on ns.groups_id = ng.groups_id
where major like '%12.03.01%' and avgMark is not null
order by name;

# все компетенции на конкретное направление
select distinct code
from new_students
inner join new_groups ng on new_students.groups_id = ng.groups_id
inner join new_marks nm on new_students.students_id = nm.students_id
inner join new_disciplines nd on nm.disciplines_id = nd.disciplines_id
inner join new_connection_of_disciplines_and_competencies ncodac on nd.disciplines_id = ncodac.disciplines_id
inner join new_competency nc on ncodac.competency_id = nc.id
where major like '%11.03.04%'
group by code
order by nc.code;

# дубликаты связей дисциплина-компетенция
select distinct nd.disciplines_id, code, count(code)
from new_connection_of_disciplines_and_competencies as ncodac
join new_competency nc on ncodac.competency_id = nc.id
join new_disciplines nd on ncodac.disciplines_id = nd.disciplines_id
where specialization like '%09.03.01%'
group by nd.disciplines_id, code
order by count(code) desc;

select distinct new_disciplines.disciplines_id
from new_disciplines
join new_marks nm on new_disciplines.disciplines_id = nm.disciplines_id
where avgMark is not null


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
          having count(new_marks.disciplines_id) > 9      # ограничение "больше 9 оценок за предмет", иначе скрипт долго работает
          )
    and new_disciplines.disciplines_id in
        (
            select new_disciplines.disciplines_id
            from new_marks
            join new_disciplines on new_marks.disciplines_id = new_disciplines.disciplines_id
            group by disciplines_id
            having count(new_marks.disciplines_id) > 9
            );