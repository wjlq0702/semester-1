# Week 1.2, Session 2: Task 6
temp = int(input("Enter the temperature of the machine in Celsius"))
pressure = int(input("Enter the pressure of the machine in PSI:"))
operational_status = int(input("Enter the machine's operational status (1 for operating, 0 for stopped)"))

if temp > 80:
    print("Machine temperature is too high. We reccomend shutting down the machine.")

elif temp >= 50 and temp <=80:
    print("The temperature is within safe limits")
elif temp < 50:
    print("The temperature is low, no action is required")
else :
    print(" Error : Values inputted are not integers.")

if pressure > 100:
    print("High pressure detected. We reccomend the machine requires maintanence")
elif pressure   >= 50 and pressure <=100:
    print("Pressure is stable")
elif pressure < 70:
    print ("Pressure is low, system is operating normally")
else: 
    print(" Error : Values inputted are not integers.")

if operational_status == 1:
    if temp > 80 or pressure > 100:
        print("Machine running is unsafe. We reccomend shutting down the machine.")
    else: 
        print("Everything is normal")
elif operational_status == 0:
    print("Machine is not currently operating. No immediate action is needed")
else:
    print("Error: operational_status input is not a 0 or 1")