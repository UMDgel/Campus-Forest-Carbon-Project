# Campus-Forest-Carbon-Project: 
These models accompany Appendix  B.2 and Appendix C.2 within the University of Maryland's Peer-Review Offset Protocol for Maryland Reforestation/Afforestation Projects. These models also use the ArcPy library, which requires an ArcGIS license. For use with other GIS software, please replicate the template's methodology. 

Because these models are only templates, we reccommended making a copy and editing variable and file path names on the duplicate model. This will prevent accidental deletion of essential code. 

We also reccomended running this script in Jupyter notebook or other suitable Python environments. Be sure to first set up your work space (where you will pull data from and save files to) before running each model. For further detailed instructions, please see comments in the models.

All data necessary to run the models are provided here:
- [Simulated forest aboveground biomass data for the first 300 years of forest succession over the Regional Greenhouse Gas Domain](10.5281/zenodo.6506453)
- [Forest aboveground biomass from 1984-2016 for the state of MD](10.5281/zenodo.6506502)

More details on the Ecosystem Demography data products derived from NASA Carbon Monitoring System science and further literature can also be found in the provided links. 

These models follow the same methodology, with the primary difference being the number of years used. The Carbon Baseline model only utilizes two years (project start and end year), whereas the Carbon Monitoring model uses the entire forest project's time period, which can be any number of years greater than two. 

## Carbon Baseline Template (Appendix B.2) 
This model estimates a forest project's current baseline stocks in order to assess changes to carbon stocks during the project time period. This model will output two values: the total amount of carbon in Mg C for the (1) project start year and the (2) project end year

To calculate the actual carbon baseline, subtract the total amount of carbon for the project end year from the start year. This will output the total projected amount of carbon in Mg C that will be accumulated over the project time period (i.e., carbon baseline). 

## Carbon Monitoring Model Template (Appendix C.2)
This second model estimates a forest project's carbon dynamics over a specified time period for inclusion within a forest project's carbon inventory. This model will output the carbon stock for every year specified in Mg C. 

To calculate the carbon flux values, subtract carbon stock values from the newer to older year (e.g., 2020 carbon stock - 2019 carbon stock). This value is the total projected amount of carbon accumulated since that last year. Complete carbon monitoring can be developed by calculating the carbon flux and assessing changes to the flux values for an entire time period. 

For any questions, suggestions, or concerns please contact fpanday@umd.edu and lma6@umd.edu. 
