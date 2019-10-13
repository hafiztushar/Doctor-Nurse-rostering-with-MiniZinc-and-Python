import pymzn

print("Nurse/Doctor Rostering: \n "
      "1.Prepare a Nurse Roster. \n "
      "2.Prepare a Doctor Roster.\n")
choice = input("Enter Your Choice: ")

if choice == '1':
    print("Nurse Rostering: \n "
        "1.Prepare a Nurse Roster in which every nurse has an equal number of day, night and off shifts. \n "
        "2.Prepare a Nurse Roster(without ensuring equal number of day, night and off shifts.\n")
    choice_again = input("Enter Your Choice: ")
    if choice_again=='1':
            x=input("num of days to be rostered:")
            y=input("num of nurses:")
            p=input("Number of nurses required in a day shift:")
            q=input("Number of nurses required in a night shift:")
            r=input("Minimum number of night shift each nurse has to be available:")
            s = input("Minimum number of day shift each nurse has to be available:")
            t=r=input("Minimum number of off day each nurse gets:")

            f = open("nurse.dzn", "w+")
            f.write("num_days = %s; \n" % x)
            f.write("num_nurses = %s; \n" % y)
            f.write("req_day = %s; \n" % p)
            f.write("req_night = %s; \n" % q)
            f.write("min_night = %s; \n" % r)
            f.write("min_day = %s; \n" % s)
            f.write("min_off = %s; \n" % t)
            f.close()

            print("Resulted Nurse Roster:")
            solns = pymzn.minizinc('nurse_all_shifts_equal.mzn', 'nurse.dzn', output_mode='item')
            print(solns[0])

    elif choice_again == '2':
            x = input("num of days to be rostered:")
            y = input("num of nurses:")
            p = input("Number of nurses required in a day shift:")
            q = input("Number of nurses required in a night shift:")
            r = input("Minimum number of night shift each nurse has to be available:")
            s = input("Minimum number of day shift each nurse has to be available:")
            t = r = input("Minimum number of off day each nurse gets:")

            f = open("nurse.dzn", "w+")
            f.write("num_days = %s; \n" % x)
            f.write("num_nurses = %s; \n" % y)
            f.write("req_day = %s; \n" % p)
            f.write("req_night = %s; \n" % q)
            f.write("min_night = %s; \n" % r)
            f.write("min_day = %s; \n" % s)
            f.write("min_off = %s; \n" % t)
            f.close()

            print("Resulted Nurse Roster:")
            solns = pymzn.minizinc('nurse_all_shifts_not_equal.mzn', 'nurse.dzn', output_mode='item')
            print(solns[0])

elif choice == '2':
    print("Doctor Rostering: \n "
        "1.Prepare a Doctor Roster in which every doctor has an equal number of day, night and off shifts. \n "
        "2.Prepare a Doctor Roster(without ensuring equal number of day, night and off shifts.\n")
    choice_again = input("Enter Your Choice: ")
    if choice_again=='1':
            x=input("num of days to be rostered:")
            y=input("num of doctors:")
            p=input("Number of doctors required in a day shift:")
            q=input("Number of doctors required in a night shift:")
            r=input("Minimum number of night shift each doctor has to be available:")
            s = input("Minimum number of day shift each doctor has to be available:")
            t=r=input("Minimum number of off day each doctor gets:")

            f = open("doctor.dzn", "w+")
            f.write("num_days = %s; \n" % x)
            f.write("num_doctors = %s; \n" % y)
            f.write("req_day = %s; \n" % p)
            f.write("req_night = %s; \n" % q)
            f.write("min_night = %s; \n" % r)
            f.write("min_day = %s; \n" % s)
            f.write("min_off = %s; \n" % t)
            f.close()

            print("Resulted Doctor Roster:")
            solns = pymzn.minizinc('doctor_all_shifts_equal.mzn', 'doctor.dzn', output_mode='item')
            print(solns[0])

    elif choice_again == '2':
            x = input("num of days to be rostered:")
            y = input("num of doctors:")
            p = input("Number of doctors required in a day shift:")
            q = input("Number of doctors required in a night shift:")
            r = input("Minimum number of night shift each doctor has to be available:")
            s = input("Minimum number of day shift each doctor has to be available:")
            t = r = input("Minimum number of off day each doctor gets:")

            f = open("doctor.dzn", "w+")
            f.write("num_days = %s; \n" % x)
            f.write("num_doctors = %s; \n" % y)
            f.write("req_day = %s; \n" % p)
            f.write("req_night = %s; \n" % q)
            f.write("min_night = %s; \n" % r)
            f.write("min_day = %s; \n" % s)
            f.write("min_off = %s; \n" % t)
            f.close()

            print("Resulted Doctor Roster:")
            solns = pymzn.minizinc('doctor_all_shifts_not_equal.mzn', 'doctor.dzn', output_mode='item')
            print(solns[0])
