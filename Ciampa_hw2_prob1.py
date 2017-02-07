import numpy as np
from decimal import Decimal

#input the velocity as a fraction of c and the distance in light-years
beta=float(input("Enter the speed at which you travel (fraction of c): "))
dist_inp=float(input("Enter the distance to the planet (in Light-years): "))

#speed of light in cm
c=3e10

#function that will calculate the time it takes for the ship to reach the planet observed from Earth.
def timeEarth(dist_inp,beta):
	dist=dist_inp*9.461e17  #puts light-years into cm
	vel=beta*c            #puts velocity into cm/s
	
	t_earth = dist/vel
	t_earth=t_earth/31536000.
	
	print("At",dist_inp,"Light-years...")
	print("The time it takes to travel there is",t_earth,"years for an observer on Earth.")
	return

#function that will calculate the time it takes for the ship to reach the planet observed by a passenger
def timeShip(dist_inp,beta):
	dist=dist_inp*9.461e17  #puts light-years into cm
	vel=beta*c            #puts velocity into cm/s
	gamma=1.0/(np.sqrt(1.0-(beta**2)))   #gamma factor accounts for the length contraction due to relativistic speeds in frame

	distance=dist/gamma
	t_ship=distance/vel
	t_ship=t_ship/31536000.
	
	print("At",dist_inp,"Light-years...")
	print("The time it takes to travel there is",t_ship,"sec for an observer on the spaceship.")
	return

#calling the functions using the inputs above
timeEarth(dist_inp,beta)
timeShip(dist_inp,beta)
