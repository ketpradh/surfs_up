# Surfs_up by Ketaki
## Overview of the analysis
### This project helps W.Avy to undertand the temperature patterns in Oahu, for the months of June and Decemnber. This analysis will help him decide if investing in the surf and icecream shop business is profitable year round.
## Results:
### From the analysis, we can see that the June and December temperature statistics are as follows:
#### June:
#### December:

## Summary: 
### It can be seen from the above statistics that temperatures through the year do not vary much. 
#### Query 1- Precipitation data for June and December Grouped by date determining which day it rained the most.
results_June = session.query(Measurement.prcp, Measurement.date).filter(extract('month', Measurement.date) == '06').\
group_by(Measurement.date).order_by(Measurement.date.desc())
![Results for June]()
results_Dec = session.query(Measurement.prcp, Measurement.date).filter(extract('month', Measurement.date) == '12').\
group_by(Measurement.date).order_by(Measurement.date.desc())
![Results for December]()
#### Query 2- Precipitation data for June and December - Which stations had the most precipitation in June and December.
results_June = session.query(Measurement.prcp, Measurement.station).filter(extract('month', Measurement.date) == '06').\
                group_by(Measurement.station).order_by(Measurement.prcp.desc())
results_Dec = session.query(Measurement.prcp, Measurement.station).filter(extract('month', Measurement.date) == '12').\
                group_by(Measurement.station).order_by(Measurement.prcp.desc())                
