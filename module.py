
'''numeric module part 1:
    ___________________________________________________

1--number module:
the number module defines the numeric hierarchy(also known as "numeric tower"), it uses abstract base classes to categorise numbers


the hierarchy:
number-the root of the hierarchy
complex-number with real and imaginary parts
real-floating point numbers
rational-numbers that can be expressed as a fraction
integral-whole numbers(int)

2--math module:
the math module provides access to the mathematical functions defined by the C standard.
key features--
performance: functions are implemented in C, making them extremely fast.
precision: handles IEEE 754 floating point arithmetic
safety-provides tools to handle "not a number"(NaN) infinity

3--mathematical functions:
a.power and logarithmic functions:
used extensively in finance(compound interest) and data science

math.exp(x): returns e*2
mat.log(x, [base]): returns the logarithm in x
math.sqrt(x): return the square root of x

b.representation functions:
used for rounding and sign manipulation in UI/UX and billing system
math.ceil(x): rounds up the nearest integer
math.floor(x): rounds down to the nearest integer
math.isclose(a,b):checks of two values are nearly equal

c.trigonometric functions:
math.sin(x), math.cos(x)
math.degree(x)/, math.radians(x)

4--constants:
constants              description                              VALUE(approx)
math.pi                the mathematical constant pi             3.14159
math.e                 Euler's number                           2.71828
math.tau               the ratio of circumference to radius     6.28318
math.inf               the floating point positive infinity     inf
math.nan               a floating point "not a number" value    nan

ex- using constants and infinity to set bounds for risk threshold'''

'''numeric module part2--
____________________________________

1.cmath module (complex numbers):
complex numbers in py are written as 3+4j
the module orovides funs to convert between cartesian and polar coordinates'''


'''2.decimal module (decimal arithmetic):
the decimal module provides fixed-point and floating arithmetic with user-defined precision

feature                                  float(binary)                            decimal(base 10)
precision                                limited(53 bits)                         user-definable (default 28 places)
exactance                                0.1 is an approximation                  0.1 is exactly 0.2
usage                                    scientific simulations                   financial transaction, tax, billing'''



'''3.ftraction module:
    the fraction modle provides support for rtional number arthematic. it allows you yo represent numbers as anumerator and denominator (1/3),preventing and rounding
errors until absolute final step of a calculation.'''

from fractions import Fraction
task_a=Fraction(1,3)
task_b=Fraction(1,6)
remaining_capacity=1-(task_a+task_b)
print("capacity left for anothe rtask is:",remaining_capacity)


'''4.random and statistic module:
    the random module uses the mersenne twister algorithm to generate pseudo_random numbers.
    never use the random module for security purpose(for generating password)'''

 '''i)random module:'''
import random
print(random.random())  #returns the float value btw 0.0 to 1.0
print(random.randint(100,200)) #returns the integer btw ranges
list1=[2,6,1,7,9,2,5]
print(random.choice(list1)) #picks a single random element from list\tuple
print(random.shuffle(list1))
print(list1)
list2=[3,4,5,9,8]
print(random.sample(list1,2)) #picks a uique element from the samples
average_marks=60
variation=5
marks=random.gauss(average_marks,variation) #gauss
print(round(marks,2)) #returns a float based on a gauss distribution


  '''ii)statistic module:
code consept: measures central tendency

measures de
'''

import random import statistics
latencies=[random.guass(200,50)for_in range(100)
avg_latency=statistics.mean(latencies)
median_latency=statistics.median(latencies)
spread=statistics.stdev(latencies)
print(f"average response time:{avg_latency:.2f}ms")
print(f"median response time:{median_latency:.2f}ms")
print(f"standard deviationtime:{spread:.2f}ms")
































  
