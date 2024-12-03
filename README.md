# PCA and K-means-Based Clustering Analysis on Restaurant Dataset

Dataset: https://www.kaggle.com/datasets/anthonytherrien/restaurant-revenue-prediction-dataset/data 

![Original Features](https://github.com/user-attachments/assets/8a207187-d653-403e-b26c-7215229b89a8)

The restaurant dataset provided by Kaggle was utilized and stored in a database table named restaurant_data. The original dataset consists of 17 columns and 8368 rows. 

# Standardizing the Data

During the preprocessing stage, numerical variables were standardized by transforming them to have a mean of 0 and a standard deviation of 1. Categorical variables were converted into dummy variables using one-hot encoding and subsequently standardized. These two processed data frames were concatenated to form a final dataset with 24 columns and 8368 rows.

# Reducing the Dimensionality of Data Using PCA (Principal Component Analysis)

To reduce dimensionality, Principal Component Analysis (PCA) was applied, which condensed the 24 original features into 9 principal components. These 9 components explain approximately 81% of the total variance in the data, indicating that the essential information of the dataset was effectively retained during dimensionality reduction.

# Clustering

Using the reduced 9 principal components, K-means clustering was performed to determine the optimal number of clusters. While employing the Elbow Method, no clear point of inflection was identified. Therefore, the Calinski-Harabasz score was used for a more quantitative evaluation of clustering quality. The analysis revealed that the highest Calinski-Harabasz score was achieved with 2 clusters, and the score exhibited a declining trend as the number of clusters increased.

Specifically, the highest score with 2 clusters was 2072.745783, which is approximately 37% higher than the second-highest score of 1509.005237 observed with 3 clusters. This result indicates that 2 clusters provide the best clustering quality with the most distinct separation between clusters.

Finally, cluster labels generated from K-means clustering based on the 9 principal components were combined with the standardized data frame and stored in the database. This processed data can serve as a valuable resource for future analyses or modeling efforts.

#

We started first with restaurant review data pulled from Kaggle and our main objective was to develop and implement an unsupervised learning model to analyze and separate the data into two clusters for comparison. Ultimately with further iterations we would like to have the model determine "Go" or "Don't Go" for each restaurant. 

Using Jupyter Notebook we created the unsupervised model, loaded in our data set, standardized the data, and exported the resulting clusters into a sql file and into Tableau for visualization. 

Each of our visualizations aim to show the similarities and difference between the two clusters to begin to deterime which clusters would be "Go" vs. "Don't Go". 

Cluster Averages - Using the standardized data helps to ensure we can compare between variables, but does not help to give an overall picture of the data and real life applications. While the values of the averages themselves are arbitrary in a standardized set, the overall picture helps to show how the different items in the dataset are related and weighed. 

Standard Deviations - Between the two clusters we see more variability in the SD of the measures for Cluster 0 versus Cluster 1. Cluster 1 overall has a more consistent, but larger, standard deviation for each measure. In large, it appears that Cluster 1 has more “normal” distribution of the data and may help to indicate that these are the restaurants that should be included in the “Go” group.

Social Media - Both clusters show a positive relationship between Social Media Followers and Marketing Budget. There are indicators that businesses investing more in marketing efforts, tend to gain more followers on social media. While both clusters show similar results, Cluster 1 may reflect more substantial investments in marketing, contributing to an even greater increase in social media followers compared to Cluster 0.

Marketing Budget - Both clusters show a negative relationship between Marketing Budget and Revenue. As Marketing Budget increases, Revenue tends to decrease for both clusters, but the rate of decrease varies between them. Businesses in Cluster 0 may need to reassess their marketing strategies, as their higher marketing budget is not yielding revenue gains to match. Cluster 1 shows a more moderate decline in Revenue with increasing Marketing Budget, suggesting that marketing efforts might be more effective or have diminishing returns at a slower rate.

Weekend RSVPs and Meal Price - Both clusters show a negative relationship between Marketing Budget and Revenue. As Marketing Budget increases, Revenue tends to decrease for both clusters, but the rate of decrease varies between them. Businesses in Cluster 0 may need to reassess their marketing strategies, as their higher marketing budget is not yielding revenue gains to match. Cluster 1 shows a more moderate decline in Revenue with increasing Marketing Budget, suggesting that marketing efforts might be more effective or have diminishing returns at a slower rate.

Weekend RSVP and Ambience - Both clusters show a negative relationship between Marketing Budget and Revenue. As Marketing Budget increases, Revenue tends to decrease for both clusters, but the rate of decrease varies between them.
Businesses in Cluster 0 may need to reassess their marketing strategies, as their higher marketing budget is not yielding revenue gains to match. Cluster 1 shows a more moderate decline in Revenue with increasing Marketing Budget, suggesting that marketing efforts might be more effective or have diminishing returns at a slower rate.

Number of Reviews and Average Revenue - Both clusters have relatively even distribution between number of reviews and the correlated average revenue. The major difference between the clusters is the total revenue as a whole with Cluster 0 having a lower median value. Cluster 1 shows a larger standard deviation and more outliers than Cluster 0 at a higher median value


