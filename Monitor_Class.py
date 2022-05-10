"""
Created on Wed May 3 2022
Edits: 
Tues May 10 2022

@author: S P DeNero
"""
import math

class Monitor(object):
    """
    An object declaration for EPA Ambient monitors.
    """
#    def __init__(self, lat, long, aqs, poll): #Eventually need to add values (List? Dict?) of all pollutants with Valid or Invalid flags for each
    def __init__(self, aqsid=None, lat=None, long=None, site=None, county=None, DV_Pb=None):
        """
        A Monitor object has the following attributes:
        
        aqsid = EPA 9 digit AQS ID
        lat = monitor location latitude
        long = monitor location longitude 
        site = local site name
        county = monitor location county name

        Pollutants
        Pb = Either an float value of Latest Design Value (DV) of Lead concentrations, or "N/A" representing that there is no valid DV for this monitor-pollutant pairing
        """

        self.lat = lat
        self.long = long
        self.aqsid = aqsid
        self.site = site
        self.county = county
        self.DV_Pb = DV_Pb

    def get_lat(self):
        return self.lat

    def get_long(self):
        return self.long

    def get_coordinates(self):
        return [self.lat, self.long]

    def get_aqsid(self):
        return self.aqsid

    def get_site(self):
        return self.site

    def get_county(self):
        return self.county

    def get_pollDV_Pb(self):
        return self.DV_Pb

    def set_lat(self,lat):
        assert lat > 0 or math.isnan(lat), "Latitude in the Norther Hemisphere is Positive"
        self.lat = float(lat)

    def set_long(self,long):
        assert long < 0 or math.isnan(long), "Longitude in the Western Hemisphere is Negative"
        self.long = float(long)

    def set_coordinates(self,lat,long):
        assert lat > 0 or math.isnan(lat), "Latitude in the Norther Hemisphere is Positive"
        assert long < 0 or math.isnan(long), "Longitude in the Western Hemisphere is Negative"
        self.lat = float(lat)
        self.long = float(long)

    def set_aqsid(self,aqsid):
        #assert len(str(aqsid)) == 9, "AQS IDs are 9 digits long". Currently this assertion is failing because of Leading Zeroes.
        self.aqsid = aqsid
        
    def set_site(self,site):
        self.site = site

    def set_county(self,county):
        self.county = county

    def set_DV_Pb(self,DV_value):
        self.DV_Pb = DV_value

    # This is still To-be-Developed. Instead of a "set_DV_Pb" and "set_DV_(pollutant name)" method, just a single method that incorporates a PollName string variable.
    # def set_pollDV(self,Pollutant,DV_value):
    #     self.
    #     self.DV_Pb = DV_Pb

    def __str__(self):
        return str(self.aqsid) + ". " + self.site + " in " + self.county + " County at : [%0.3f, %0.3f]" % (self.lat, self.long)
