# Videogame sales analysis and prediction

* In this project we are going to use the videogame sales dataset from 1980 to 2015 from Kaggle, so we can answer these 6 questions and in the end, make a prediction model for the sales of specific genres

# The continent with the most videogame sales

# Top 5 selling genres of that continent

# Top 5 publishers of that continent

# History of the sales in that continent

# Top 5 genres of that continent compared to global sells

# Prediction of those 5 genres' sales in the future

First, we have to read the dataset from the CSV file and check for null values, and drop them, as this dataset is kind of small I already checked the entries in Excel to look for incorrect info in the entries, erasing all the entries from 2016 onwards, as they had only 4 or 2 each, then we check the head of the dataset for visualization purposes

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/689e04f2-8ce1-444e-a390-9376a515aaae)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/28219ada-d226-4064-a42e-bbb7e6c0716c)

Then to answer the first question we first make a sum of the sales through the years of the different columns we have in the dataset, we will use this data for a pie chart that is going to show us the continent with the most games sold

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/338be2fd-a775-4385-86e5-773cd32c41d8)

As we can see the continent with the most games sold is NA, with this info we can follow with the next question, doing a barplot with the NA videogame sales grouped by genre to see the top 5 sellers of NA

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/8c4cdaf1-ea07-4660-9952-8dfd30021ec4)

We can see that the action genre has been the most sold over the years, for extra information that will be useful in the future, we are going to get the average of action games released per year and the average global sales of this genre over the years

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/d5c77917-f77e-4f5a-86f9-00b7c74a69a2)

Then for the next question we just use the same method as the previous one but grouping the NA sales by publishers

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/9ed1a716-39dd-4cdc-900c-e0b877fe21a1)

As we see the most sold publisher was Nintendo

Now we will use line plots for the time series of the NA sales over the years to check the history of the sales of NA and check for any relevant information or pattern we might encounter

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/9a4a2600-fd57-4ff1-a492-fb3137efe21d)

Here we can see that from the year 1995 onward there was a massive increase in sales that peaked between 2008 and 2009 and started decreasing until the end of the dataset

Now to compare the 5 most sold genres of NA to global sales divided by continents and the global sales, we are going to do more lineplots as they will show us too the sales over time

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/5e9b7621-e172-404f-967a-809658ce3c43)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/3c9628e1-6233-4e29-b443-7e8334249912)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/65448488-c395-4798-9049-e11b2228561b)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/071834d4-bf60-4ad5-83d2-4633a79fc672)

Now we can see how the Action genre remains at the top in every continent and globally except for JP sales, where the role-playing game seems to remain more popular over the years

Now it is time to make the metrics we need like platform, genre, and publisher into dummy columns using one hot encode, and dropping the columns like  name, and the sales columns, also encapsulating the publishers that do not get repeated more than 50 times into the small publisher column

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/49465ea6-d4aa-4efe-a881-c944a647271d)

We now define the variables for the train and test splitting using the global sales column as that is the main variable, then we just use a scaler, optimizer and a custom r2 score function for the metrics of the linear regression model

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/bf397e67-6a5a-452f-b9db-19852ba1b98b)

Now all that is left to do is to make and train the model using Keras

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/13ab7796-42aa-480e-9267-40a6a0f9bfbc)

Now we save the model in a file and use it to get the metrics

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/96e32011-e227-4497-8097-3077fade481b)

As we can see the model is not overfitting and it has a good loss and val_loss ,the graphic shows that the model is not overfitting, also for the R2 score it has 0.43 which is acceptable for this model as this is a really small dataset

At last we make some new singular entries with their respective values to show a prediction, note that this prediction is not as accurate due to the small number of variables we have on the dataset, even though this is a time series model

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/02a59a79-f391-42f1-9c8c-f0721cc98b0a)
![image](https://github.com/Mariomte41/Portfolio/assets/140863879/82f848d6-0cf3-465c-8c1f-645b6d92f7bc)

As we can see the values are not that different from the expected and for the final entry I created 80 values of the genre action, to show the comparison of the prediction we got to the average we saw before,we can say that the results seem realistic compared to the real data
