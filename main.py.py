import pandas as pd
import matplotlib.pyplot as plt


####READING DATA
dfCTA = pd.read_csv('cta.csv')
dfEvent = pd.read_csv('event.csv')


####CLEANING DATA

dfEvent = dfEvent.drop(columns=["Requestor","Organization","Park Number","Park/Facility Name","Event Type","Event Description","Reservation Start Date"])

def convertDate(date_in_some_format):
  date_as_string = str(date_in_some_format)  
  year_as_string = date_as_string[-4:]
  return int(year_as_string)



dfCTA['service_date'] = dfCTA['service_date'].apply(convertDate)
dfEvent['Reservation End Date'] = dfEvent['Reservation End Date'].apply(convertDate)

 
dfCTA.rename(columns={"service_date":'Year'}, inplace=True)
dfEvent.rename(columns={"Reservation End Date":'Year'}, inplace=True)



####GROUPING DATA BY SUM,COUNT AND AVG

dfCTASum = dfCTA.groupby("Year",as_index=False)['total_rides'].agg(['sum'])
dfEventSum = dfEvent.groupby('Year',as_index=False)['Year'].agg(['count'])


dfCTAvg = dfCTA.groupby("Year",as_index=False)['total_rides'].agg(['mean'])





####PLOTTING

#plt.plot(dfEventSum["Year"],dfEventSum["count"])
#plt.plot(dfCTASum["Year"], dfCTASum["sum"]) 
plt.plot(dfCTAvg["Year"], dfCTAvg["mean"])
xlocs, xlabs = plt.xticks()
plt.xticks(xlocs, xlabs)
plt.show() 



