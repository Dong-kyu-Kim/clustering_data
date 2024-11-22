CREATE TABLE restaurant_cluster_label (
    cluster_id INT PRIMARY KEY,
    cluster INT
);

CREATE TABLE restaurant_scaled (
    id INT PRIMARY KEY,
    rating FLOAT,
    seating_capacity FLOAT,
    average_meal_price FLOAT,
    marketing_budget FLOAT,
    social_media_followers FLOAT,
    chef_experience_years FLOAT,
    number_of_reviews FLOAT,
    avg_review_length FLOAT,
    ambience_score FLOAT,
    service_quality_score FLOAT,
    weekend_reservations FLOAT,
    weekday_reservations FLOAT,
    revenue FLOAT,
    location_downtown BOOLEAN,
    location_rural BOOLEAN,
    location_suburban BOOLEAN,
    cuisine_american BOOLEAN,
    cuisine_french BOOLEAN,
    cuisine_indian BOOLEAN,
    cuisine_italian BOOLEAN,
    cuisine_japanese BOOLEAN,
    cuisine_mexican BOOLEAN,
    parking_availability_no BOOLEAN,
    parking_availability_yes BOOLEAN,
    FOREIGN KEY (id) REFERENCES restaurant_cluster_label(cluster_id)
);

SELECT * FROM restaurant_cluster_label;

SELECT * FROM restaurant_scaled;

SELECT * FROM restaurant_cluster_label
JOIN restaurant_scaled
ON restaurant_cluster_label.cluster_id = restaurant_scaled.id;