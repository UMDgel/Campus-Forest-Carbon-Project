# Campus-Forest-Carbon-Project: 
These models accompany Appendix  B.2 and Appendix C.2 within the University of Maryland's Peer-Review Offset Protocol for Maryland Reforestation/Afforestation Projects. 

Prior to downloading the code users must install the most recent, updated version of Jupyter Notebook or other program that can run Python scripts. Users must also download ArcGIS 10.8.1 or the most current release of ArcGIS as these models use the ArcPy library. If you do not have an ArcGIS license, we reccomended replicating our methodology with other open-acess GIS software such as QGIS. 

All data necessary to run the models and more details on the Ecosystem Demography data products derived from NASA Carbon Monitoring System science and further literatureare provided here:
- [Simulated forest aboveground biomass data for the first 300 years of forest succession over the Regional Greenhouse Gas Domain](10.5281/zenodo.6506453)
- [Forest aboveground biomass from 1984-2016 for the state of MD](10.5281/zenodo.6506502)

If using a Jupyter environment, download the code as a .ipynb file (recommended). If using another coding environment, download and open as a .py file
Because these models are only templates, we reccommended making a copy and editing variable and file path names on the duplicate model. Be sure to also first set up your work space (where you will pull data from and save files to) before running each model. For further detailed instructions, please see comments in the models.

These models follow the same methodology, with the primary difference being the number of years used. The Carbon Baseline model only utilizes two years (project start and end year), whereas the Carbon Monitoring model uses the entire forest project's time period, which can be any number of years greater than two (i.e., the specific monitoring years). Please also identify the geographic domains of interest within Maryland to use as your boundary shapefile for both models.  

## Carbon Baseline Template (Appendix B.2) 
This model estimates a forest project's current baseline stocks in order to assess changes to carbon stocks during the project time period. This model will output two values: the total amount of carbon in Mg C for the (1) project start year and the (2) project end year

To calculate the actual carbon baseline, subtract the total amount of carbon for the project end year from the start year. This will output the total projected amount of carbon in Mg C that will be accumulated over the project time period (i.e., carbon baseline). 

## Carbon Monitoring Model Template (Appendix C.2)
This second model estimates a forest project's carbon dynamics over a specified time period for inclusion within a forest project's carbon inventory. This model will output the carbon stock for every year specified in Mg C. 

To calculate the carbon flux values, subtract carbon stock values from the newer to older year (e.g., 2020 carbon stock - 2019 carbon stock). This value is the total projected amount of carbon accumulated since that last year. Complete carbon monitoring can be developed by calculating the carbon flux and assessing changes to the flux values for an entire time period. 

For any questions, suggestions, or concerns please contact fpanday@umd.edu and lma6@umd.edu. 
