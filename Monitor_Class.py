"""
Created on Wed May 3 2022

@author: S P DeNero
"""
import math
from StateAbbrv import us_state_to_abbrev

class Monitor(object):
    """
    An object declaration for EPA Ambient monitors.
    """
#    def __init__(self, lat, long, aqs, poll): #Eventually need to add values (List? Dict?) of all pollutants with Valid or Invalid flags for each
#    def __init__(self, aqsid=None, lat=None, long=None, site=None, county=None, DVs = {DV_pb:"N/A", DV_o3:"N/A", DV_no2_an:"N/A", DV_no2_hr:"N/A",DV_pm2_an:"N/A",DV_pm25_hr:"N/A"}):
    def __init__(self, aqsid=None, lat=None, long=None, site=None, county=None, state=None, DV_pb="N/A", DV_o3="N/A", DV_so2_1="N/A",  DV_so2_3="N/A",  DV_no2_an="N/A", DV_no2_hr="N/A",  DV_pm25_an="N/A", DV_pm25_hr="N/A"):
        """
        A Monitor object has the following attributes:
        
        aqsid = EPA 9 digit AQS ID
        lat = monitor location latitude
        long = monitor location longitude 
        site = local site name
        county = monitor location county name
        state = stante name (Abbrev.)

        Pollutants
        pb = Either a float value of Latest Design Value (DV) of Lead concentrations, or "Not Valid"
        o3 = Either a float value of Latest Design Value (DV) of Ozone concentrations, or "Not Valid"
        no2 = NO2 has two design values: 1-hour average and annual average.
            Both will have either a float value of Latest Design Value (DV) of NO2 concentrations, or "Not Valid", for each NO2 entry
        pm2.5 = pm2.5 has two design values: 24-hour average and annual average.
            Both will have either a float value of Latest Design Value (DV) of NO2 concentrations, or "Not Valid", for each PM2.5 entry
        """

        self.lat = lat
        self.long = long
        self.aqsid = aqsid
        self.site = site
        self.county = county
        self.state = state
        
        
        self.DV_pb = DV_pb
        self.DV_o3 = DV_o3
        self.DV_no2_an = DV_no2_an
        self.DV_no2_hr = DV_no2_hr
        self.DV_so2_1 = DV_so2_1
        self.DV_so2_3 = DV_so2_3
        self.DV_pm25_an = DV_pm25_an
        self.DV_pm25_hr = DV_pm25_hr

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

    def get_state(self):
        return self.state

    def get_pollDV_pb(self):
        return self.DV_pb

    def get_pollDV_o3(self):
        return self.DV_o3

    def get_pollDV_so2_1hr(self):
        return self.DV_so2_1

    def get_pollDV_so2_3hr(self):
        return self.DV_so2_3

    def get_pollDV_no2_an(self):
        return self.DV_no2_an

    def get_pollDV_no2_hr(self):
        return self.DV_no2_hr

    def get_pollDV_pm25_an(self):
        return self.DV_pm25_an

    def get_pollDV_pm25_hr(self):
        return self.DV_pm25_hr

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

    def set_state_name(self,state):
        assert state in us_state_to_abbrev, "Misspelled or Mis-identified state name: "+state
        self.state = us_state_to_abbrev[state]

    def set_state_abbrv(self,state):
        self.state = state

    def set_DV_pb(self,DV_value):
        self.DV_pb = DV_value

    def set_DV_o3(self, DV_value):
        self.DV_o3 = DV_value

    def set_DV_so2_1(self, DV_value):
        self.DV_no2_an = DV_value

    def set_DV_so2_3(self, DV_value):
        self.DV_no2_hr = DV_value

    def set_DV_no2_an(self, DV_value):
        self.DV_no2_an = DV_value

    def set_DV_no2_hr(self, DV_value):
        self.DV_no2_hr = DV_value

    def set_DV_pm25_an(self, DV_value):
        self.DV_pm25_an = DV_value

    def set_DV_pm25_hr(self, DV_value):
        self.DV_pm25_hr = DV_value

    # def set_pollDV(self,Pollutant,DV_value):
    #     self.
    #     self.DV_Pb = DV_Pb

    def report(self):
        return str(self.aqsid) + "!" + \
               str(self.lat) + "!" + \
               str(self.long) + "!" + \
               str(self.site) + "!" + \
               str(self.county) + "!" + \
               str(self.state) + "!" + \
               str(self.DV_pb) + "!" + \
               str(self.DV_o3) + "!" + \
               str(self.DV_so2_1) + "!" + \
               str(self.DV_so2_3) + "!" + \
               str(self.DV_no2_an) + "!" + \
               str(self.DV_no2_hr) + "!" + \
               str(self.DV_pm25_an) + "!" + \
               str(self.DV_pm25_hr)

    def __dir__(self):
        return ['aqsid', 'lat', 'long', 'site', 'county', 'state', 'DV_pb', 'DV_o3', 'DV_so2_1', 'DV_so2_3', 'DV_no2_an', 'DV_no2_hr',  'DV_pm25_an', 'DV_pm25_hr']

    def __str__(self):
        return str(self.aqsid) + ". " + self.site + " in " + self.county + \
               " County at : [%0.3f, %0.3f]" % (self.lat, self.long) + \
               "\n Lead DV " + str(self.DV_pb) + \
               "\n Ozone DV " + str(self.DV_o3) + \
               "\n 1-hour SO2 DV " + str(self.DV_so2_1) + \
               "\n 3-Hour SO2 DV " + str(self.DV_so2_3) + \
               "\n Annual NO2 DV " + str(self.DV_no2_an) + \
               "\n 1-Hour NO2 DV " + str(self.DV_no2_hr) + \
               "\n Annual PM2.5 DV " + str(self.DV_pm25_an) + \
               "\n 24-Hour PM2.5 DV " + str(self.DV_pm25_hr)
