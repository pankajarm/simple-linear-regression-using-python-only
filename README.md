# simple-linear-regression-using-python-only

In this nano project, we will build simple but robust linear regression model from scratch in python and use it to predict Blood Sugar of Diabetes Patient from their BMI data.

Read more about Body Mass Index and how it impacts people health in various ways, and ultimately how it effect Blood Sugar among diabetes patient Here: https://en.wikipedia.org/wiki/Body_mass_index

Data taken from http://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt is showing Blood Sugar (in mg/l) of 442 diabetes patient with 10 baseline variables, age, sex, body mass index, average blood pressure, and six blood serum measurements

Yes, you heard right in Title of this article, we will used no state of the art SciKit Learn but will build Linear Regression model with our own hand from scratch and explaining things on the way.

We will be covering:

Fitting data around straight line equation y = mx+b

Computing errors via Square of errors (y_predicted - y)^2

Minimizing Errors using partial derivatives aka Gradient Descent

Computing new m & b by using Gradient Descent with Learning Rate over many iterations

Use this new m & b to predict Blood Sugar of sample/test data of BMI

Please note, This article does not undermine status of SciKit-Learn or GraphLab anyhow and that these packages are unncesseary (because they are totally absolutely wonderful, widely used in industry and much needed packages for any real life machine learning or data science projects)

However, the Goal is to show math and beauty of python, and the reasoning that all these packages are somehow using similar math and logic behind the doors.  In addition these packages provides many many other features, and very highly sustainable Machine Learning models , via simple funciton calls. Read more about SciKit Learn here, http://scikit-learn.org/stable/ & https://turi.com

Ok, enough background, lets' kickoff this nano project.

Please read the complete article here:

http://pankajmathur.com/learn-linear-regression-a-must-have-for-deep-learning-machine-learning-any-kind-learnings-you-will-do/
