# from numpy import number
import phonenumbers  
from phonenumbers import  geocoder
from test import correct_name
from test import umber
import folium

# number.py
from test import number




key="455ed48f2df6446faa7dec20b3911b16"

check_number=phonenumbers.parse(number)
number_location =geocoder.description_for_number(check_number,"en")
print(number_location)


from phonenumbers import carrier
service_provider =phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))


from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query=str(number_location)
result=geocoder.geocode(query)

lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)



map_location=folium.Map(location=[lat,lng],oom_start=9)
folium.Marker([lat,lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")








