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

def read_pb_mon(filePath, MonitorDict):
    """
    Function to read the EPA DV workbook for Lead (Pb) values.
    Input:
    filePath - string containing where to find the Lead (Pb) DV file from EPA website. This is already downloaded. Updated once per year.
    MonitorDict - Dictionary containing all of the monitor listings encountered so far.
        The dictionary key is the AQS ID
        The dictionary value is a Monitor object
    Output:
    MonitorDict updated with all Lead (Pb) DV listings
    """
    # excel_file_name = "example.xlsx"
    excel_file_name = "pb_designvalues_2018_2020_final_05_24_21.xlsx"
    excel_tab_name = "Table5. Site Status"
    DV_Index = "Valid             2018-2020 Design Value (μg/m3) [1,2]"

    # print('In read_Pb_vals. Full Path Is: ', filePath+excel_file_name)
    # in order to read/write Excel 2010, you need to "install openpyxl" module
    
    
    #there are 3 rows of header & spacing before the table begins.
    df = pd.read_excel(filePath+excel_file_name, excel_tab_name, skiprows=3)
    
    for x in df.index:

        if not math.isnan(df.loc[x,"AQS Site ID"]):

            aqsid = str(int(df.loc[x, "AQS Site ID"]))
            while len(aqsid) < 9:
                aqsid = "0" + aqsid

            if df.loc[x,"AQS Site ID"] not in MonitorDict:
                #Call read_mon_details to get site general information
                currentMon, aqsid = read_mon_details(df,x) 
            
            else: #current monitor is already in the dictionary
                currentMon = MonitorDict[aqsid]

            #Now Add the Pb Values. Doesnt matter if the monitor is already in the dictionary or not. This should eventually be a non-specific function also where you pass in the pollutant name and DV_Index which corresponds to the excel file column header
            
            try:
                DV_value = float((df.loc[x, DV_Index]))
                currentMon.set_DV_pb(DV_value)
                #This method should not be pollutant specific. Should pass in (1) pollutant name and (2) DV value. Not sure how to do that yet.
                # currentMon.set_pollDV("Pb",DV_value)
            except ValueError:
                #Blank space represents "Not a Valid DV". Therefore
                DV_value = "N/A"
                currentMon.set_DV_pb(DV_value)
                #This method should not be pollutant specific. Should pass in (1) pollutant name and (2) DV value. Not sure how to do that yet.
                # currentMon.set_pollDV("Pb",DV_value)
            # print(currentMon, " Lead DV Value ", DV_value)
            
            MonitorDict[aqsid] = currentMon

    return MonitorDict

def read_o3_mon(filePath, MonitorDict):
    """
    Function to read the EPA DV workbook for Ozone (O3) values.
    Input:
    filePath - string containing where to find the Ozone DV file from EPA website. This is already downloaded. Updated once per year.
    MonitorDict - Dictionary containing all of the monitor listings encountered so far.
        The dictionary key is the AQS ID
        The dictionary value is a Monitor object
    Output:
    MonitorDict updated with all Ozone DV listings
    """
    excel_file_name = "o3_designvalues_2018_2020_final_05_11_21.xlsx"
    excel_tab_name = "Table5. Site Status"
    DV_Index = "Valid            2018-2020 Design Value (ppm) [1,2]"    

    #there are 3 rows of header & spacing before the table begins.
    df = pd.read_excel(filePath+excel_file_name, excel_tab_name, skiprows=3)
    
    for x in df.index:

        if not math.isnan(df.loc[x,"AQS Site ID"]):

            aqsid = str(int(df.loc[x, "AQS Site ID"]))
            while len(aqsid) < 9:
                aqsid = "0" + aqsid

            if df.loc[x,"AQS Site ID"] not in MonitorDict:
                #Call read_mon_details to get site general information
                currentMon, aqsid = read_mon_details(df,x) 
                # print("New monitor in ozone file, was not in Pb lead file")

            else: #current monitor is already in the dictionary
                currentMon = MonitorDict[aqsid]

            #Now Add the o3 Values. Doesnt matter if the monitor is already in the dictionary or not. This should eventually be a non-specific function also where you pass in the pollutant name and DV_Index which corresponds to the excel file column header

            try:
                DV_value = float((df.loc[x, DV_Index]))
                #Unlike in the Pb workbook, in the Ozone workbook the blanks are coming back as "nan", but is converting to float without error. How? 
                if math.isnan(DV_value):
                    DV_value = "N/A"
                else:
                    currentMon.set_DV_o3(DV_value)
                
                # currentMon.set_pollDV("o3",DV_value)
            except ValueError:
                #Blank space represents "Not a Valid DV". Therefore
                # print("DV Value is throwing an error with conversion to float")
                DV_value = "N/A"
                currentMon.set_DV_o3(DV_value)
                
                # currentMon.set_pollDV("Pb",DV_value)
            # print(currentMon, " Ozone DV Value ", DV_value)
            
            MonitorDict[aqsid] = currentMon


    return MonitorDict

def read_no2_mon(filePath, MonitorDict):
    """
    Function to read the EPA DV workbook for Nitrogen Dioxide (NO2) values.

    Input:
    filePath - string containing where to find the NO2 DV file from EPA website. This is already downloaded. Updated once per year.
    MonitorDict - Dictionary containing all of the monitor listings encountered so far.
        The dictionary key is the AQS ID
        The dictionary value is a Monitor object
    Output:
    MonitorDict updated with all NO2 DV listings
    """
    excel_file_name = "no2_designvalues_2018_2020_final_05_21_21.xlsx"
    annual_excel_tab_name = "Table5a. Site Status Annual"
    annual_DV_Index = "Valid 2020 Annual Design Value (ppb) [1,2]"
    hourly_excel_tab_name = "Table5b. Site Status 1-hour"
    hourly_DV_Index = "Valid               2018-2020               1-hour Design Value (ppb) [1,2]"


    # Read & Save Annual NO2 DV Values

    # there are 3 rows of header & spacing before the table begins.
    df = pd.read_excel(filePath + excel_file_name, annual_excel_tab_name, skiprows=3)

    for x in df.index:

        if not math.isnan(df.loc[x, "AQS Site ID"]):

            aqsid = str(int(df.loc[x, "AQS Site ID"]))
            while len(aqsid) < 9:
                aqsid = "0" + aqsid

            if aqsid not in MonitorDict:

                # Call read_mon_details to get site general information
                currentMon, aqsid = read_mon_details(df, x)
                # print("New monitor in ozone file, was not in Pb lead file")

            else: #current monitor is already in the dictionary
                currentMon = MonitorDict[aqsid]

            # Now Add the NO2 Annual Values. Doesnt matter if the monitor is already in the dictionary or not. This should eventually be a non-specific function also where you pass in the pollutant name and DV_Index which corresponds to the excel file column header
            try:
                DV_value = float((df.loc[x, annual_DV_Index]))

                if math.isnan(DV_value):
                    DV_value = "N/A"
                else:
                    currentMon.set_DV_no2_an(DV_value)

            except ValueError:
                # Blank space represents "Not a Valid DV". Therefore
                # print("DV Value is throwing an error with conversion to float")
                DV_value = "N/A"
                currentMon.set_DV_no2_an(DV_value)

            MonitorDict[aqsid] = currentMon

    # Read & Save 1-Hour NO2 DV Values
    # there are 3 rows of header & spacing before the table begins.
    df = pd.read_excel(filePath + excel_file_name, hourly_excel_tab_name, skiprows=3)

    for x in df.index:

        if not math.isnan(df.loc[x, "AQS Site ID"]):

            aqsid = str(int(df.loc[x, "AQS Site ID"]))
            while len(aqsid) < 9:
                aqsid = "0" + aqsid

            if aqsid not in MonitorDict:

                # Call read_mon_details to get site general information
                currentMon, aqsid = read_mon_details(df, x)

            else:  # current monitor is already in the dictionary
                currentMon = MonitorDict[aqsid]

            # Now Add the NO2 1-hour Values. Doesnt matter if the monitor is already in the dictionary or not. This should eventually be a non-specific function also where you pass in the pollutant name and DV_Index which corresponds to the excel file column header
            try:
                DV_value = float((df.loc[x, hourly_DV_Index]))

                if math.isnan(DV_value):
                    DV_value = "N/A"

                else:
                    currentMon.set_DV_no2_hr(DV_value)

            except ValueError:
                # Blank space represents "Not a Valid DV". Therefore
                # print("DV Value is throwing an error with conversion to float")
                DV_value = "N/A"
                currentMon.set_DV_no2_hr(DV_value)

            MonitorDict[aqsid] = currentMon

    return MonitorDict

def read_pm25_mon(filePath, MonitorDict):
    """
    Function to read the EPA DV workbook for PM2.5 values.

    Input:
    filePath - string containing where to find the PM2.5 DV file from EPA website. This is already downloaded. Updated once per year.
    MonitorDict - Dictionary containing all of the monitor listings encountered so far.
        The dictionary key is the AQS ID
        The dictionary value is a Monitor object
    Output:
    MonitorDict updated with all PM2.5 DV listings
    """
    excel_file_name = "pm25_designvalues_2018_2020_final_05_24_21.xlsx"
    annual_excel_tab_name = "Table5a. Site Status Ann"
    annual_DV_Index = "Valid           2018-2020 Design Value (μg/m3) [1,2,3]"
    hourly_excel_tab_name = "Table5b. Site Status 24hr"
    hourly_DV_Index = "Valid           2018-2020 Design Value (μg/m3) [1,2,3]"


    # Read & Save Annual NO2 DV Values

    # there are 3 rows of header & spacing before the table begins.
    df = pd.read_excel(filePath + excel_file_name, annual_excel_tab_name, skiprows=3)

    for x in df.index:

        if not math.isnan(df.loc[x, "AQS Site ID"]):

            aqsid = str(int(df.loc[x, "AQS Site ID"]))
            while len(aqsid) < 9:
                aqsid = "0" + aqsid

            if aqsid not in MonitorDict:

                # Call read_mon_details to get site general information
                currentMon, aqsid = read_mon_details(df, x)
                # print("New monitor in ozone file, was not in Pb lead file")

            else: #current monitor is already in the dictionary
                currentMon = MonitorDict[aqsid]

            # Now Add the NO2 Annual Values. Doesnt matter if the monitor is already in the dictionary or not. This should eventually be a non-specific function also where you pass in the pollutant name and DV_Index which corresponds to the excel file column header
            try:
                DV_value = float((df.loc[x, annual_DV_Index]))

                if math.isnan(DV_value):
                    DV_value = "N/A"
                else:
                    currentMon.set_DV_pm25_an(DV_value)

            except ValueError:
                # Blank space represents "Not a Valid DV". Therefore
                # print("DV Value is throwing an error with conversion to float")
                DV_value = "N/A"
                currentMon.set_DV_pm25_an(DV_value)

            MonitorDict[aqsid] = currentMon

    # Read & Save 24-Hour PM2.5 DV Values
    # there are 3 rows of header & spacing before the table begins.
    df = pd.read_excel(filePath + excel_file_name, hourly_excel_tab_name, skiprows=3)

    for x in df.index:

        if not math.isnan(df.loc[x, "AQS Site ID"]):

            aqsid = str(int(df.loc[x, "AQS Site ID"]))
            while len(aqsid) < 9:
                aqsid = "0" + aqsid

            if aqsid not in MonitorDict:

                # Call read_mon_details to get site general information
                currentMon, aqsid = read_mon_details(df, x)

            else:  # current monitor is already in the dictionary
                currentMon = MonitorDict[aqsid]

            # Now Add the NO2 1-hour Values. Doesnt matter if the monitor is already in the dictionary or not. This should eventually be a non-specific function also where you pass in the pollutant name and DV_Index which corresponds to the excel file column header
            try:
                DV_value = float((df.loc[x, hourly_DV_Index]))

                if math.isnan(DV_value):
                    DV_value = "N/A"

                else:
                    currentMon.set_DV_pm25_hr(DV_value)

            except ValueError:
                # Blank space represents "Not a Valid DV". Therefore
                # print("DV Value is throwing an error with conversion to float")
                DV_value = "N/A"
                currentMon.set_DV_pm25_hr(DV_value)

            MonitorDict[aqsid] = currentMon

    return MonitorDict



MonitorDict = Start_Reading_Mon_Vals()
# print(MonitorDict["011011002"])
MonitorDict = read_pb_mon(file_path, MonitorDict)
# print(MonitorDict.get("011011002","DNE"))
MonitorDict = read_o3_mon(file_path, MonitorDict)
# print(MonitorDict.get("011011002","DNE"))
MonitorDict = read_no2_mon(file_path, MonitorDict)
MonitorDict = read_pm25_mon(file_path, MonitorDict)


print(MonitorDict.get("010730023","DNE"))
print(MonitorDict.get("060010015","DNE"))
