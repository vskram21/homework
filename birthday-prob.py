import string 
import math
import fractions 

def power_two(pow):
	tempa = 1
	for ip in range(1, pow+1):
		tempa = 365*tempa
	return (tempa)

def numa(i):
	p= 365
	numa1 = 1
	for j in range (1,i+1):
		numa1 = p * numa1
		p = p - 1
	return (numa1)
	
	
for i in range(1,365):
	#vara = abs( (float(numa(i)) / float(pow(365,i) ) ) ) 
	#print 'The Value of Nume:', numa(i)  , ' \t Denom: ', power_two(i), '\n'
	#print 'The value for ',i,' is ' , vara , '\n' 
	print 'The value for ',i,' is ' ,  (float(numa(i)) / float(power_two(i) ) )  , '\n' 
