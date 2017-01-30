#simple linear regression using python, no fancy sklearn, scipy, pandas ackages needed
# use only 2 functions from numpy
from numpy import genfromtxt, array

# we are goning to use Linear equation of type y = mx + b
# where m is slope, and b is y-intercept, a constant
# x is independent varaible and y is depdendent variable

# The Step Gradient/ Slope Descent function, calcualates gradient of b and m
def step_gradient(b_current, m_current, points, learningRate):
	b_gradient = 0
	m_gradient = 0
	N = float(len(points))
	for i in range(len(points)):
		x = points[i,0]
		y = points[i,1]
		b_gradient += - (2/N) * (y - ((m_current * x) + b_current))
		m_gradient += - (2/N) * x * (y - ((m_current * x) + b_current))

	new_b = b_current - (learningRate * b_gradient)
	new_m = m_current - (learningRate * m_gradient)

	return [new_b, new_b]


# The Error function
def compute_error_for_line_given_points(b, m, points):
	
	totalError = 0
	
	for i in range(0, len(points)):
		x = points[i,0]
		y = points[i,1]
		totalError += (y - (m*x + b)) ** 2

	return totalError / float(len(points))


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
	
	b = starting_b
	m = starting_m
	for i in range(num_iterations):
		b, m = step_gradient(b,m, array(points), learning_rate)
		return [b, m]


def pankax():

	#data from data.csv cotaining number of study hours and GPA
	points = genfromtxt("data.csv", delimiter=",")
	
	# choose learning rate
	learning_rate = 0.0001
	
	# iniital y-intercept guess aka the constant in linear equation
	initial_b = 0
	
	#  iniital slope guess
	initial_m = 0
	
	# choose numbr of iterations to run linear regression
	num_iterations = 1000
	
	# now print linear regression is working
	print "Starting Gradient/Slope descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m,points))
	
	print "Running..."
	
	[b,m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
	print "After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations,b,m,compute_error_for_line_given_points(b,m,points))


# as usual start with main function and put it in the end of the code
if __name__ == '__main__':
	pankax()
