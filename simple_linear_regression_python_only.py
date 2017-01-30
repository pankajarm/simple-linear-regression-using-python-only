#simple linear regression using python, no fancy liabraries and packages needed














def compute_error_for_line_given_points(b, m, points):
	
	totalError = 0
	
	for i in range(0, len(points)):
		x = points[i,0]
		y = points[i,1]
		totalError += (y - (m*x + b)) ** 2

	return totalError / float(len(points))


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
	pass


def pankax():
	
	points = 'data here'
	
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
