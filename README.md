# Campus-Forest-Carbon-Project

# -*- coding: utf-8 -*-
# Carbon Monitoring Model Template

"""
Before you begin editing this template, create a copy and edit the copy instead!
This model will output annual carbon stock values and carbon loss values in Metric Tons of Carbon (Mg C)
"""

#To set up your workspace, use your specified filepath
#Be sure to change all directory and file names to your own

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

"""# Pre-Processing Step"""

#This block of code will convert files to 30-meter resolution and NAD_1983_UTM_Zone_18N (26918) projection

raster_list = arcpy.ListRasters("*")

count = 11
for raster in raster_list:
    if raster.startswith('file'):# name as first word of the raster file you want to pre-process (the input file name)
        count = count
        filename = r'Y:\my_file_path\carbon_monitoring_results\file_name_20{}.tif'.format(count) # write your filepath including the name of the input file, be sure to include the "20" to specifiy each layer's year
        input_raster = gdal.Open(filename)
        output_raster = r'Y:\my_file_path\carbon_monitoring_results\output_file_20{}.tif'.format(count) # write your filepath and  name of processed output file
        gdal.Warp(output_raster, input_raster, dstSRS='EPSG:26918', xRes= '30', yRes='30')
        count = count + 1

"""# Calculating Carbon Gains"""

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
        Mask.save(r'Y:\my_file_path\carbon_monitoring_results\output_file\gain_results\S1_file_20{}.tif'.format(count)) # write your file path to save gain results and the Step 1 output file name, be sure to include the "20" so the output results save the gains for each year  
        count = count + 1

#Step 2: Multiply raster files by the tree canopy cover percentage

arcpy.env.workspace = r'Y:\my_file_path\carbon_monitoring_results\gain_results' # define specific file path for gain results
raster_list = arcpy.ListRasters("*")

count = 11
for raster in raster_list:
    if raster.startswith('S1'): # name as first word of the output file from Step 1 
        count = count
        raster1 = r'S1_file_20{}.tif'.format(count) 
        raster2 = r'Y:\file_path\Maryland_PercentTreeCover_30m.tif' # add the file path of where tree canopy cover % is saved
        outTimes = Times(raster1, raster2)
        outTimes.save(r'S2_file_20{}.tif'.format(count)) # name the file output for this step
        count = count + 1

#Step 3: Raster to point

arcpy.env.workspace = r'Y:\my_file_path\carbon_monitoring_results\gain_results' # define specific file path for gain results
raster_list = arcpy.ListRasters("*")

count = 11
for raster in raster_list:
    if raster.startswith('S2'): # name as first word of the output file from Step 2
        count = count
        source = 'S2_file_20{}.tif'.format(count)
        output = 'S3_file_20{}.shp'.format(count) # name the file output for this step
        arcpy.RasterToPoint_conversion(source, output, "VALUE")
        count = count + 1

#Step 4: Calculation

arcpy.env.workspace = r'Y:\my_file_path\carbon_monitoring_results\gain_results' # define specific file path for gain results
expression = '(!grid_code! * 20 * 0.09 * 0.5)'
field = "SUM_MgC"

path =r'Y:\my_file_path\carbon_monitoring_results\gain_results' # define specific file path for gain results
list_of_files = os.listdir(path)

count = 11
for file in list_of_files:
    if file.startswith('S3'):  # name as first word of the output file from Step 3
        count = count
        arcpy.AddField_management(r'S3_file_20{}.shp'.format(count), "MgC", "DOUBLE")
        arcpy.CalculateField_management(r'S3_file_20{}.shp'.format(count), 'MgC', expression)
        stats = arcpy.Statistics_analysis(r'S3_file_20{}.shp'.format(count),\
                                    r'S4_file_20{}'.format(count),\ # name the file output for this step
                                    [["MgC", "SUM"]])
        value = [row[0] for row in arcpy.da.SearchCursor(r'S4_file_20{}'.format(count), (field))]
        print("20{}: ".format(count) + str(value))
        count = count + 1

"""# Calculating Carbon Loss"""

#Step 1: Extract by Mask 

arcpy.env.workspace = r'Y:\my_file_path\carbon_monitoring_results' # define specific file path for results

raster_list = arcpy.ListRasters("*")

count = 11
for raster in raster_list:
    if raster.startswith('output'): # name as first word of of the pre-processed output file
        try:
            count = count
            Mask = ExtractByMask(raster,\
                       r"Y:\my_file_path\carbon_monitoring_results\loss_results\loss_file_20{}.shp".format(count)) # write your file path to save loss results and name of output file, including the "20" so loss can be calculated for each specific year
            Mask.save(r'Y:\my_file_path\carbon_monitoring_results\loss_results\S1_file_20{}.tif'.format(count)) # name the file output for this step
            count = count + 1
        except:
            if count < 21:
                print("No loss in 20{}".format(count))
                count = count + 1
                continue
            else:
                break

#Step 2: Raster to point

arcpy.env.workspace = r'Y:\my_file_path\carbon_monitoring_results\loss_results' # define file path for loss results
raster_list = arcpy.ListRasters("*")

count = 11
for raster in raster_list:
    if raster.startswith('S1'): # name as first word of output file from step 1 
        try:
            count = count
            source = 'S1_file_20{}.tif'.format(count)
            output = 'S2_file_20{}.shp'.format(count) # name the file output for this step
            arcpy.RasterToPoint_conversion(source, output, "VALUE")
            count = count + 1
        except:
            if count < 21:
                print("20{}.shp does not exist".format(count))
                count = count + 1
                continue
            else:
                break

#Step 3: Calculation

arcpy.env.workspace = r'Y:\my_file_path\carbon_monitoring_results\loss_results' # define file path for loss results
expression = '(!grid_code! * 20 * 0.09 * 0.5)'
field = "SUM_MgC"

path = r'Y:\my_file_path\carbon_monitoring_results\loss_results' # define file path for loss results
list_of_files = os.listdir(path)

count = 11
for file in list_of_files:
    if file.startswith('S2'): # name as first word of output file from step 2
        try:
            count = count
            arcpy.AddField_management(r'S2_file_20{}.shp'.format(count), "MgC", "DOUBLE")
            arcpy.CalculateField_management(r'S2_file_20{}.shp'.format(count), 'MgC', expression)
            stats = arcpy.Statistics_analysis(r'S2_file_20{}.shp'.format(count), r'S3_file_20{}'.format(count), [["MgC", "SUM"]])  # name the file output for this step
            value = [row[0] for row in arcpy.da.SearchCursor(r'S3_file_20{}'.format(count), (field))]
            print("20{}: ".format(count) + str(value))
            count = count + 1
        except:
            if count < 21:
                print("20{}: 0".format(count))
                count = count + 1
                continue
            else:
                break
