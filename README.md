# Doctor-nurse-rostering-with-MiniZinc

It is an optimized scheduling of nurses and doctors considering real life scenario and
following various constraints. 

Project consists of four different models.
	-Nurse rostering without equal number of shifts for each nurse.
	-Nurse rostering with equal number of shifts for each nurse.
	-Doctor rostering with equal number of shifts for each nurse.
	-Doctor rostering with equal number of shifts for each nurse.
Using python file Start.py user will give inputs of Number of nurses, 
doctors, days to be scheduled and lot more needed parameter.

Constraints:
	-Total nurses, doctors required in a day shift, night shift.
	-Total number of night shift, day shift, off days a nurse, doctor must perform.
	-Deterministic Finite Automation to ensure :
		-Each nurse is scheduled for each day as either: (d) on day shift, 
		(n) on night shift, or (o) off. 
		-In each four day period a nurse must have at least one day off, 
		and no nurse can be scheduled for 3 night shifts in a row.
