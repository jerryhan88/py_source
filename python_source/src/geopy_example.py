
from geopy.distance import vincenty, VincentyDistance


p1 = (1.276772,103.612184)
p2 = (1.383266,103.965440)

NORTH, EAST, SHOUTH, WEST = 0, 90, 180, 270
mover = VincentyDistance(kilometers=1)

p3 = mover.destination(point=p1, bearing=EAST)
p4 = mover.destination(point=p1, bearing=SHOUTH)



import folium
cp = ((p1[0] + p2[0]) / float(2), (p1[1] + p2[1]) / float(2))
map_osm = folium.Map(location=[cp[0], cp[1]], zoom_start=11)
map_osm.add_children(folium.PolyLine(locations=[(p1[0], p1[1]), (p2[0], p2[1])], weight=0.5))

for p, label in [(p1, 'p1'), (p2, 'p2'), (cp, 'Distance (p1, p2): %f m' % vincenty(p1, p2).meters), (p3,'p3 (1km East from p1)'), (p4,'p4 (1km South from p1)')]:
	folium.Marker((p[0], p[1]), popup=label).add_to(map_osm)


map_osm.save('geopy_example.html')


