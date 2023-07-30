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

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/32c013ba-42a3-4ded-a5bd-7dfb46a06b22)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/e9d99a4a-5404-4eed-b872-4b5f2a77d2b7)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/d4ae7158-6454-4084-a4df-b6d293e8c0fc)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/01e9e4c5-aa5c-4947-a060-c793968f795e)


As we can see the most skewed to the right are the fixed acidity and the alcohol

Then i used 4 scatterplots to answer another individual question seeing which one of these 4 columns are the most propense to have a good impact on quality

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/7ff332a5-2a37-4364-a07a-9c68054bfa13)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/2dfa9376-36b7-4fca-a580-0b136230fb26)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/5e6addfe-8467-4e6f-86f5-484f1fdecfca)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/229e57cc-c3fd-436d-b65d-31b100c87435)

In this we can see that alcohol is the most propense to have a positive impact on the quality, so we just confirm it with a heatmap of the correlationof all the wine features seeing that there is a 0.45 on the alcohol to quality correlation

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/ac0aa0e6-ed4a-483a-8dff-20b6f156dd67)

*Now we get onto the 4 primary questions being the first one: Is a certain type of wine (red or white) associated with higher quality?

We use the groupby function including the mean function to get the mean correlation between color and quality
![image](https://github.com/Mariomte41/Portfolio/assets/140863879/832d8366-71e4-431a-9163-11b39cc6711a)

We can see that in fact, the white wine is associated with a higher quality

*The next questions is: Do wines with higher alcoholic content receive better ratings?

For this what i did was get the median from the alcohol column and then divide it between the low_alcohol and high_alcohol columns doing a more and equal than and a minor than the median

Then we use the .mean function to get the mean in relation to the quality of the two columns
![image](https://github.com/Mariomte41/Portfolio/assets/140863879/473aba3e-3463-4ac8-9106-d372ac9cdd9f)
And then we make a barplot to ensure the quality in relation to the columns
![image](https://github.com/Mariomte41/Portfolio/assets/140863879/943b5e9c-5da3-4457-aa66-678250324b22)

The answer to the question is that yes, the higher alcoholic content receives better ratings


*The next question is: Do sweeter wines (more residual sugar) receive better ratings?

For this question i did the same as the alcohol one and got the median of the residual sugar column and divide it between the median then i used it to get a mean compared to the quality
![image](https://github.com/Mariomte41/Portfolio/assets/140863879/3a4c8dc0-cd6b-4226-a1dc-43fe8a9aab40)
![image](https://github.com/Mariomte41/Portfolio/assets/140863879/6cdfc4a0-ce78-44e9-902a-6eee01260132)
And made a linear plot to show that in fact a higher residual sugar gets the wine better ratings


The final question is: What level of acidity is associated with the highest quality?

For this question i had to use the function .describe of the pH column to show the kind of acidity the wine had, separating it in bins named high, moderately high, medium and low, then using them to make a new column named acidity levels that had these bins compared to the ph column, next i got the mean of the acidity levels compared to the quality

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/dfee743a-36e9-42f9-9bbf-ab5ba2daa8cc)
![image](https://github.com/Mariomte41/Portfolio/assets/140863879/b7ed0b29-0182-47d2-aeca-4c0593d0a730)

Then for confirming the data i made a plot showing that in fact the low acidity level is better for the average quality showing an inversely proportional growth answering the final question
