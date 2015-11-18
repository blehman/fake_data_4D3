#Fake Data
This is simply available for visualization practice b/c it represents
some interesting challenges. The clusterID in the last column of the
line\_counts\_clusterID.csv aligns with the results; however, the results do not contain all of
the same keys.  

Huge thanks to @zanstrong for the drawings and brainstorming! Also, thanks to @s1nelson, @micahstubbs, @shirleyxywu and @enjalot for all of the thinking with me!  

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
1. Multinomial Logistic Regression (thanks @s1nelson)
2. t-SNE (thanks @micahstubbs)

Visualization:  
1. % Presence of each feature per each label.
  * Heatmap (thanks @zanstrong)
    * click merge on feature selection
    * option to remove feature
    * separation between heatmap rows to indication disctions
2. How do the users arrive at the label?
  * Node path ()
    * Similar to a decision tree to showcase paths by which tweets receive a
      label.
  * [Parallel Coordinates](http://bl.ocks.org/jasondavies/1341281) (thanks @shirleyxywu and @enjalot)
    * Turn on/off labels
    * Forground/Background colors instead of 14 different colors
    * Opacity for selected labels
    * randomly arround the feature ordering.
  * [Crossfilter](http://square.github.io/crossfilter/) (thanks @enjalot).
  * The @zanstrong technique:

3. Difference from the mean count of each item per each cluster.


