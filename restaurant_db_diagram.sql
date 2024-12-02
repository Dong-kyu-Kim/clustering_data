-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/QM63T2
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "restaurant_cluster_label" (
    "cluster_id" INT   NOT NULL,
    "cluster" INT   NOT NULL,
    CONSTRAINT "pk_restaurant_cluster_label" PRIMARY KEY (
        "cluster_id"
     )
);

CREATE TABLE "restaurant_scaled" (
    "id" INT   NOT NULL,
    "rating" FLOAT   NOT NULL,
    "seating_capacity" FLOAT   NOT NULL,
    "average_meal_price" FLOAT   NOT NULL,
    "marketing_budget" FLOAT   NOT NULL,
    "social_media_followers" FLOAT   NOT NULL,
    "chef_experience_years" FLOAT   NOT NULL,
    "number_of_reviews" FLOAT   NOT NULL,
    "avg_review_length" FLOAT   NOT NULL,
    "ambience_score" FLOAT   NOT NULL,
    "service_quality_score" FLOAT   NOT NULL,
    "weekend_reservations" FLOAT   NOT NULL,
    "weekday_reservations" FLOAT   NOT NULL,
    "revenue" FLOAT   NOT NULL,
    "location_downtown" BOOLEAN   NOT NULL,
    "location_rural" BOOLEAN   NOT NULL,
    "location_suburban" BOOLEAN   NOT NULL,
    "cuisine_american" BOOLEAN   NOT NULL,
    "cuisine_french" BOOLEAN   NOT NULL,
    "cuisine_indian" BOOLEAN   NOT NULL,
    "cuisine_italian" BOOLEAN   NOT NULL,
    "cuisine_japanese" BOOLEAN   NOT NULL,
    "cuisine_mexican" BOOLEAN   NOT NULL,
    "parking_availability_no" BOOLEAN   NOT NULL,
    "parking_availability_yes" BOOLEAN   NOT NULL,
    CONSTRAINT "pk_restaurant_scaled" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "restaurant_scaled" ADD CONSTRAINT "fk_restaurant_scaled_id" FOREIGN KEY("id")
REFERENCES "restaurant_cluster_label" ("cluster_id");

