# simple-linear-regression-using-python-only

In this nano project, we will build simple but robust linear regression model from scratch in python and use it to predict
life expectancy of people from their BMI data. 

Read more about Body Mass Index and how it impacts people health in various ways, and ultimately life expectancy Here: https://en.wikipedia.org/wiki/Body_mass_index

Data taken from https://www.gapminder.org/ showing life expectancy of people in different country in correlation to BMI

Yes, you heard right, we will used no state of the art SciKit Learn but will build Linear Regression model with our own hand.

Please note, This is not to undermine anyhow, that these packages are unncesseary (because they are totally absolutely wonderful, widely used in industry and much needed packages for any real life machine learning or data science projects)

However, the Goal is to show math and beauty of python, and the reasoning that all these packages are using similar math and logic behind the doors and then create highly sustainable Machine Learning models, which are provide via simple funciton calls. Read more about SciKit Learn here, http://scikit-learn.org/stable/

In this nano project we are using Simple line equation y = mX +b to build supervised Linear Regression Model. 

Based upon given data, we are taking y (target) as Life Expectancy and X (feature) as BMI of people, Look at the data here, (there are no name columns) but do note, that first column is Life Expetancy and second column is BMI. https://github.com/pankymathur/LIfe-Expectancy-From-BMI/blob/master/bmi_and_life_expectancy.csv

Our model, will assume that there is relationship between y (Life Expetancy) and X (BMI) and they are following a pattern that is represented by equation of line y = mx +b

where 'm' is the slope between 'X' (BMI) and 'y' (Life Expectancy), i.e. relationship factor, and in comaprison to our data, it mean that for every unit of BMI (X), Life Expectancy (y) will be increase by m times. 

'b' is y-intercept (a constant value), y-intercept, it's a default value of y when x = 0 and is always constant for any values of x > 0, and in comparison to our data, it mean that whether any value of BMI (X) is given or not to our model, there is always a Life Expetancy (y) which is b .

Who will have ever known that AI would be so pro life.... :)

Let's move forward, but Do note, both 'm' & 'b' will be generated during model training or sometime called in machine learning world 'fit process'. (All SK-Learn models used .fit() method to train a model from data)

Long Story short, They way Training or model fitting works (atleast in my understanding..), is that we will use equation type y = mX + b, on the given data via trying to fit all values of X in relationship to y and by finding correct slope 'm' and adding 'b' (y-itercept a constant value) to it. 

This will be achieved by choosing any random value of m and b and then put X value into equation (y = mX +b ), this will give us a new y. This new y aka y_predicted will be compare to actual y from data, and then we will take the square of the difference of errors, i.e. error = (y - y_predicted) ^ 2

for example, if you open life_expectancy.csv https://github.com/pankymathur/LIfe-Expectancy-From-BMI/blob/master/bmi_and_life_expectancy.csv you will see in first row, with BMI (X) = 20.62058 and Life Expectancy (y) = 52.8 years

let's say we use randomly m = 1 and b = 1. Then we put these values into equation y_predicted = mX +b. 

so y_predicted = (1)(20.62058) + 1 = 21.62058 years

now actual y was 52.8 years, so error = (y - y_predicted ) ^ 2 = (52.8 years - 21.62058 years ) ^2 = 31.17942 years. That Sound like a huge unforgiven error for predicting a person age. However, this is where logic of self learning, meaning learning from your mistake will come to picture.

Now, we will take this error and try to minimize this by choosing different value of 'm' and 'b'. How do we know, which value of 'm' and 'b' is right at this point, actually we don't, however, we know that which direction we can take, meaning, we know, that by choosing m = 1 and b = 1 we are very short of predicting correct life span of 52.8 years. so let's go in the direction of choosing higher m and b. 

how about m = 3 and b = 3 , so new y_predicted = (m)(X) + b = (3)(20.62058) + 3 = 64.86174 years. 
so, error = (y - y_predicted ) ^ 2 = (52.8 years - 64.86174 years ) ^2 = 12.06174 years (you saw why we choose to square the errors, so we have positive error value..)

12.06174 years error is better then 31.17942 years but still not good. 

how about m = 2.5 and b = 2.5 , so new y_predicted = (m)(X) + b = (2.5)(20.62058) + 2.5 = 54.05145 years. 
so, error = (y - y_predicted ) ^ 2 = (52.8 years - 54.05145 years ) ^2 = 1.25145 years

Not bad at all, we just achieve error of only 1.25 years in just 3 steps of starting with random values of m and b and then learning from error which direction to go. Now, that's sound something like self learning. 

Hope it all make sense to you...

Let me know your thoughts, questions under comments section. 
