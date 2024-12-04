#!/usr/bin/env python
# coding: utf-8

# # Clustering Restaurant Data

# In[23]:


pip install seaborn


# In[44]:


import pandas as pd
import hvplot.pandas
import seaborn as sns
import matplotlib.pyplot as plt


# # Correlation Heatmap

# In[45]:


df_correlation = pd.read_csv(
    Path("./exported_resources/restaurant_scaled_and_clustered.csv")
)

df_correlation.head(5)


# In[46]:


# Compute the correlation matrix
correlation_matrix = df_correlation.corr()

# Display the correlation matrix
print(correlation_matrix)


# In[47]:


# Set the size of the heatmap
plt.figure(figsize = (10, 8))

# Create the heatmap
sns.heatmap(correlation_matrix, annot = True, fmt = '.2f', cmap = 'coolwarm', cbar = True)

# Add a title
plt.title('Correlation Heatmap', fontsize = 16)

# Show the heatmap
plt.show()


# In[ ]:




