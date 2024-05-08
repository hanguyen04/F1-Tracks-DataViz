# F1 Tracks - Data Visualized 

# Project Objective: 
After seeing the recent fatalities at Circuit de Spa-Francorchamps (Belgium), I want to look at the Data from different Formula 1 tracks to see which tracks are more dangerous or cause harm to the drivers.

# Project Outline: 
* Gather data from the Internet about the crashes for each track and compile it
* Seeing which track has the most crashes
* Cross-referencing it with other possible data points through more datasets & graphs \
[Weather at each location - i.e: rain can affect DNF rates] \
[Car performance each season - i.e: McLaren 2022 had a lot of mechanical failures leading to DNF which isn't related to the track]

# Progress
I currently have data for DNF for every race from the past 20 years 

## Web Crawling 
API used for Data: https://ergast.com/mrd/ \
This is an API used by many fans of F1 for their personal project as they can use a web crawler to gather data from it \
I have built my own web crawler to get data specifically for the DNFs over the past 20 years and write it as CSV files for plotting 

## Initial Plotting 
I used Matplotlib & Seaborn for plotting to visualize the data from the last 10 years for relevancy and better viewing

![Figure_1](https://github.com/hanguyen04/f1dataviz/assets/63039106/d5d43b8e-18be-4196-bc1e-d9c0125c049f)
[Figure 1. DNF Values by Year (2011 - 2021)] 

Based on this, the Monaco GP stood out the most. This is expected as there is a higher rate of crashes at this rate every year due to the tight turns which the track is known for 

## Next Steps 
* Figuring out how to better visualize the data which are all plotted on to the graph right now
* More accurately represent the crash race as the circuits which aren't raced on get the value of zero or the race which came before it (inaccurate)
* Build more scrapers to get data for the aforementioned information such as weather or mechanical failure
