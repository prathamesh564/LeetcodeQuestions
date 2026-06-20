select c.name as Customers
from Customers c
LEFT join Orders o on c.id=o.CustomerId
where o.id is Null
