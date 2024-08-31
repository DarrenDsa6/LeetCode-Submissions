
SELECT 
    firstName AS firstname, 
    lastName AS lastname, city, state
FROM 
    Person 
LEFT JOIN 
    Address 
ON 
    Person.personId = Address.personId;

