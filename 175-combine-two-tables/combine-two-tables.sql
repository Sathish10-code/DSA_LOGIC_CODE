# Write your MySQL query statement below
select p.firstName,p.lastname,a.city,a.state 
from address a right join person p on p.personid=a.personid