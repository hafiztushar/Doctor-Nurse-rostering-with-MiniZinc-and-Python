%doctor rostering

include "regular.mzn";

int: num_doctors;                    %number of doctors to be scheduled
set of int: DOCTORS = 1..num_doctors;
int: num_days;                      %number of days the roster to be made for
set of int: DAYS = 1..num_days;     
set of int: sec_doctor= 1..(num_doctors-1);

int: req_day;                       %number of doctors required for a day shift
int: req_night;                     %number of doctors required for a night shift
int: min_night;                     %minimum night shifts a doctor has to perform  
int: min_day;                       %minimum day shifts a doctor has to perform
int: min_off;                       %minimum day shifts a doctor has to perform

int: S = 3;                         %shifts number
set of int: SHIFTS = 1..S; 
int: d = 1;
int: n = 2;
int: o = 3;
array[SHIFTS] of string: name = ["d","n","o"];

int: Q = 6;                         %set of all states for DFA
int: q0 = 1;                        %initial state
set of int: STATES = 1..Q;

%Deterministic finite automaton (DFA)
%Each doctor is scheduled for each day as either: (d) on day shift, (n) on night shift, or (o) off. 
%In each four day period a doctor must have at least one day off, and no doctor can be scheduled for 3 night shifts in a row

array[STATES,SHIFTS] of int: t =
     [| 2, 3, 1    % state 1
      | 4, 4, 1    % state 2
      | 4, 5, 1    % state 3
      | 6, 6, 1    % state 4
      | 6, 0, 1    % state 5
      | 0, 0, 1|]; % state 6 

array[DOCTORS,DAYS] of var SHIFTS: roster;     %Roster Declared


% Makin gsure minimum number of doctors required for both shifts are availbale
constraint forall(j in DAYS)(
	       sum(i in DOCTORS)(bool2int(roster[i,j] == d)) == req_day /\
               sum(i in DOCTORS)(bool2int(roster[i,j] == n)) == req_night
	   );
	   
	   

%Using DFA making sure of the states of shifts of a doctor and that each doctor has to stay a minimum number of nights 
constraint forall(i in DOCTORS)(
	       regular( [roster[i,j] | j in DAYS], Q, S, t, q0, STATES) /\
	       sum(j in DAYS)(bool2int(roster[i,j] == n)) >= min_night
	   );
%Using DFA making sure of the states of shifts of a doctor and that each doctor has to stay a minimum number of days 
constraint forall(i in DOCTORS)(
	       regular( [roster[i,j] | j in DAYS], Q, S, t, q0, STATES) /\
	       sum(j in DAYS)(bool2int(roster[i,j] == d)) >= min_day
	   );
	   
%Using DFA making sure of the states of shifts of a doctor and that each doctor gets a minimum off days
constraint forall(i in DOCTORS)(
	    regular( [roster[i,j] | j in DAYS], Q, S, t, q0, STATES) /\
	       sum(j in DAYS)(bool2int(roster[i,j] == o)) >= min_off
	   );
	   
	   
	   

%using to make sure for each doctor there is equal number of day shifts
constraint forall(i in sec_doctor)(
	        sum(j in DAYS)(bool2int(roster[i,j] == d)) == sum(j in DAYS)(bool2int(roster[i+1,j] == d)) 
	   );
	   
%using to make sure for each doctor there is equal number of night shift
constraint forall(i in sec_doctor)(
	        sum(j in DAYS)(bool2int(roster[i,j] == n)) == sum(j in DAYS)(bool2int(roster[i+1,j] == n)) 
	   );	   
	   
%using to make sure for each doctor there is equal number of off days
constraint forall(i in sec_doctor)(
              sum(j in DAYS)(bool2int(roster[i,j] == o)) == sum(j in DAYS)(bool2int(roster[i+1,j] == o)) 
	   );




solve satisfy;	      	             

output [ name[fix(roster[i,j])] ++ if j==num_days then "\n" else " " endif
       | i in DOCTORS, j in DAYS ]; 