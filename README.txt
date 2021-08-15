dependencies:

python packages used in the code:

requests
datetime
time
ptyz
timezonefinder

Logic:

Get user input of latitutude nad longitude of the desired location 

Find the current date in the region based on latitude and longitude

Convert date found into unix timestamp

Decrement unix timestamp by 72000 seconds(22 hours) to get the time stamp of 4am 
in the region

Call the one call api 3 times 
	
	Call 1-Yesterday 4 am  (with time stamp of date-72000 seconds)
	Call 2-Day before yesterday 4 am (with time stamp decrement of 86400(1 day=86400 seconds) from the 
previous timestamp)
	
	Call 3-2 days before 4 am (with time stamp decrement of 86400(1 day=86400 seconds) from the 
previous timestamp)

During each API call parse through the response JSON and pull the current date("dt")
object and current pressure("pressure) object

Print the Pressure values with date and time during each api call

Instrcutions to run the program:

Step 1:Install all dependencies by using the commands below

pip install requests

pip install datetime

pip install time

pip install ptyz

pip install timezonefinder

Step 2: Run task1.py 

Step 3: Input latitude and longitude 








