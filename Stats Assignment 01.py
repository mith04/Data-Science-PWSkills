#!/usr/bin/env python
# coding: utf-8

# # Q1. What is Statistics?
# 

# Statistics  is the Science of collecting,Organising ,analyzing,interpretation, presentation of data .

# # Q2. Define the different types of statistics and give an example of when each type might be used.
# 

# There are 2 types of StatisTics:
# 1.Descriptive statistics 
# 2.Inferential Statistics:
# 
# **** common technicques used in Descriptive statistics *** 
# 
# a.Measures of Central Tendency : This includes mean(average), median(middle value) and mode(frequent value)
# 
# b.Measures of Dispersion : this includes the range , variance and standard deviations 
# 
# c.Frequency of Distibutions : this displays the frequency of each value Or Range of value in a dataset using histograms, bar charts Or frequency tables.

# Eaxmple Where we can use it. 
# 1. descriptive statistics : in the survey of the ages of employees in a company, You might calculate the Mean,median And Mode of the age To provide the summary of age distributions in a company .
# 
# 2. Inferentail statistics : A pharmeutical company want to test if  a new medicine is effective Or not . they done a clinical test on sample of patient to determine the medicine is effective Or not And can be generaluized to the larger populations 
# 

# # Q3.  What are the different types of data and how do they differ from each other? Provide an example of each type of data.

# Types of Data types : 
# 
# 1. Categorical OR Qualitive Datatypes
# a.Nominal Data  : It is also Called Categorical data , Consists of Categories or label without any inherent Or numerical value
# 
# Example :Gender(Male and female),eye color , types of fruits 
# 
# b.Ordinal Data : It represents the categories with meaningful Order or ranking but doesn't have consist interval between categories
# Example : customer feedback(good, better , bad)
# Education Levels(high school diploma , Bachelor's degree Or master degree)
# 
# 2. Numerical Or Quantitive Data types :
# a. Discrete Data :Discrete data can only take on specific, distinct values and often involves counting rather than measuring.Only whole numbers are accepted .
# Example : numbers of Student in class.
# 
# 
# b. continuous Data :Continuous data is data that can be calculated. It has an infinite number of probable values that can be selected within a given specific range.
# 
# Example: Temperature range

# # Q4. Categorise the following datasets with respect to quantitative and qualitative data types:
# 
# # (i)	Grading in exam: A+, A, B+, B, C+, C, D, E
# 
# # (ii)	Colour of mangoes: yellow, green, orange, red
# 
# # (iii)	Height data of a class: [178.9, 179, 179.5, 176, 177.2, 178.3, 175.8,...]
# 
# # (iv)	Number of mangoes exported by a farm: [500, 600, 478, 672, …]

# Ans:
#     (i) Grading in exam: A+, A, B+, B, C+, C, D, E
# is a Qualitative values (Categorical value )
# 
# (ii) Colour of mangoes: yellow, green, orange, red === Qualitative values (Categorical value )
# 
# (iii) Height data of a class: [178.9, 179, 179.5, 176, 177.2, 178.3, 175.8, ...] === Quantitative Data 
# 
# (iv) Number of mangoes exported by a farm: [500, 600, 478, 672, ...] == Quantitative Data 

# # Q5. Explain the concept of levels of measurement and give an example of a variable for each level.
# 

# 1. Nominal Level of measurement : Norminal data are categorical and represent distinct categories Or label with no inherent or order ranking .
# Example : EYE COLOR , TYPES OF CARS, BLOOD TYPES
# 
# 2. Ordinal Level of measurement : Ordinal data are categorical data with a Meaningful order or ranking but the intervals between categories are not consistly measureable or meaningful 
# 
# example : Education levels
# customer statisfactions rating
# 
# 3.Interval Level of Measurement: interval data have ordered categories with consistent intervals between them, but there is no true Zero points 
# 
# example : Temperature In Celsius 
# IQ SCORES
# 
# 4.RATIO LEVELS OF MEASUREMENTS : Ratio  data have Ordered categories with consistent Intervals between them and a true Zero Points , where Zerso indicates the complete ablsence od the attribute beinf Measured
# 
# Example : Height, weight, Income 

# # Q6. Why is it important to understand the level of measurement when analyzing data? Provide an example to illustrate your answer.

# Ans: The Level of measurement is Crucial when analyzing the data because it detemines the types of statistical analyses and operations that are appropriate for the data . 
# Failing to recognize the Level of measurement can Lead to Incorrect Conclusions and inappropriate statistical techniques
# 
# Here are the Techniques why it is important to understands the Level of measurements:
# 
# 1. Appropriate Statistical Techniques : Different Levels of measurements require different types of statistical techniques .Using wrong Statistical techniques Can lead to a Misleading results. 
# 
# Example : if you test Ordinal data as interval data , you may calculate meaningless Means or Variance
# 
# 2. Proper Data Presentation : Understanding the Level of measurements Helps in Choosing Appropriate data Visualizations Model .
# For example : a.Norminal data can be represented using Bar chart Or pie charts 
# b. Interval and ration data can be represented using histograms and Scatterplots 
# 
# 3. Meaningful Interpretation:Knowing the level of measurement allows for meaningful interpretation of results.
# 
# Example :
# 
# It's appropriate to say that a group with a mean height of 180 cm is taller than a group with a mean height of 170 cm when dealing with ratio data.
# 
# 
# ***** Here is the Example why Understanding of level of measurement is Important***** 
# 
# --> suppose you are taking a Survey for a restaurant, Where you asked the Customer to rate as per the Overall experience in this restaurant.
# rating scale is Between 0 to 5 ( 0 -- very unstatisfied and 5 -- very Statsified )
# 
# the data collected are Ordinal data because the categories hace an order but do not have consistent intervals between them 
# 
# 
# If you treat this ordinal data as interval data and calculate the mean satisfaction score, you might conclude that the restaurant's average satisfaction rating is 3.5.However, this interpretation is misleading because the intervals between the ratings (1 to 2, 2 to 3, etc.) do not necessarily represent equal differences in satisfaction. Using ordinal data to calculate a mean in this manner can lead to the false impression that the restaurant's satisfaction is mediocre when, in reality, customer perceptions might vary widely.
# 
# 

# # Q7. How nominal data type is different from ordinal data type.
# 

# The main differences between Nominal Data and Ordinal Data are:
# 
# 1. While Nominal Data is classified without any intrinsic ordering or rank, Ordinal Data has some predetermined or natural order.
# 
# 2. Nominal data is qualitative or categorical data, while Ordinal data is considered “in-between” qualitative and quantitative data.

# # Q8. Which type of plot can be used to display data in terms of range?
# 
# Ans : Box plot is a type of plot that used to display data in terms of range 
# 
# Box plot provide graphical summary of a data set including: minimum Value,First Quartile(25%) , median(50%) ,third Quartile(75%)
# and Maximum values

# #  Describe the difference between descriptive and inferential statistics. Give an example of each type of statistics and explain how they are used

# Ans : Descriptive Statistics: Descriptive Statistics are used to summarise and describe the main features of dataset . and it's main aim to Provide a simple and concise overviee of the data's characteristics without making inference about a large population
# 
# ** we can Calculate mean, median , mode and frequency Distribution of the dataset . It helps to understand the centeral Of tendency , varibality and Distrinution of the data 
# 
# Inferential Statistics:Inferential Statistics involves making inferences Or predicitions about a popultations based on a sample of data . They are used to draw conculsions ,test hypothesis and make generalizations beyond the Observed data set 
# 
# we can use it : Hypothesis testing , confidence of intervals , regressions analysis and ANOVA
# 
# Example : pharmaceutical company  is testing a new medicine to Lower blood pressure . they collected sample of 200 patients and calculated the mean reductions in BLOOD PRESSURE REDUCTION 
# this is a example of descriptive statistics 
# 
# Inferences statistics:  They might conduct a hypothesis test to determine if the mean reduction observed in the sample is statistically significant and can be generalized to the broader population of patients. If it is statistically significant, they could conclude that the drug is effective for reducing blood pressure in the population.
# 
# 
# 
# 
# 

# # Q10. What are some common measures of central tendency and variability used in statistics? Explain how each measure can be used to describe a dataset

# Measures of Central Tendency:
# mean : The mean is the sum of all values in a dataset divided by the number of values. It represents the "average" value.
# 
# uses :The mean provides a measure of the center or typical value in the dataset. It is sensitive to extreme values (outliers).
# 
# Median : The median is the middle value when the data is arranged in ascending or descending order.
# use :he median is a measure of central tendency that is robust to outliers. It represents the middle value and is often used when the data contains extreme values or is not normally distributed.
# 
# 
# mode :The mode is the value(s) that occur most frequently in the dataset.
# use:The mode identifies the most common value(s) in the dataset. It is useful for categorical and discrete data and can help identify the "typical" category.
# 
# 
# Measures of Variability (Dispersion):
# 
# 
# Range :The range is the difference between the maximum and minimum values in the dataset.
# use :The range provides a simple measure of the spread of data. It is sensitive to outliers and is easy to calculate.
# 
# Variance:The variance is the average of the squared differences between each data point and the mean. It measures the average deviation of data points from the mean.
# 
# use :Variance quantifies the spread of data and is widely used in statistical analysis. A high variance indicates greater variability.
# Standard Deviation:
# 
# standard deviation: The standard deviation is the square root of the variance. It measures the average distance between data points and the mean.
# 
# Use: The standard deviation provides a measure of the dispersion of data similar to the variance but in the same units as the original data. It is a common and easily interpretable measure of variability.
# Interquartile Range (IQR):
# 
# Interquartile Range (IQR): The IQR is the range between the first quartile (Q1) and the third quartile (Q3). It represents the range of the middle 50% of the data.
# Use: The IQR is robust to outliers and provides a measure of the spread of the central portion of the data. It is often used in box plots to identify potential outliers.
# 

# In[ ]:




