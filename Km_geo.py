import pandas as pd
df = pd.read_csv(r'C:\Users\akshaya\Downloads\food_coded.csv')

df=df[['cook','eating_out','employment','ethnic_food','exercise','fruit_day','income','on_off_campus','pay_meal_out',
      'sports','veggies_day']]
df = df.apply (pd.to_numeric, errors='coerce')
df = df.dropna()
print(df)


import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid") 
ax=sns.boxplot(order=["cook","eating_out","employment","ethnic_food","exercise","fruit_day","income","on_off_campus","pay_meal_out",
      "sports","veggies_day"], data=df)


ax.set_xticklabels(['cook','eating_out','employment','ethnic_food','exercise','fruit_day','income','on_off_campus','pay_meal_out',
      'sports','veggies_day'],rotation=45)
plt.show()

from sklearn.cluster import KMeans
import numpy as np
x = df.iloc[:, [6,1]].values
wcss = []
for i in range(1, 15):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,15), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
kmeans = KMeans(n_clusters=6, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(x)
plt.scatter(x[:,0],x[:,1],c = pred_y.astype(float))
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=150, c='red')
plt.show()

import json, requests
import pprint
url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
client_id ='SZ1RINU0PM3OKTESKD5LATONJTLCCN50DRAFOZYNE5PUOYNF',
client_secret='JF1HMAFKTZBRXTSGUC0C3T3MK1JH03YND4UYCEDTN0NHVQPI',
v='20180323',
ll='13.135727,77.572482',
query='food',
limit=100
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
data1=data['response']['groups'][0]['items']

              
import csv  
import io
f = io.open(r'C:\Users\akshaya\Downloads\new.csv', 'w', encoding="utf-8")
writer = csv.writer(f)
header = ['id','type', 'name','address','city','country','distance', 'lat','long', 'state',]
writer.writerow(header)

details=[]

for i in range(len(data1)):
 val1= data1[i]['venue']['categories'][0]['id']
 val2= data1[i]['venue']['categories'][0]['name']
 val3= data1[i]['venue']['name']
 ak = data1[i]['venue']['location']
 if 'address' in ak.keys():
        val4 = data1[i]['venue']['location']['address']
 else:
        val4="Nan"
 if 'city' in ak.keys():
        val5 = data1[i]['venue']['location']['city']
 else:
        val5="Nan"
 val6= data1[i]['venue']['location']['country'] 
 val7= data1[i]['venue']['location']['distance'] 
 val8= data1[i]['venue']['location']['lat'] 
 val9= data1[i]['venue']['location']['lng'] 
 if 'state' in ak.keys():
        val10= data1[i]['venue']['location']['state'] 
 else:
        val10= "Nan"
 contents = [val1,val2,val3,val4,val5,val6,val7,val8,val9,val10]
 details.append(contents)
#print(details) 
writer.writerows(details)
import pandas as pd
df1 = pd.read_csv(r'C:\Users\akshaya\Downloads\new.csv')
#df1.drop(df1[df1['distance'] > 10000].index, inplace = True)
df1.to_csv(r'C:\Users\akshaya\Downloads\output5.csv', index=False)

del params
del writer
del details 
f.close()
del f
del header

params = dict(
client_id ='SZ1RINU0PM3OKTESKD5LATONJTLCCN50DRAFOZYNE5PUOYNF',
client_secret='JF1HMAFKTZBRXTSGUC0C3T3MK1JH03YND4UYCEDTN0NHVQPI',
v='20180323',
ll='13.135727,77.572482',
query='groceries',
limit=100
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
data1=data['response']['groups'][0]['items']

              
import csv  
import io
f1 = io.open(r'C:\Users\akshaya\Downloads\newi.csv', 'w', encoding="utf-8")
writer = csv.writer(f1)
header = ['id','type', 'name','address','city','country','distance', 'lat','long', 'state',]
writer.writerow(header)

details=[]

for i in range(len(data1)):
 val1= data1[i]['venue']['categories'][0]['id']
 val2= data1[i]['venue']['categories'][0]['name']
 val3= data1[i]['venue']['name']
 ak = data1[i]['venue']['location']
 if 'address' in ak.keys():
        val4 = data1[i]['venue']['location']['address']
 else:
        val4="Nan"
 if 'city' in ak.keys():
        val5 = data1[i]['venue']['location']['city']
 else:
        val5="Nan"
 val6= data1[i]['venue']['location']['country'] 
 val7= data1[i]['venue']['location']['distance'] 
 val8= data1[i]['venue']['location']['lat'] 
 val9= data1[i]['venue']['location']['lng'] 
 if 'state' in ak.keys():
        val10= data1[i]['venue']['location']['state'] 
 else:
        val10= "Nan"
 contents = [val1,val2,val3,val4,val5,val6,val7,val8,val9,val10]
 details.append(contents)
#print(details) 
writer.writerows(details)
import pandas as pd
df1 = pd.read_csv(r'C:\Users\akshaya\Downloads\newi.csv')
#df1.drop(df1[df1['distance'] > 10000].index, inplace = True)
df1.to_csv(r'C:\Users\akshaya\Downloads\outputi5.csv', index=False)

import pandas as pd
import folium
op = pd.read_csv(r'C:\Users\akshaya\Downloads\final.csv')
print(op)
from sklearn.cluster import KMeans
import numpy as np
x = op.iloc[:, [2,3]].values
wcss = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,10), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(x)
plt.scatter(x[:,0],x[:,1])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=30, c='red')
plt.show()

locations = op[['lat', 'lng']]
locationlist = locations.values.tolist()

map = folium.Map(location=[13.133521,77.567135])
for point in range(0, len(locationlist)):
    folium.Marker(locationlist[point]).add_to(map)
map