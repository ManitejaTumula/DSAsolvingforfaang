# Write your MySQL query statement below
select firstName,LastName,city,state
from person p
left join address a
on p.personid=a.personid