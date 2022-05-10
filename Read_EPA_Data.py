'''
This module will read in the EPA's design values for the listed pollutants, and save the needed data to a "monitor" object.
'''
import pandas as pd
import math
from Monitor_Class import Monitor

file_path = "../AirQuality/EPA_DV/"
# excel_file_name = "pb_designvalues_2018_2020_final_05_24_21.xlsx"
excel_file_name = "example.xlsx"
excel_tab_name = "Table5. Site Status"
# print('Full Path Is: ', file_path+excel_file_name)
# in order to read/write Excel 2010, you need to "install openpyxl" module


def Start_Reading_Mon_Vals():
    """
    Initialize the set() of monitor objects 
    """
    MonitorDict = {}
    return MonitorDict

def read_mon_details(df,x):
    """
    Function to read the latitude, longitude, site details, AQS ID, and County Name of the monitor. 
    This is not pollutant-specific information.
    
    Input:
    df = dataframe from the excel file 
    x = current row index from readign the df

    Output:
    currentMon = Monitor Objct with lat, long, aqsid, site, and county values
    aqsid = a 9-digit long string to be used as the KEY value in the MonitorDict
    """
    currentMon = Monitor()
    currentMon.set_lat   (df.loc[x, "Site Latitude"])
    currentMon.set_long  (df.loc[x, "Site Longitude"])
    aqsid = str(int(df.loc[x,"AQS Site ID"]))
    while len(aqsid) < 9:
        aqsid = "0" + aqsid
    currentMon.set_aqsid (aqsid)
    site_name = df.loc[x, "Local Site Name"]
    if len(site_name) < 2:
        site_name = "(No Site Name)"
    currentMon.set_site  (site_name)
    currentMon.set_county(df.loc[x, "County Name"])

    return currentMon, aqsid

def read_Pb_mon(filePath, MonitorDict):
    """
    Function to read the EPA DV workbook for Lead (Pb) values.
    """
    excel_file_name = "pb_designvalues_2018_2020_final_05_24_21.xlsx"
    # excel_file_name = "example.xlsx"
    excel_tab_name = "Table5. Site Status"

    print('In read_Pb_vals. Full Path Is: ', filePath+excel_file_name)
    # in order to read/write Excel 2010, you need to "install openpyxl" module
    
    #there are 3 rows of header & spacing before the table begins.
    df = pd.read_excel(filePath+excel_file_name, excel_tab_name, skiprows=3)
    
    for x in df.index:

        if not math.isnan(df.loc[x,"AQS Site ID"]):

            if df.loc[x,"AQS Site ID"] not in MonitorDict:
                #Call read_mon_details to get site general information
                currentMon, aqsid = read_mon_details(df,x) 
            
            #Now Add the Pb Values. Doesnt matter if the monitor is already in the dictionary or not. This should eventually be a non-specific function also where you pass in the pollutant name and DV_Index which corresponds to the excel file column header
            DV_Index = "Valid             2018-2020 Design Value (μg/m3) [1,2]"
            try:
                DV_value = float((df.loc[x, DV_Index]))
                currentMon.set_DV_Pb(DV_value)
                #This method should not be pollutant specific. Should pass in (1) pollutant name and (2) DV value. Not sure how to do that yet.
                # currentMon.set_pollDV("Pb",DV_value)
            except ValueError:
                #Blank space represents "Not a Valid DV". Therefore
                DV_value = "N/A"
                currentMon.set_DV_Pb(DV_value)
                #This method should not be pollutant specific. Should pass in (1) pollutant name and (2) DV value. Not sure how to do that yet.
                # currentMon.set_pollDV("Pb",DV_value)
            print(currentMon, " Lead DV Value ", DV_value, type(DV_value))
            
            MonitorDict[aqsid] = currentMon

    return MonitorDict


#there are 3 rows of header & spacing before the table begins.
df = pd.read_excel(file_path+excel_file_name, excel_tab_name, skiprows=3)
# print(df['AQS Site ID'])

MonitorDict = Start_Reading_Mon_Vals()

MonitorDict = read_Pb_mon(file_path, MonitorDict)

# for x in df.index:

#     if not math.isnan(df.loc[x,"AQS Site ID"]):

#         if df.loc[x,"AQS Site ID"] not in MonitorDict:
#             #Call read_mon_details to get site general information
#             currentMon, aqsid = read_mon_details(df,x) 


#         #Now Add the Pb Values. Doesnt matter if the monitor is already in the dictionary or not. This should eventually be a non-specific function also where you pass in the pollutant name and DV_Index which corresponds to the excel file column header
#         DV_Index = "Valid             2018-2020 Design Value (μg/m3) [1,2]"
#         try:
#             DV_value = float((df.loc[x, DV_Index]))
#             currentMon.set_DV_Pb(DV_value)
#             #This method should not be pollutant specific. Should pass in (1) pollutant name and (2) DV value. Not sure how to do that yet.
#             # currentMon.set_pollDV("Pb",DV_value)
#         except ValueError:
#             #Blank space represents "Not a Valid DV". Therefore
#             DV_value = "N/A"
#             currentMon.set_DV_Pb(DV_value)
#             #This method should not be pollutant specific. Should pass in (1) pollutant name and (2) DV value. Not sure how to do that yet.
#             # currentMon.set_pollDV("Pb",DV_value)
#             print(DV_value,type(DV_value))

#         MonitorDict[aqsid] = currentMon
        
        

def read_CO_vals():
    """
    Function to read the EPA DV workbook for Carbon Monoxide (CO) values.
    """
    return None


def read_NO2_vals():
    """
    Function to read the EPA DV workbook for Nitrogen Dioxide (NO2) values.
    """
    return None


def read_PM10_vals():
    """
    Function to read the EPA DV workbook for PM10 values.
    """
    return None


def read_PM25_vals():
    """
    Function to read the EPA DV workbook for PM2.5 values.
    """
    return None


def read_O3_vals():
    """
    Function to read the EPA DV workbook for Ozone (O3) values.
    """
    return None
