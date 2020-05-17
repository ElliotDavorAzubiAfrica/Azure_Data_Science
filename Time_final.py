import datetime
from datetime import datetime, timedelta


Start_time = input("Please enter the start time (hh:mm aa) :") 
try:
    h, m ,s = Start_time.split(':')
    Start_time_totalSeconds = int(h) * 3600 + int(m) * 60 + int(s)
    print("Your start time is :", Start_time )
except ValueError:
    print("Wrong value!!!")

End_time = input("Please enter the end time (hh:mm aa) :") 
try:
    h, m ,s = End_time.split(':')
    End_time_totalSeconds = int(h) * 3600 + int(m) * 60 + int(s)
    print("Your Stoppage Time is:",End_time)
except ValueError:
    print("Wrong value!!!")

if End_time_totalSeconds < Start_time_totalSeconds:
    Total_time=(Start_time_totalSeconds -End_time_totalSeconds)/3600
    print("You have worked for :",Total_time)
else:
    Total_time= (End_time_totalSeconds-Start_time_totalSeconds)/3600
    print("Your work duration in hours is :",Total_time)


pay_rate = float(input("Please enter your pay rate :") )
print("Your pay rate is  :", pay_rate )

Total_pay=Total_time*pay_rate
print("Your pay for the duration of work in US Dollars  is  ",Total_pay)