from mlab import river_collection

river_a = list(river_collection.find({'continent': 'Africa'}))
print(river_a)
    
river_sa = list(river_collection.find())
for river in river_sa :
  if river['continent'] == 'S. America':
    if river['length'] < 1000 :
      print(river)