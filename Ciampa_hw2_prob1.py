import numpy as np
from decimal import Decimal

#input the velocity as a fraction of c and the distance in light-years
beta=float(input("Enter the speed at which you travel (fraction of c): "))
dist_inp=float(input("Enter the distance to the planet (in Light-years): "))

#speed of light in cm
c=3e10

#function that will calculate the time it takes for the ship to reach the planet observed from Earth.
def timeEarth(dist_inp,beta):
	dist=dist_inp*9.5e18  #puts light-years into cm
	vel=beta*c            #puts velocity into cm/s
	
	t_earth = dist/vel
	
	print("At",dist_inp,"Light-years...")
	print("The time it takes to travel there is %.2E sec for an observer on Earth." % Decimal(t_earth))
	return

#function that will calculate the time it takes for the ship to reach the planet observed by a passenger
def timeShip(dist_inp,beta):
	dist=dist_inp*9.5e18  #puts light-years into cm
	vel=beta*c            #puts velocity into cm/s
	gamma=1.0/(np.sqrt(1.0-(beta**2)))   #gamma factor accounts for the length contraction due to relativistic speeds in frame

	distance=dist/gamma
	t_ship=distance/vel
	
	print("At",dist_inp,"Light-years...")
	print("The time it takes to travel there is %.2E sec for an observer on the spaceship." % Decimal(t_ship))
	return

#calling the functions using the inputs above
timeEarth(dist_inp,beta)
timeShip(dist_inp,beta)
