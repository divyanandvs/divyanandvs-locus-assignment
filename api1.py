import requests
import datetime
from datetime import date
import time
import datetime
import timezonefinder, pytz

lat=input("Enter latitude: ")
#type cast to float
lat=float(lat)
lon=input("Enter longtitude: ")
#type cast to float
lon=float(lon)

tf = timezonefinder.TimezoneFinder()

# From the lat/long, get the tz-database-style time zone name
timezone_str = tf.certain_timezone_at(lat=lat, lng=lon)

if timezone_str is None:
    print ("Could not determine the time zone")
else:
    # Find the current time in the given time zone
    timezone = pytz.timezone(timezone_str)
    dt = datetime.datetime.utcnow()
    
    dt=dt + timezone.utcoffset(dt)
    
    
    # Find the unix timestamp of the current date time in the given time zone
    timestamp = time.mktime(dt.timetuple())
    timestamp= int(timestamp)
    
    dt1=datetime.datetime.fromtimestamp(timestamp)
    

    #Extract only date from the cuurent date time in the given time zone
    dt1=dt1.strftime('%Y-%m-%d')
    
    #convert date time object to its string equivalent
    dt1=datetime.datetime.strptime(dt1, '%Y-%m-%d')
    

    #Find the unix timestamp equivalent for the current date(midnight)
    timestamp1 = time.mktime(dt1.timetuple())
    #Find the unix timestamp of 4am the previous day
    timestamp1=int(timestamp1) -72000
    #print (timestamp1)
print("Note:All dates,time denote local date and time of the region provided in input")
i=0
while i < 3:

    parameters = {
        "lat": lat,
        "lon": lon,
        "dt":timestamp1
    }
    response = requests.get("https://api.openweathermap.org/data/2.5/onecall/timemachine?appid=9501778cc8b528d4400fc94759a1912d",params=parameters)

    jsonResponse = response.json()
    
    #compute the datetime equivalent of the timestamp
    dt2=datetime.datetime.fromtimestamp(timestamp1)
    dt2=dt2.strftime('%Y-%m-%d %H:%M:%S')
    dt2=datetime.datetime.strptime(dt2, '%Y-%m-%d %H:%M:%S')
    
    
    
    
    print("On ",dt2," pressure level was",(jsonResponse["current"]["pressure"] )," mbar")
    
    
    #keep track of number of days
    i=i+1
    #go 24 hours back i.e 4am of the previous day
    timestamp1=timestamp1-86400

    
