
from pymongo import MongoClient
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri) 

db = client.c4e

customers = db["customers"]
all_customers = list(customers.find())
events = 0
wom = 0 
ads = 0
for customer in all_customers:
    if customer['ref'] == 'events':
        events = events + 1
    elif customer['ref'] == 'wom':
        wom = wom + 1 
    else: 
        ads = ads + 1

print('events =', events)
print('wom = ', wom)
print('ads = ', ads)

ref_counts = [events,wom,ads]

ref_names = ["events" , "word of mouth" , "advertisements"]

pyplot.pie(ref_counts, labels = ref_names, autopct="%.1f%%", shadow=True, explode=(0,0.05,0.05))
pyplot.axis("equal")
pyplot.title("Data of 6969 customers of a marketing database.")
pyplot.show()