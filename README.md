# simple-linear-regression-using-python-only

In this nano project, we will build simple but robust linear regression model from scratch in python and use it to predict
life expectancy of people from their BMI data. 

Read more about Body Mass Index and how it impacts people health in various ways, and ultimately life expectancy Here: https://en.wikipedia.org/wiki/Body_mass_index

Data taken from https://www.gapminder.org/ showing life expectancy of people in different country in correlation to BMI

Yes, you heard right, we will used no state of the art SciKit Learn but will build Linear Regression model with our own hand.

Please note, This is not to undermine anyhow, that these packages are unncesseary (because they are totally absolutely wonderful, widely used in industry and much needed packages for any real life machine learning or data science projects)

However, the Goal is to show math and beauty of python, and the reasoning that all these packages are using similar math and logic behind the doors and then create highly sustainable Machine Learning models, which are provide via simple funciton calls. Read more about SciKit Learn here, http://scikit-learn.org/stable/

In this nano project we are using Simple line equation y = mX +b to build supervised Linear Regression Model. 

Based upon given data, we are taking y (target) as Life Expectancy and X (feature) as BMI of people, Look at the data here, these are no name columns but do note, first column is Life Expetancy and second column is BMI https://github.com/pankymathur/LIfe-Expectancy-From-BMI/blob/master/bmi_and_life_expectancy.csv

Our model, will assume that there is relationship between y (Life Expetancy) and X (BMI) which is following equation of line
y = mx +b  where 'm' as the slope between 'X' and 'y', i.e. relationship factor and 'b' is y-intercept (a constant value), minimum default value of y when x = 0 and is always constant for any values of x > 0

Do note, both 'm' & 'b' will be generated during model training or sometime called in machine learning workd as a fit process. (All SK-Learn models used .fit() method to train a model from data)

Long Story short, They way Training or model fitting works (atleast in my understanding..), is that we will use equation type y = mX + b, from the given data.csv which has Study Hours (X) and GPA (y), via trying and fitting all values of X in relationship to y by finding correct slope 'm' and by adding 'b' (y-itercept a constant value) to it.

We will start with random value of m and b, let's say m = 1 and b = 1. Then we put these values into equation y = mX +b. 

for example, if you open life_expectancy.csv https://github.com/pankymathur/LIfe-Expectancy-From-BMI/blob/master/bmi_and_life_expectancy.csv you will see in first row, with BMI = and Life Expectancy = 

Hope it all make sense to you...
