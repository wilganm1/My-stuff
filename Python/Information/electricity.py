	--------------Electronics & Electricity--------------

Voltage (V) - electric potential difference between 2 points. Volts
Current (I) - flow of electric charge. Amperage
Resistance (R) - opposition of flow. Ohms
Power (R) - work of electricity. Watts

	def voltage(I,R):
	  V = I * R
	
	def current(V,R):
	  I = V * R
	
	def resistance(V,I):
	  R = V/I



AC current - current that alternates directions. Happens because turbine spins. different orientations
DC current - Current that flows in one direction. Direct Current.

--------DC Power formulas--------
	def DCpower(V,I):
	  P = V * I
	
	def DCpowercr(I,R):
	  P = I**2 * R
	
	def DCpowervr(V,R):
	  P = V**2/R


Capacitor - stores electrical energy. C = Q/v
		C = capacitence (Farads)
		Q = charge
		v = voltage

	def capacitance(Q,V):
		C = Q/V

Conductance (G) siemens - measure of a material's ability to conduct electic current.
	def conductance(R):
		G = 1 / R

Electric charge (C) coloumbs - property of matter based on number of electrons. positive or negative.
	def charge(I,t):
		Q = I * t

Impedance (Z) - resistance of AC current. Ohms
	def impedance(R,X):
		Z = (R**2 + X**x)**-2

Frequency (Hz) - number of cycles of something in a unit of time. Hertz.
	def frequency(T):
		f = 1 / T
		
Time period (T) - duration to complete one cycle. seconds.
	def time_period(f):
		T = 1/f

		----------Components----------
Inductor - stores magnetic energy when current passed through it. Henry unit.
		
Diodes - one-way passage for electricity

Rectifier - converts AC current to DC current
Inverter - Converts DC to AC

Relay - electromagnetic switch that opens and closes voltage-free contacts.

Transformer - takes input voltage and changes to a different output

MOSFET - 

