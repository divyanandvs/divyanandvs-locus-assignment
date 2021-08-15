Dependencies:

Python packages used in the code:

1.requests
2.datetime
3.time
4.ptyz
5.timezonefinder

Logic:

1.Get user input of latitutude nad longitude of the desired location 

2.Find the current date in the region based on latitude and longitude

3.Convert date found into unix timestamp

4.Decrement unix timestamp by 72000 seconds(22 hours) to get the time stamp of 4am 
in the region

5.Call the one call api 3 times 
	
	5.a.Call 1-Yesterday 4 am  (with time stamp of date-72000 seconds)
	5.b.Call 2-Day before yesterday 4 am (with time stamp decrement of 86400(1 day=86400 seconds) from the 
previous timestamp)
	
	5.c.Call 3-2 days before 4 am (with time stamp decrement of 86400(1 day=86400 seconds) from the 
previous timestamp)

6.During each API call parse through the response JSON and pull the current date("dt")
object and current pressure("pressure") object

7.Print the Pressure values with date and time during each api call

Instrcutions to run the program:

Step 1:Install all dependencies by using the commands below

pip install requests

pip install datetime

pip install time

pip install ptyz

pip install timezonefinder

Step 2: Run task1.py 

Step 3: Input latitude and longitude 

Sample input:
Enter latitude: 20
Enter longitude: -40

Sample output:
Note:All dates,time denote local date and time of the region provided in input
2021-08-14 04:00:00  pressure level was 1019  mbar
2021-08-13 04:00:00  pressure level was 1019  mbar
2021-08-12 04:00:00  pressure level was 1018  mbar


Scalability:

1.Code is scalable to n number of days historical weather if we have historical data of n number of days.
2.The number of days can be made to input by the user.








