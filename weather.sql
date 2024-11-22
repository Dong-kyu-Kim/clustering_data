CREATE TABLE weather_cluster_label(
    cluster_id INT PRIMARY KEY,
    cluster INT
);

CREATE TABLE weather_scaled (
    id INT PRIMARY KEY,
    temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT,
    cloud_cover FLOAT,
    pressure FLOAT,
    no_rain BOOLEAN,
    rain BOOLEAN,
	FOREIGN KEY (id) REFERENCES weather_cluster_label(cluster_id) 
);

SELECT * FROM weather_cluster_label;

SELECT * FROM weather_scaled;

SELECT * FROM weather_scaled
JOIN weather_cluster_label
ON weather_scaled.id = weather_cluster_label.cluster_id;