# Write your MySQL query statement below
select ee.unique_id, e.name from employees e left join employeeUNI ee on e.id = ee.id