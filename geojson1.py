import urllib.parse  
import urllib.request
import json  

serviceurl = 'http://python-data.dr-chuck.net/geojson?'  

address = input('Enter location: ')  
url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})  
print ('Retrieving', url)
uh = urllib.request.urlopen(url)  
data = uh.read()  
print ('Retrieved',len(data),'characters')
#print(data)
try: js = json.loads(str(data))  
except: js = None  
print (js)
if 'status' not in js or js['status'] != 'OK':  
  print ('==== Failure To Retrieve ====')  
  print (data)
 
placeid = js["results"][0]["place_id"]  
print ('Place ID ', placeid)