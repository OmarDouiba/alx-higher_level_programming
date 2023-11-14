--  script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, (SUM(value) / COUNT(city)) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
