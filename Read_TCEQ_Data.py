'''
This file reads in data from the TCEQ monitoring network website for two monitors near the user's home in Austin Texas

Monitor 171, located on Webberville Road, reports PM2.5 data
Monitor 1619, located near Lady Bird Lake, reports Ozone (O3) data

'''
#import requests
#from bs4 import BeautifulSoup
import pandas as pd

pm25_vals = {}
o3_vals = {}

pm25_url = "https://www.tceq.texas.gov/cgi-bin/compliance/monops/daily_summary.pl?cams=171"
o3_url   = "https://www.tceq.texas.gov/cgi-bin/compliance/monops/daily_summary.pl?cams=1619"

# mon_url = ["https://www.tceq.texas.gov/cgi-bin/compliance/monops/daily_summary.pl?cams=171",
#            "https://www.tceq.texas.gov/cgi-bin/compliance/monops/daily_summary.pl?cams=1619"]
# for url in mon_url[0:1]: #eventually loop, but for now we're just going to call both

# We use the Pandas URL reader, which skips a lot of the other manipulation necessary. Dont need to use BS4 or Requests.
# downloaded_html = requests.get(url)
# soup = BeautifulSoup(downloaded_html.text, 'html.parser')


# Read first URL. Get the hours and the PM2.5 values from this monitor URL listing.
df = pd.read_html(pm25_url, attrs={'border': '1'}, flavor='bs4')
df_vals = df[0].copy()


# These tables have Merged Cells in the header, so they have "MultiIndexed column headers.
# So the [1] index column is ('Morning', 'Mid' ) and the [2] index column is ('Morning' , '1:00')
# The first value is "Parameter measured", as is the n-1 column value.
Hours_List = [time[1] for time in df_vals.columns[1:len(df_vals.columns)-2]]
# print(Hours_List)


#TODO figure out how to get the script to search for keywords. i.e. "Find the term 'Ozone' in table". Then you can create a loop instead of this current rigid flat structure.
PM25_List = [df_vals.iloc[4,x+1] for x in range(len(Hours_List))]
# print(PM25_List)


# Read second URL for the Ozone values.
df = pd.read_html(o3_url, attrs={'border': '1'}, flavor='bs4')
df_vals = df[0].copy()

O3_List = [df_vals.iloc[0,x+1] for x in range(len(Hours_List))]
# print(O3_List)



# Current_Mon = "CAMS"+url.rsplit("=")[1]

df_reporting = pd.DataFrame(columns=['Hour', 'PM2.5', 'O3'])
df_reporting['Hour'] = Hours_List
df_reporting['PM2.5'] = PM25_List
df_reporting['O3'] = O3_List

# print(df_reporting.head())

# print("Printing 'to_html'")
# print(df_reporting.to_html())

# So now we have a populated "df_reporting", which can be used to show on the homescreen.