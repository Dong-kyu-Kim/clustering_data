#!/usr/bin/env python
# coding: utf-8

# # Clustering Restaurant Data

# In[5]:


import pandas as pd
import hvplot.pandas
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, Birch


# # Load and Check the Dataset

# In[6]:


# Load the original dataset
restaurant_df = pd.read_csv(
    Path("./resources/restaurant_data.csv")
)

restaurant_df


# In[7]:


# Check the data
restaurant_df.info()


# # Standardize the Data

# In[8]:


# Normalize the data, scaling selected columns to a mean of 0 and a standard deviation of 1 
restaurant_df_scaled = StandardScaler().fit_transform(restaurant_df[["Rating", "Seating Capacity", "Average Meal Price",
                                                                     "Marketing Budget", "Social Media Followers",
                                                                     "Chef Experience Years", "Number of Reviews",
                                                                     "Avg Review Length", "Ambience Score", "Service Quality Score",
                                                                     "Weekend Reservations", "Weekday Reservations", "Revenue"]])

restaurant_df_scaled = pd.DataFrame(data = restaurant_df_scaled,
                                    columns = ["Rating", "Seating Capacity", "Average Meal Price",
                                              "Marketing Budget", "Social Media Followers",
                                              "Chef Experience Years", "Number of Reviews",
                                              "Avg Review Length", "Ambience Score", "Service Quality Score",
                                              "Weekend Reservations", "Weekday Reservations", "Revenue"])

restaurant_df_scaled


# In[9]:


# Convert categorical variable into dummy/indicator variables.
dummies_df = pd.get_dummies(restaurant_df[["Location", "Cuisine", "Parking Availability"]])

# Concatenate "restaurant_df_scaled" data and "dummies_df" data
restaurant_df_converted = pd.concat([restaurant_df_scaled, dummies_df], axis = 1)
restaurant_df_converted.to_csv(Path("./exported_resources/restaurant_df_scaled.csv", header = True))
restaurant_df_converted


# In[10]:


# Check the data
restaurant_df_converted.info()


# # Reducing the Dimensionality of Data Using PCA (Principal Component Analysis)

# In[11]:


# Reducing the Dimensionality of Data Using PCA
pca = PCA(n_components = 9)
restaurant_pca_df = pca.fit_transform(restaurant_df_converted)
restaurant_pca_df = pd.DataFrame(data = restaurant_pca_df, 
                                columns = ["PCA_1", "PCA_2", "PCA_3", "PCA_4", 
                                           "PCA_5", "PCA_6", "PCA_7", "PCA_8", "PCA_9"])
restaurant_pca_df


# In[12]:


# Check the reduced 9 principal components variance ratio
variance_ratio = sum(pca.explained_variance_ratio_) * 100
print(f"The 24 original features were reduced to 9 principal components, capturing approximately {round(variance_ratio, 2)}% of total variance.")


# # Determining the Number of Clusters

# In[13]:


import warnings

warnings.filterwarnings("ignore")

# Determine the number of clusters using elbow method
inertia = []
cluster_list = list(range(1, 41))

for clusters in cluster_list:
    k_model = KMeans(n_clusters = clusters, random_state = 1)
    k_model.fit(restaurant_pca_df)
    inertia.append(k_model.inertia_)

elbow = {
    "cluster_num": cluster_list,
    "inertia": inertia
}

# Visualize elbow method
elbow_df = pd.DataFrame(data = elbow)

elbow_df.hvplot.line(
    x = "cluster_num",
    y = "inertia",
    title = "Elbow Method",
    xticks = cluster_list,
    alpha = 0.7,
    color = 'red'
)


# In[14]:


print("Since the optimal number of clusters is not clearly identifiable, I will rely on the Calinski-Harabasz score for determination.")


# In[15]:


# Determine the number of clusters using Calinski-Harabasz score
scores = []
cluster_list = list(range(2, 41))

for clusters in cluster_list:
    k_model = KMeans(n_clusters = clusters, random_state = 1)
    k_model.fit(restaurant_pca_df)
    labels = k_model.labels_
    score = metrics.calinski_harabasz_score(restaurant_pca_df, labels)
    scores.append(score)

cluster_scores = {
    "cluster_num": cluster_list,
    "Calinski Harabasz Score": scores
}

# Make a dataframe of Calinski Harabasz Score
scores_df = pd.DataFrame(data = cluster_scores)
scores_df


# In[16]:


# Visualize the Calinski-Harabasz score
plt.figure(figsize = (10, 4))
plt.bar(scores_df["cluster_num"], scores_df["Calinski Harabasz Score"], color = 'blue', alpha = 0.3)
plt.xticks(cluster_list)
plt.title("Calinski Harabasz Score by Cluster Numbers")
plt.xlabel("Cluster Numbers")
plt.ylabel("Calinski Harabasz Score")
plt.tight_layout()

plt.show()


# In[17]:


print("The optimal number of clusters appears to be 2.")


# # Segment the Data Using the K-means Algorithm

# In[18]:


# Segment the Data Using the K-means Algorithm
k_model = KMeans(n_clusters = 2, random_state = 1)
k_model.fit(restaurant_pca_df)
cluster = k_model.predict(restaurant_pca_df)

# Create cluster dataframe
cluster_df = pd.DataFrame(data = cluster, columns = ["Cluster"])
cluster_df.to_csv(Path("./exported_resources/restaurant_cluster_label_df.csv"), header = True)
cluster_df


# In[19]:


# Concatenate the "restaurant_pca_df" dataframe and "cluster_df" dataframe
pca_clustered_df = pd.concat([restaurant_pca_df, cluster_df], axis = 1)
pca_clustered_df


# In[20]:


# Concatenate the "restaurant_df_converted" (scaled data) dataframe and "cluster_df" dataframe
restaurant_df_scaled_clustered = pd.concat([restaurant_df_converted, cluster_df], axis = 1)
restaurant_df_scaled_clustered


# In[21]:


# Check the dataframe
restaurant_df_scaled_clustered.info()


# # PCA and K-means-Based Clustering Analysis on Restaurant Dataset

# The restaurant dataset provided by Kaggle was utilized and stored in a database table named restaurant_data. The original dataset consists of 17 columns and 8368 rows.
# 
# During the preprocessing stage, numerical variables were standardized by transforming them to have a mean of 0 and a standard deviation of 1. Categorical variables were converted into dummy variables using one-hot encoding and subsequently standardized. These two processed data frames were concatenated to form a final dataset with 24 columns and 8368 rows.
# 
# To reduce dimensionality, Principal Component Analysis (PCA) was applied, which condensed the 24 original features into 9 principal components. These 9 components explain approximately 81% of the total variance in the data, indicating that the essential information of the dataset was effectively retained during dimensionality reduction.
# 
# Using the reduced 9 principal components, K-means clustering was performed to determine the optimal number of clusters. While employing the Elbow Method, no clear point of inflection was identified. Therefore, the Calinski-Harabasz score was used for a more quantitative evaluation of clustering quality. The analysis revealed that the highest Calinski-Harabasz score was achieved with 2 clusters, and the score exhibited a declining trend as the number of clusters increased.
# 
# Specifically, the highest score with 2 clusters was 2072.745783, which is approximately 37% higher than the second-highest score of 1509.005237 observed with 3 clusters. This result indicates that 2 clusters provide the best clustering quality with the most distinct separation between clusters.
# 
# Finally, cluster labels generated from K-means clustering based on the 9 principal components were combined with the standardized data frame and stored in the database. This processed data can serve as a valuable resource for future analyses or modeling efforts.

# In[ ]:




