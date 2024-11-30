#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# In[2]:


# Load the csv file
cluster_df = pd.read_csv(
    Path("./exported_resources/restaurant_scaled_and_clustered.csv")
)

cluster_df


# In[3]:


# Check the dataframe
cluster_df.info()


# # Export the Cluster 0 Features

# In[4]:


# Export to csv file average of cluster 0
cluster_0 = cluster_df.loc[cluster_df["cluster"] == 0, "rating":"parking_availability_yes"]
cluster_0_avg = pd.DataFrame(cluster_0.mean())
cluster_0_avg = cluster_0_avg.transpose()
cluster_0_avg.to_csv(Path("./exported_resources/cluster_0_avg.csv"))
cluster_0_avg


# In[5]:


# Export to csv file standard deviation of cluster 0
cluster_0_std = pd.DataFrame(cluster_0.std())
cluster_0_std = cluster_0_std.transpose()
cluster_0_std.to_csv(Path("./exported_resources/cluster_0_std.csv"))
cluster_0_std


# # Export the Cluster 1 Features

# In[6]:


# Export to csv file average of cluster 1
cluster_1 = cluster_df.loc[cluster_df["cluster"] == 1, "rating":"parking_availability_yes"]
cluster_1_avg = pd.DataFrame(cluster_1.mean())
cluster_1_avg = cluster_1_avg.transpose()
cluster_1_avg.to_csv(Path("./exported_resources/cluster_1_avg.csv"))
cluster_1_avg


# In[7]:


# Export to csv file standard deviation of cluster 1
cluster_1_std = pd.DataFrame(cluster_1.std())
cluster_1_std = cluster_1_std.transpose()
cluster_1_std.to_csv(Path("./exported_resources/cluster_1_std.csv"))
cluster_1_std


# In[ ]:




