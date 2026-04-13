# Write your MySQL query statement below
delete from person
where id in (
    select id from (
        select id , email, Row_number() over (partition by email order by id) as rnk
        from person) a  where rnk>1
    )

