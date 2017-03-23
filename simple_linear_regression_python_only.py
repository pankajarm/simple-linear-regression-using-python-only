#simple linear regression using python and numpy, no fancy sklearn, pandas packages needed
# Note we have use only 2 functions from numpy: genfromtxt and array

#  import packages
from __future__ import division
from numpy import genfromtxt, array

# we are goning to use Linear equation of type y = mx + b
# where m is slope, and b is y-intercept, a constant
# x is independent varaible aka feature and y is depdendent variable aka target

# The Step Gradient Descent function => use the error/ cost function and then minimize it using partial deriviatives
def step_gradient(b_current, m_current, points, learningRate, iteration):
	
	b_gradient = 0
	m_gradient = 0
	N = float(len(points))
	
	for i in range(len(points)):
		x = points[i,0]
		y = points[i,1]
		#  Partial derivatives calcultion for b_gradient an m_gradient for error funcion f(X)= ((y_initial-y_predicted)^2) / N

		# (d)/(db)((y - (m x + b))^2/N) = (2 (b + m x - y))/N = - (2/N (-b -mx +y)) =  - (2/N (y - (mx+b))
		b_gradient += - (2/N) * (y - ((m_current * x) + b_current))

		# (d)/(db)((y - (m x + b))^2/N) = (2x (b + m x - y))/N = - (2x/N (-b -mx +y)) = - (2x/N (y - (mx+b))
		m_gradient += - (2/N) * x * (y - ((m_current * x) + b_current))

		# print "At row = {0}, b_gradient = {1}, m_gradient = {2}".format(i, b_gradient, m_gradient)

	new_b = b_current - (learningRate * b_gradient)
	new_m = m_current - (learningRate * m_gradient)
	# print "\n After {0} iterations the new b = b_current - (learningRate * b_gradient) = {1} - ({3} * {2}) = {4}".format(iteration+1, b_current, b_gradient, learningRate, new_b)
	# print "After {0} iterations the new m = m_current - (learningRate * m_gradient) = {1} - ({3} * {2}) = {4} \n".format(iteration+1, m_current, m_gradient, learningRate, new_m)


	return [new_b, new_m]


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
	
	b1 = starting_b
	m1 = starting_m
	for i in range(num_iterations):
		b1, m1 = step_gradient(b1, m1, array(points), learning_rate, i)
	
	return [b1, m1]

# The Square of Error function
def compute_error_for_line_given_points(b, m, points):
	
	totalError = 0
	error = 0
	
	for i in range(0, len(points)):
		x = points[i,0]
		y = points[i,1]
		# Our Error funcion f(x) = ((y_initial - y_predicted)^2) / Number of data rows
		error = ((y - (m*x + b)) ** 2) / len(points)
		totalError += error / len(points)
		print "At Row {0}, using b = {1} and m = {2}, Error = {3}".format(i, b, m, error)

	print "\n Total Error is: {0}".format(totalError)
	return error, totalError

def pankax():

	#data from data.csv cotaining number of study hours and GPA
	points = genfromtxt("diabetes.csv", delimiter=",")
	
	# choose learning rate
	learning_rate = 0.001
	
	# iniital y-intercept guess aka the constant in linear equation
	initial_b = 1
	
	#  iniital slope guess
	initial_m = 1
	
	# choose numbr of iterations to run linear regression
	num_iterations = 100
	
	#print linear regression is working
	print "\n First compute Error for each row by using equation y_predicted = mx +b and error =  (y - y_predicted) ^2 / len(points) by using random b = {0}, and m = {1} \n".format(initial_b, initial_m)

	# compute errors
	compute_error_for_line_given_points(initial_b, initial_m,points)
	
	print "\n Now, let's run gradient_descent_runner to get new m and b with learning rate of {1} and {0} iterations \n".format(num_iterations, learning_rate)
	
	[b,m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)

	# print (b,m)

	# compute final error with new b and m calculated from gradient_descent_runner
	compute_error_for_line_given_points(b,m,points)
	print "\n After {0}nd iterations final b = {1}, m = {2} \n".format(num_iterations,b,m)

	# now lets use this new b and m to predict some random person expected life expectancy by given BMI
	print "\n Enter BMI to get Blood Sugar\n"
	X_test = 27.2
	print "\n Test/Sample BMI is: {0}\n".format(X_test)
	y_test = m * X_test + b
	print "\n Blood Sugar is {0} \n".format(y_test)


# as usual start with main function and put it in the end of the code
if __name__ == '__main__':
	pankax()
