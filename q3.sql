SELECT Name
FROM Salesperson
WHERE Salesperson.ID in (
	SELECT salesperson_id
	FROM Orders
	GROUP BY salesperson_id
	HAVING ( COUNT(salesperson_id) > 1)
)