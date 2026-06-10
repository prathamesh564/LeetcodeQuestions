CREATE TABLE Employee (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    salary INT NOT NULL,
    managerId INT,
)
select e.name as Employee
from Employee e
join Employee m
on e.managerid=m.id
where e.salary>m.salary
