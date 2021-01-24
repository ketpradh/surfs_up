# Surfs_up by Ketaki
## Overview of the analysis
This project helps W.Avy to undertand the temperature patterns in Oahu, for the months of June and December. This analysis will help him decide if investing in the surf and icecream shop business would be sustainable and profitable year-round.
## Results:
From the analysis, we can see that the June and December temperature statistics are as follows:
#### June:
![](https://github.com/ketpradh/surfs_up/blob/main/Resources/June%20Temp%20Statistics.PNG)
#### December:
![](https://github.com/ketpradh/surfs_up/blob/main/Resources/June%20Temp%20Statistics.PNG)
- The mean temperatures between June(75) and December(71) do not change drastically.
- The temperature variation(standard deviation) in both the months is similar. 3.25(June) 3.75(Dec).
- There seems to be no more Outliers for the December month.

- The difference in the maximum and low temperatures between June and December do not change drastically, however the minimum temprartures in December(56) is low compared to June(64).
- There is a good amount of sample data collected for both the months.

## Summary: 
It can be seen from the above statistics that temperatures through the year do not vary much and it would probably be profitable to open the surf and icecream shop in Oahu.
#### Query 1- Precipitation data for June and December,Grouped by date determining which day it rained the most.
results_June = session.query(Measurement.prcp, Measurement.date).filter(extract('month', Measurement.date) == '06').\
group_by(Measurement.date).order_by(Measurement.prcp.desc())
![Results for June]()
results_Dec = session.query(Measurement.prcp, Measurement.date).filter(extract('month', Measurement.date) == '12').\
group_by(Measurement.date).order_by(Measurement.prcp.desc())
![Results for December]()
It can be seen that December receives more rain than June.
#### Query 2- Maximum/Minimum tempertaures recorded for June and December by stations.
results_June = session.query(func.max(Measurement.tobs), func.min(Measurement.tobs), Measurement.station, Station.elevation).\
                filter(extract('month', Measurement.date) == '06').\
                filter(Measurement.station == Station.station).group_by(Measurement.station).order_by(Station.elevation.desc())
![June results]()
results_Dec = session.query(func.max(Measurement.tobs), func.min(Measurement.tobs), Measurement.station, Station.elevation).\
                filter(extract('month', Measurement.date) == '12').\
                filter(Measurement.station == Station.station).group_by(Measurement.station).order_by(Station.elevation.desc())
![Dec results]()            
