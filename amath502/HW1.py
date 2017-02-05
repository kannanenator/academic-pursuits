'''
AMATH 502 Assignment 1
By: Anand Kannan
'''

import matplotlib.pyplot as plt
import math

func1 = lambda x: x-x**2 # ** is how you do powers in python...^ is bitwise and
func2 = lambda x: 1-x**2

analytical_func1 = lambda t: (.25*math.exp(t))/(1+.25*math.exp(t))
analytical_func2 = lambda t: (math.exp(2*t)-1)/(math.exp(2*t)+1)

ic1 = (0, 0.2)
ic2 = (0, 0)

def calculate(func, analytical_func, method, step_size, initial_condition, t_final):
	xs = [x*step_size for x in range(initial_condition[0], int(t_final/step_size)+1)] # We know what the x values are already
	ys = [initial_condition[1]]

	y_n = initial_condition[1]

	# iterate the ys
	for i in range(int(t_final/step_size)):
		if method == "euler":
			y_nplusone = y_n + func(y_n)*step_size # euler method
		if method == "improved_euler":
			y_nplusone_hat = y_n + func(y_n)*step_size
			y_nplusone = y_n + (step_size/2)*(func(y_n) + func(y_nplusone_hat)) # improved euler method

		ys.append(y_nplusone)
		y_n = y_nplusone

	print("Absolute Error for {0} method: {1}").format(method, abs(analytical_func(xs[-1]) - ys[-1]))
	print("Relative Error for {0} method: {1}").format(method, abs(analytical_func(xs[-1]) - ys[-1])/analytical_func(xs[-1]))

	return xs, ys, analytical_func


def plot(xs, ys, imp_xs, imp_ys, analytical_func, eqn, style1="r", style2="b", style3="g"):
	plt.plot(xs, ys, style1, label="euler")
	plt.plot(imp_xs, imp_ys, style2, label="improved euler")
	plt.plot(xs, [analytical_func(x) for x in xs], style3, label="analytical")
	plt.legend(loc="upper left")
	plt.title(eqn + " for " + str(len(xs)-1) + " steps")
	plt.plot()
	plt.show()

# Plots for x' = x-x**2 10 steps
euler_x, euler_y, analytical_func = calculate(func1, analytical_func1, "euler", 0.5, ic1, 5)
imp_euler_x, imp_euler_y, _ = calculate(func1, analytical_func1, "improved_euler", 0.5, ic1, 5)
plot(euler_x, euler_y, imp_euler_x, imp_euler_y, analytical_func, "x' = x*(1-x)")

# Plots for x' = x-x**2 100 steps
euler_x, euler_y, analytical_func = calculate(func1, analytical_func1, "euler", 0.05, ic1, 5)
imp_euler_x, imp_euler_y, _ = calculate(func1, analytical_func1, "improved_euler", 0.05, ic1, 5)
plot(euler_x, euler_y, imp_euler_x, imp_euler_y, analytical_func, "x' = x*(1-x)")

# Plots for x' = 1-x**2 10 steps
euler_x, euler_y, analytical_func = calculate(func2, analytical_func2, "euler", 0.5, ic2, 5)
imp_euler_x, imp_euler_y, _ = calculate(func2, analytical_func2, "improved_euler", 0.5, ic2, 5)
plot(euler_x, euler_y, imp_euler_x, imp_euler_y, analytical_func, "x' = 1-x**2")

# Plots for x' = 1-x**2 100 steps
euler_x, euler_y, analytical_func = calculate(func2, analytical_func2, "euler", 0.05, ic2, 5)
imp_euler_x, imp_euler_y, _ = calculate(func2, analytical_func2, "improved_euler", 0.05, ic2, 5)
plot(euler_x, euler_y, imp_euler_x, imp_euler_y, analytical_func, "x' = 1-x**2")

