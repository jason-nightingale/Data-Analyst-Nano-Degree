/*This project we will be trending my local Kansas City weather data compared to
global trends by year. Per project specs, we first need to do a lookup in
the city_list table to locate a city nearest me. Then pull the data from
the city_data table for the located city and order by year. Finally, we
will pull all city_data from the global_data table and order by year.*/

/*Start by searching the city_list to find the city nearest me*/
SELECT *
FROM city_list
where country LIKE '%nited%' AND country LIKE '%tates'
order by country, city;
/*The closest city near me is 'Kansas City'*/

/*Use 'Kansas City' for pulling the city_data. Make sure to keep and eye
on punctuation by using wildcards.*/
SELECT *
FROM city_data
where (city LIKE '%ansas%' AND city LIKE '%ity') AND (year BETWEEN 1781 AND 2013)
order by year;

/*Pull all data from global_data order by year.*/
SELECT *
FROM global_data
WHERE year BETWEEN 1781 AND 2013
order by year;
