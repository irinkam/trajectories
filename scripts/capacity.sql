-- трудоемкость индикатора
select new_disciplines_indicators.indicators_id,
       sum(new_disciplines.capacity)
from new_disciplines
join new_disciplines_indicators new_disciplines_indicators on new_disciplines.disciplines_id = new_disciplines_indicators.disciplines_id
group by new_disciplines_indicators.indicators_id;

update new_indicators
join    (select new_disciplines_indicators.indicators_id,
                sum(new_disciplines.capacity) as capacity
        from new_disciplines
        join new_disciplines_indicators new_disciplines_indicators on new_disciplines.disciplines_id = new_disciplines_indicators.disciplines_id
        group by new_disciplines_indicators.indicators_id) as tableA on tableA.indicators_id = new_indicators.id
set new_indicators.capacity = tableA.capacity
where new_indicators.id = tableA.indicators_id;

-- трудоемкость компетенции
select  new_competency.id,
        sum(new_indicators.capacity)
from new_competency
join new_indicators on new_competency.id = new_indicators.comp_id
group by new_competency.id
having sum(new_indicators.capacity) is not null

update new_competency
join    (select  new_competency.id,
                sum(new_indicators.capacity) as capacity
        from new_competency
        join new_indicators on new_competency.id = new_indicators.comp_id
        group by new_competency.id
        having sum(new_indicators.capacity) is not null) as tableA on tableA.id = new_competency.id
set new_competency.capacity = tableA.capacity
where new_competency.id = tableA.id;

-- относительная трудоемкость индикатора
update new_indicators
join
        (select new_competency.id,
               new_indicators.id as indicator_id,
               new_indicators.capacity/new_competency.capacity as weight
        from new_indicators
        join new_competency on new_indicators.comp_id = new_competency.id
        where new_indicators.capacity/new_competency.capacity is not null) as tableA on tableA.indicator_id = new_indicators.id
set new_indicators.weight = tableA.weight
where new_indicators.id = tableA.indicator_id;

-- нормирование оценки (относительная оценка)
update new_marks
set relative_mark = new_marks.mark/5
where new_marks.relative_mark is null;

-- относительный уровень освоения индикатора компетенции студентом
select tableA.disciplines_id,
       sum(tableA.weight) * new_marks.relative_mark
from new_indicators
join new_disciplines_indicators on new_indicators.id = new_disciplines_indicators.indicators_id
join new_disciplines on new_disciplines_indicators.disciplines_id = new_disciplines.disciplines_id
join new_marks on new_disciplines.disciplines_id = new_marks.disciplines_id
join (select new_disciplines.disciplines_id,
                ni.id as indicator_id,
                new_disciplines.capacity / ni.capacity as weight
        from new_disciplines
        join new_disciplines_indicators ndi on new_disciplines.disciplines_id = ndi.disciplines_id
        join new_indicators ni on ndi.indicators_id = ni.id
        where new_disciplines.capacity / ni.capacity is not null) as tableA on tableA.disciplines_id = new_disciplines.disciplines_id
group by new_marks.relative_mark, tableA.weight, tableA.disciplines_id;