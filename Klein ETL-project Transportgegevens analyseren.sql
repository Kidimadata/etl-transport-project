/*Toon alle gegevens uit de tabel transport_data
-- SELECT * FROM transport_data;*/


/* Hoeveel rijen met data bevat de tabel? 
SELECT COUNT(*) FROM transport_data;*/


/* Welke kolommen bevatten ontbrekende waarden? 
SELECT AVG("Total distance (km)")
FROM transport_data;*/


/* Welke ritten hebben de grootste afstanden? 
SELECT * FROM transport_data 
ORDER BY "Total distance (KM)" DESC;*/


/* Hoeveel ritten zijn er per type transport? 
SELECT "Transport dataset", COUNT(*)
FROM transport_data
GROUP BY "Transport dataset";*/