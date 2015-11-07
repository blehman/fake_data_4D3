
#Fake Data
This is simply available for visualization practice b/c it represents
some interesting challenges. The clusterID in the last column of the
line\_counts\_clusterID.csv aligns with the results; however, the results does not contain all of
the same keys.  

###Fake Data Structure
1.  line_counts_clusterID.csv - the last column is the cluster label.
    The preceeding 14 columns are boolean values that represent the
presences of some features.  
2.  cluster\#\_results - additional information for each cluster that
    provides details on the following:
  * Gender
  * Language
  * Interests
  * TV Genre
  * TV Show
  * Location: Country
  * Location: Region
  * Location: Metro
  * Device Category
  * Device Wireless Network

###Fake Data Visualization & Analysis
What is possible?

Analysis:  
1. Multinomial Logistic Regression

Visualization:
1. % Presence of each feature per each label.
2. Difference from the mean count of each item per each cluster.

