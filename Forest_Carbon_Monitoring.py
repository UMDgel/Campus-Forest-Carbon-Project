
# coding: utf-8

# # Carbon Monitoring Model Template (Appendix C.2)
Before you begin editing this template, create a copy and edit the copy instead!
This model will output annual carbon stock values in Metric Tons of Carbon (Mg C)
To calculate carbon flux between years, please see the readme file
# In[ ]:


#To set up your workspace, use your specified filepath
#Be sure to change all directory and file names to your own


# In[3]:


#Import the necessary modules after setting up your workspace
#This block of code needs to be run first everytime you open this python file, otherwise you will recieve an error

import arcpy 
from arcpy import env
from arcpy.sa import *
import os
from osgeo import gdal

arcpy.CheckOutExtension('Spatial')
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'Y:\my_file_path\carbon_monitoring_results' # write the filepath where you will save your results


# # Pre-Processing Step

# In[12]:


#This block of code will convert files to 30-meter resolution and NAD_1983_UTM_Zone_18N (26918) projection

raster_list = arcpy.ListRasters("*")

count = 11
for raster in raster_list:
    if raster.startswith('ED'):
        count = count
        filename = r'Y:\my_file_path\carbon_monitoring_results\ED_AGB_20{}.tif'.format(count) # write your filepath including the name of the input file, be sure to include the "20" to specifiy each layer's year
        input_raster = gdal.Open(filename)
        output_raster = r'Y:\my_file_path\carbon_monitoring_results\output_file_20{}.tif'.format(count) # write your filepath and  name of processed output file
        gdal.Warp(output_raster, input_raster, dstSRS='EPSG:26918', xRes= '30', yRes='30')
        count = count + 1


# # Calculating Carbon Stock

# In[1]:


#Step 1: Extract layers to boundary

arcpy.env.workspace = r'Y:\my_file_path\carbon_monitoring_results' # define specific file path 
raster_list = arcpy.ListRasters("*")

count = 1
for raster in raster_list:
    if raster.startswith('output'): # name as first word of of the pre-processed output file
        count = count
        input_raster = r'output_file_20{}.tif'.format(count) # name input as your pre-processed output file
        boundary = r"boundary.shp" # rename as your boundary layer 
        Mask = ExtractByMask(input_raster, boundary)
        Mask.save(r'Y:\my_file_path\carbon_monitoring_results\stock_results\S1_file_20{}.tif'.format(count)) # write your file path to save gain results and the Step 1 output file name, be sure to include the "20" so the output results save the gains for each year  
        count = count + 1


# In[4]:


#Step 2: Raster to point

arcpy.env.workspace = r'Y:\my_file_path\carbon_monitoring_results\stock_results' # define specific file path for gain results
raster_list = arcpy.ListRasters("*")

count = 11
for raster in raster_list:
    if raster.startswith('S1'): # name as first word of the output file from Step 1
        count = count
        source = 'S1_file_20{}.tif'.format(count)
        output = 'S2_file_20{}.shp'.format(count) # name the file output for this step
        arcpy.RasterToPoint_conversion(source, output, "VALUE")
        count = count + 1


# In[13]:


#Step 3: Calculation (conversion from Kg C/m2 to Mg C)

arcpy.env.workspace = r'Y:\my_file_path\carbon_monitoring_results\stock_results' # define specific file path for gain results
expression = '(!grid_code! * 20 * 0.09 * 0.5)'
field = "SUM_MgC"

path =r'Y:\my_file_path\carbon_monitoring_results\stock_results' # define specific file path for gain results
list_of_files = os.listdir(path)

count = 11
for file in list_of_files:
    if file.startswith('S3'):  # name as first word of the output file from Step 3
        count = count
        arcpy.AddField_management(r'S2_file_20{}.shp'.format(count), "MgC", "DOUBLE")
        arcpy.CalculateField_management(r'S2_file_20{}.shp'.format(count), 'MgC', expression)
        stats = arcpy.Statistics_analysis(r'S2_file_20{}.shp'.format(count),                                    r'S3_file_20{}'.format(count),\ # name the file output for this step
                                    [["MgC", "SUM"]])
        value = [row[0] for row in arcpy.da.SearchCursor(r'S3_file_20{}'.format(count), (field))]
        print("20{}: ".format(count) + str(value))
        count = count + 1
        

