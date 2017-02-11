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

Fitting data around straight line equation y = mx+b

In this nano project we are using Simple line equation y = mX +b to build supervised Linear Regression Model.

Based upon given data, we are taking y (target) as Life Expectancy and X (feature) as BMI of people, Look at the data here, (there are no name columns) but do note, that first column is Life Expetancy and second column is BMI. https://github.com/pankymathur/LIfe-Expectancy-From-BMI/blob/master/bmi_and_life_expectancy.csv

Our model, will assume that there is relationship between y (Life Expetancy) and X (BMI) and they are following a pattern that is represented by equation of line y = mx +b

where 'm' is the slope between 'X' (BMI) and 'y' (Life Expectancy), i.e. relationship factor, and in comaprison to our data, it mean that for every unit of BMI (X), Life Expectancy (y) will be increase by m times.

'b' is y-intercept (a constant value), y-intercept, it's a default value of y when x = 0 and is always constant for any values of x > 0, and in comparison to our data, it mean that whether any value of BMI (X) is given or not to our model, there is always a Life Expetancy (y) which is b .

Who will have ever known that AI would be so pro life.... :)

Computing errors via Square of errors function (y_predicted - y)^2

Let's move forward, but please note, both 'm' & 'b' will be generated during model training or sometime called in machine learning world 'fit process'. (All SciKit-Learn models used .fit() method to train a model from data)

Long Story short, They way Training or model fitting works (atleast in my understanding..), is that we will use equation type y = mX + b, on the given data via trying to fit all values of X in relationship to y and by finding correct slope 'm' and adding 'b' (y-itercept a constant value) to it.

This will be achieved by choosing any random value of m and b and then put X value into equation (y = mX +b ), this will give us a new y. This new y aka y_predicted will be compare to actual y from data, and then we will take the square of the difference of errors, i.e. error function f(x) = (y_initial - y_predicted)^2

# The Square of Error function

def compute_error_for_line_given_points(b, m, points):
 
 totalError = 0
 
 for i in range(0, len(points)):
 x = points[i,0]
 y = points[i,1]
 # Our Error funcion f(X)= (y_initial-y_predicted)^2
 totalError += (y - (m*x + b)) ** 2
 print "At Row {0}, using b = {1} and m = {2}, Error = {3}".format(i,b, m, totalError)

return totalError / float(len(points))

for example, if you open life_expectancy.csv https://github.com/pankymathur/LIfe-Expectancy-From-BMI/blob/master/bmi_and_life_expectancy.csv you will see in first row, with BMI (X) = 20.62058 and Life Expectancy (y) = 52.8 years

let's say we use randomly m = 1 and b = 1. Then we put these values into equation y_predicted = mX +b.

so y_predicted = (1)(20.62058) + 1 = 21.62058 years

now actual y was 52.8 years, so error function f(x) = (y_initial - y_predicted)^2 = (52.8 years - 21.62058 years ) ^2 = 31.17942 years. That Sound like a huge unforgiven error for predicting a person age. However, this is where logic of self learning, meaning learning from your mistake will come to picture.

Now, we will take this error and try to minimize this by choosing different value of 'm' and 'b'. How do we know, which value of 'm' and 'b' is right at this point, actually we don't, however, we know that which direction we can take, meaning, we know, that by choosing m = 1 and b = 1 we are very short of predicting correct life span of 52.8 years. so let's go in the direction of choosing higher m and b.

how about m = 3 and b = 3 , so new y_predicted = (m)(X) + b = (3)(20.62058) + 3 = 64.86174 years. so,  error function f(x) = (y_initial - y_predicted)^2 = (52.8 years - 64.86174 years ) ^2 = 12.06174 years (you saw why we choose to square the errors, so we have positive error value..)

12.06174 years error is better then 31.17942 years but still not good.

how about m = 2.5 and b = 2.5 , so new y_predicted = (m)(X) + b = (2.5)(20.62058) + 2.5 = 54.05145 years. so,  error function f(x) = (y_initial - y_predicted)^2 = (52.8 years - 54.05145 years ) ^2 = 1.25145 years

Not bad at all, we just achieve error of only 1.25 years in just 3 steps of starting with random values of m and b and then learning from error which direction to go. Now, that's sound something like self learning.

Minimizing Errors using partial derivatives aka Gradient Descent

Now the good news, and this is where the power of math (calculus to be precise) comes to picture. In above example we were minimizing errors by changing manually higher or lower values of m and b values via choosing a direction where error tends to be going down and repeating that process few times until error is minimized.  This whole process can be automatized by using partial derivatives (http://mathinsight.org/partial_derivative_introduction) .

Here is an image representing Gradient Descent in action from  MATT NEDRICH , one of my favorite blogger who frequently write about Machine and Deep Learning.



Wait.. Don't Panic.. I will try to explain in simple words, what is partial derivative and how this is connected with changing values of m and b by choosing direction in which error tends to be going down.
Partial derivative is a branch of calculus, Calculus is a branch of mathematics, that deals with study of change, like Geometry that deals with study of shapes and space or like Algebra that deals with study of functions.  Partial derivative calculate rate of change of function with respect to one variable at one time and keeping other variables constant.
In our example, our error function is f(x) = (y_initial - y_predicted)^2, so by using partial derivative on f(x) with respect to b and keeping m as constant, we can get rate of change of error function with respect to b, we can call this b_gradient, this could be positive or negative value and it need to be applied to previous value of b, so to come up with new value of b.
Here is the mathematical formula for calculating b_gradient:

b_gradient += - (2/N) * 1 * (y - ((m_current * x) + b_current))


Similarly, by using partial derivative on f(x) = (y_initial - y_predicted)^2 with respect to m and keeping b as constant, we can get m_gradient, this could be positive or negative value and it need to applied to previous value of m, so to come up with new value of m.
Here is the mathematical formula for calculating m_gradient:

m_gradient += - (2/N) * x * (y - ((m_current * x) + b_current))


Computing new m & b by using Gradient Descent with Learning Rate over many iterations

new_b = b_current - (learningRate * b_gradient)
new_m = m_current - (learningRate * m_gradient)

Now, We will use b_gradient and m_gradient which could be positive or negative value and we will apply them to previous value of b and m, in order to come up with new value of b and m. However, instead of adding directly b_gradient and m_gradient, we will add a learning rate factor to these gradients. Then we will run this same process over many iterations to come up with best fitted b_gradient and m_gradient.


In Machine Learning or Deep Learning lingo, Learning Rate and Iterations are called Hyper parameters. These hyper parameter are used to fine tune model by fitting model more accurately around the data, however, beware that Hyper Parameters are two sided sword, you want to use them to fine tune your model on training data but you don't want to over fit the model so that it will do poor prediction on any new test result. Again, in Machine Learning/ Deep Learning lingo it mean Generalized model vs Over fitted model.


#Here is complete step_gradient function

def step_gradient(b_current, m_current, points, learningRate, iteration):
 
 b_gradient = 0
 m_gradient = 0
 N = float(len(points))
 
 for i in range(len(points)):
 x = points[i,0]
 y = points[i,1]
 # Partial derivatives calcultion for b_gradient an m_gradient for error funcion f(X)= (y_initial-y_predicted)^2
 b_gradient += - (2/N) * 1 * (y - ((m_current * x) + b_current))
 m_gradient += - (2/N) * x * (y - ((m_current * x) + b_current))

# print "At row = {0}, b_gradient = {1}, m_gradient = {2}".format(i, b_gradient, m_gradient)

new_b = b_current - (learningRate * b_gradient)
 new_m = m_current - (learningRate * m_gradient)
 print "\n After {0} iterations the new b = b_current - (learningRate * b_gradient) = {1} - ({3} * {2}) = {4}".format(iteration+1, b_current, b_gradient, learningRate, new_b)
 print "After {0} iterations the new m = m_current - (learningRate * m_gradient) = {1} - ({3} * {2}) = {4} \n".format(iteration+1, m_current, m_gradient, learningRate, new_m)


 return [new_b, new_m]
 
 
#Here is complete Gradient Runner Function that run step gradient over many iterations to come up with # new b and m

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
 
 b1 = starting_b
 m1 = starting_m
 for i in range(num_iterations):
 b1, m1 = step_gradient(b1, m1, array(points), learning_rate, i)
 
 return [b1, m1]
 
Use this new m & b to predict Blood Sugar of sample/test data of BMI

# now lets use this new b and m to predict some random person expected life expectancy by given BMI

 print "\n Enter BMI to get Blood Pressure\n"
 X_test = 27.6
 print "\n Test/Sample BMI is: {0}\n".format(X_test)
 y_test = m * X_test + b
 print "\n Blood Sugar is {0} \n".format(y_test)
