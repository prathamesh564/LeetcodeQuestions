CREATE TABLE Employee (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    salary INT NOT NULL,
    managerId INT,
    FOREIGN KEY (managerId) REFERENCES Employee(id)
);
INSERT INTO Employee (id, name, salary, managerId) VALUES
(1, 'Joe', 70000, 3),
(2, 'Henry', 80000, 4),
(3, 'Sam', 60000, NULL),
(4, 'Max', 90000, NULL);

select e.name as Employee
from Employee e
join Employee m
on e.managerid=m.id
where e.salary>m.salary;
