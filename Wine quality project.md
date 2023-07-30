# Wine quality dataset visualization and data cleaning

* In this project we are gonna work with a dataset of white and red wine and we are going to use it to answer this 4 primary questions
along other questions scattered across the project 

# Is a certain type of wine (red or white) associated with higher quality?
# Do wines with higher alcoholic content receive better ratings?
# Do sweeter wines (more residual sugar) receive better ratings?
# What level of acidity is associated with the highest quality?

First we read the csv files of both red and white wine and we analyze their shape and type of data, this time i had some problems with the dataset so i had 
to use excel to find bad placed decimal points in the file, so after exploring and changing the regional decimal symbol and replacing the commas 
for points i could change it to numerical values, but i needed to delete some high numerial values that did not relate to the normal values of the 
dataset from python

After checking for data cleaning i finally put together the two datasets so i could have only one with both wines
and then used the np.repeat command to separate them by color and make a new column to classify them

I then made 4 histograms to see what column could appear to be skewed to the right using fixed acidity, total sulfur dioxide
ph and alcohol

