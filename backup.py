# 3:19 PM 
#  import packages
from __future__ import division
from __future__ import print_function
from numpy import genfromtxt, array


# write step gradient function here using partial derivatives

def step_gradient(b_current, m_current, points, learningRate):

	# set initial b_gradient
	b_gradient = 0
	# set initial m_gradient
	m_gradient = 0
	# N
	N = float(len(points))
	# now loop through all the points to calculate final_b and final_m for each x and y
	for i in range(len(points)):
		# get x, remember points[rows, columns]
		x = points[i,0]
		# get y, remeber points[rows, columns]
		y = points[i,1]
		# calculate y_new from current b and current m
		y_new = (m_current * x) + b_current
		# now keep adding partial derivative of b_gradient
		b_gradient += - (2/N) * 1 * (y - y_new)
		# now keep adding partial derivate of m_gradient
		m_gradient += - (2/N) * x * (y - y_new)

	# use partial deriviatives to calculate this minimize value of b
	final_b = b_current - (learningRate * b_gradient)
	# use partial derivatives to calculate minimize value of m
	final_m = m_current - (learningRate * m_gradient)

	return [final_b, final_m]

# compute error
def compute_error_for_line_with_given_points(b, m, points):

	# write logic to calculale square of error
	# start with zero error
	total_error = 0

	# go to points data in loop by maiking a rnageand get x, y
	for i in range(len(points)):
		x = points[i,0]
		y = points[i,1]

		# using x, b and m calculate new y, i.e. y1
		y1 = (m*x + b)

		# now calculate the difference between y and y1 and square the errors
		total_error += (y - y1) **2

	# return normalized error
	return total_error / float(len(points))

# gradient descent runner
def compute_gradient_descent_for_each_iterations(starting_b, starting_m, points, num_iterations, learning_rate):
	# FIST ATTEMPTED STOP TIME 3:52 PM ET
	# Second Attempt 12:45 PM
	# write logic to compute gradient descent for each iteration
	b1 = starting_b
	m1= starting_m
	for i in range(num_iterations):
		b1, m1 = step_gradient(b1, m1, array(points), learning_rate)
	
	return [b1, m1]


# write program flow in main function
def pankax():

	#  Goal is to come up with best fit line among data points starting at initial b and m
	# get data of points
	points = genfromtxt('data.csv', delimiter=",")

	# setup learning rate, at which you want your line move to best fit
	learning_rate = 0.01

	# setup initial b , y-intercept
	initial_b = 0

	# setup iniital m, slope
	initial_m = 0

	# setup iterations, in which you want to come up with final b and m with given learning rate
	iterations = 1000

	# compute initial error with initial b and initial m of line from points 
	initial_error = compute_error_for_line_with_given_points(initial_b, initial_m, array(points))

	#  print error
	print ('Going to star gradient descent at b =', initial_b, 'm = ', initial_m, 'with learning rate = ', learning_rate, 'and error = ', initial_error)

	print ("Running....")

	# compute  new b and m using gradient descent runner aka trying to find minimum error place by using slope/gradient
	[b, m] = compute_gradient_descent_for_each_iterations(initial_b, initial_m, array(points), iterations, learning_rate)

	print (b,m)

	# compute final error
	final_error = compute_error_for_line_with_given_points(b, m, array(points))

	#  print final error with new b and m from gradient descent
	print ('After ',iterations,' iterations, b = ',b,', m = ',m,' and final error = ',final_error)

	# minus 6 minutes
	pass

# call main functin on load
if __name__ == '__main__':
	pankax()