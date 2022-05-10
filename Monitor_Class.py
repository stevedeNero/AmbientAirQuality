"""
Created on Wed May 3 2022

@author: S P DeNero
"""

class Monitor(object):
    """
    An object declaration for EPA Ambient monitors.
    """
#    def __init__(self, lat, long, aqs, poll): #Eventually need to add values (List? Dict?) of all pollutants with Valid or Invalid flags for each
    def __init__(self, lat, long, aqs):
        """
        initialize the location and identification of source
        """
        self.lat = lat
        self.long = long
        self.aqs = aqs

    def get_lat(self):
        return self.lat

    def get_long(self):
        return self.long

    def get_coordinates(self):
        return [self.lat, self.long]

    def get_aqs(self):
        return self.aqs

    def set_UTME(self,lat):
        assert len(self.lat) > 0, "Latitude in the Norther Hemisphere is Positive"
        self.lat = float(lat)

    def set_UTMN(self,long):
        assert len(self.long) < 0, "Longitude in the Western Hemisphere is Negative"
        self.long = float(long)

    def set_coordinates(self,lat,long):
        assert len(self.lat) > 0, "Latitude in the Norther Hemisphere is Positive"
        assert len(self.long) < 0, "Longitude in the Western Hemisphere is Negative"
        self.lat = float(lat)
        self.long = float(long)

    def set_aqs(self,aqs):
        assert len(self.aqs) == 9, "AQS IDs are 9 digits long"
        self.aqs = aqs

    def __str__(self):
        return self.aqs + " : [%0.3f, %0.3f]" % (self.lat, self.long)