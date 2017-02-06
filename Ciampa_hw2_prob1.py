import numpy as np
import matplotlib.pyplot as plt

vel_inp=float(input("Enter the speed at which you travel (fraction of c): "))
dist_inp=float(input("Enter the distance to the planet (in Light-years): "))

gamma=1.0/(np.sqrt(1.0-(vel_inp**2)))


vel=vel_inp*3e10      #puts velocity into cm/s

##Rest frame of an observer on Earth.
#t_earth=dist/vel
#
##Passenger on spaceship
#dist_spaceship=dist/gamma
#t_spaceship=dist_spaceship/vel

def timeEarth(dist_inp,vel_input):
	dist=dist_inp*9.5e18  #puts light-years into cm
	t_earth = dist_input/vel_input
	print("At",dist_input,"")
	print("The time it takes to travel there is",t_earth, " sec for an observer on Earth.")
	return

def timeShip(dist_inp,vel_input):
	dist=dist_inp*9.5e18  #puts light-years into cm
	distance=dist_input/gamma
	t_ship=distance/vel_input
	print("The time it takes to travel there is",t_ship, " sec for an observer on the spaceship.")
	return

timeEarth(dist,vel)
timeShip(dist,vel)

timeEarth(10.,0.9)
timeShip(10.,0.9)