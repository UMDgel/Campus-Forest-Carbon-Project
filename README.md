# Campus-Forest-Carbon-Project: 
These models accompany Appendix  B.2 and Appendix C.2 within the University of Maryland's Peer-Review Offset Protocol for Maryland Reforestation/Afforestation Projects. 

Prior to downloading the code users must install the most recent, updated version of Jupyter Notebook or other Python friendly environment.

All data necessary to run the models and more details on the Ecosystem Demography data products derived from NASA Carbon Monitoring System science and further literature are provided here:
- [Simulated forest aboveground biomass data for the first 300 years of forest succession over the Regional Greenhouse Gas Domain](https://doi.org/10.5281/zenodo.6506453)
- [Forest aboveground biomass from 1984-2016 for the state of MD](https://doi.org/10.5281/zenodo.6506502) 

If using a Jupyter environment, download the code as a .ipynb file (recommended). If using another coding environment, download and open as a .py file.
Because these models are only templates, we reccommended making a copy and editing variable and file path names on the duplicate model. Be sure to also first set up your work space (where you will pull data from and save files to) before running each model. For further detailed instructions, please see comments in the models.

These models follow the same methodology, with the primary difference being the number of years used. The Carbon Baseline model only utilizes two years (project start and end year), whereas the Carbon Monitoring model uses the entire forest project's time period, which can be any number of years greater than two (i.e., the specific monitoring years). Please also identify the geographic domains of interest within the RGGI region to use as your boundary shapefile for both models. It should be noted that as data is updated yearly, the link will change as well. 

These models are developed in part by the Campus Forest Carbon Project. CFCP is a Global Ecology Lab based project utilizing satellite data products to calculate above ground biomass with the goal of contributing to UMD’s net zero carbon emissions goal. More information about the Campus Forest Carbon Project can be found here. 

## Carbon Baseline Template (Appendix B.2) 
This model estimates a forest project's current baseline stocks in order to assess changes to carbon stocks during the project time period. This model will output two values: the total amount of carbon in Mg C for the (1) project start year and the (2) project end year

To calculate the actual carbon baseline, subtract the total amount of carbon for the project end year from the start year. This will output the total projected amount of carbon in Mg C that will be accumulated over the project time period (i.e., carbon baseline). 

## Carbon Monitoring Model Template (Appendix C.2)
This second model estimates a forest project's carbon dynamics over a specified time period for inclusion within a forest project's carbon inventory. This model will output the carbon stock for every year specified in Mg C. 

To calculate the carbon flux values, subtract carbon stock values from the newer to older year (e.g., 2020 carbon stock - 2019 carbon stock). This value is the total projected amount of carbon accumulated since that last year. Complete carbon monitoring can be developed by calculating the carbon flux and assessing changes to the flux values for an entire time period. 

For any questions, suggestions, or concerns please contact CFCP@umd.edu

