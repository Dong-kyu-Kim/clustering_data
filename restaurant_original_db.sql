CREATE TABLE restaurant_data (
    Name VARCHAR(30),
    Location VARCHAR(30),
    Cuisine VARCHAR(30),
    Rating FLOAT,
    Seating_Capacity INT,
    Average_Meal_Price FLOAT,
    Marketing_Budget FLOAT,
    Social_Media_Followers INT,
    Chef_Experience_Years INT,
    Number_of_Reviews INT,
    Avg_Review_Length FLOAT,
    Ambience_Score FLOAT,
    Service_Quality_Score FLOAT,
    Parking_Availability VARCHAR(15),
    Weekend_Reservations INT,
    Weekday_Reservations INT,
    Revenue FLOAT
);

SELECt * FROM restaurant_data;