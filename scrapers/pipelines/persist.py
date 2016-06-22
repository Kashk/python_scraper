# -*- coding: utf-8 -*- 
from scrapers.database.tables import *

class Persist(object):
    def process_item(self, item, spider):
        s = session()

        property_id = s.query(Home).filter(Home.link == item['link']).all()

        if (not len(property_id)):
            h = Home(title = item['title'],
                    owner_name = item['owner_name'],
                    link = item['link'],
                    description = item['description'],
                    sleeps = item['sleeps'],
                    bedrooms = item['bedrooms'],
                    bathrooms = item['bathrooms'],
                    property_type = item['property_type']
                    )
            s.add(h)
            s.commit()
            property_id = h.id
        else:
            property_id = property_id[0].id
            


        for location in item['location']:
            location_id = s.query(Locations).filter(Locations.name == location).all()
            if(not len(location)):
                l = Locations(name = location)
                s.add(l)
                s.commit()
                location_id = l.id
            else:
                location_id = location_id[0].id

            print "Property id is %s" % property_id
            print "Location id is %s" % location_id
            pl = PropertyLocations(property_id = property_id, location_id = location_id)
            s.add(pl)
            s.commit()

