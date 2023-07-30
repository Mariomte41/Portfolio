# Welcome to my portfolio
Porfolio containing my personal projects

# 1: Instagram data visualization, correlation and predictions of impressions

* In this project i used a dataframe with analytics from an instagram account, after i read the data and secured that there was no wrong numbers i visualized the density of the From home impressions and the From explore impressions with matplotlib

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/307275f1-c359-46be-a07f-06d7d66a3642)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/b3a61f07-046e-4f61-bc5f-9db8374045ce)

We can see that the From Explore source is a lot more dense than the From Home one

And i also used a pie chart so i could get a percentage of every income of impressions on the dataset

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/d1a46625-e79f-4258-9eb9-ed3eb83e1d05)

As we see the most input we get are from the From Home and From Hashtags sources

I then used a wordcloud to show the most used captions and hashtags in the account

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/91de6360-cfac-4d0a-88d9-6da28ed980fd)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/0740bed7-7379-4678-b10c-1988b6c51040)

I used the data of impressions with its relationship with likes, comments, shares and saves to make two scatter plots

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/9ca026da-3c40-4dca-af10-8e5c32624737)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/a5934306-b0cf-4b10-9f2c-6825089051f2)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/11c75971-730a-4552-8b5e-fa2149989d75)

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/c5b90aa8-61c5-4506-8137-764bcf5b4e0f)

We can see that the most positive relationship is the likes and impressions one, this meaning that likes are one of the most impactful measure for impressions

I then showed a correlation between the impressions and the other columns

![image](https://github.com/Mariomte41/Portfolio/assets/140863879/90a5ca30-b6ec-420b-a13e-c559a2758cd9)

This shows that the impressions are more impactfull with likes and saves, and if you have a higher count of those two your post will probably hava more reach

Now we want to know the conversion rate between the follows and profile visits so we make a simple formula to get it dividing the total of the two and then multiplying it to 100
![image](https://github.com/Mariomte41/Portfolio/assets/140863879/f8a45b63-f83d-468b-a4cb-0c847233a026)

We now make it a scatterplot to see if the relationship is linear
![image](https://github.com/Mariomte41/Portfolio/assets/140863879/bfd0b65c-ac07-4829-9f72-e8f0580bcf06)

We finally are gonna make a prediction model for the impressions of the account taking the data from all the other columns to see an aproximated reach with exact data of 282 likes 233 saves 4 coments 9 shares 165 profile visists and 54 follows
![image](https://github.com/Mariomte41/Portfolio/assets/140863879/e3e4cb5a-30df-4c6c-9feb-649f23aac694)

The predicction shows an aproximated of 9257.06 impressions for a post that has those measures
