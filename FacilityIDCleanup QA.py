# CountFeatures is a function for taking the (Feature Class, Feature Layer, WHERE_CLAUSE )   
import arcpy
# Setting the workspace
arcpy.env.workspace = 'Z:\FacilityIDCleanup.gdb'
# FC = Feature Class, LYR = Feature Layer
def CountFeatures(FC,LYR,PREFIX):
    arcpy.MakeFeatureLayer_management(FC,LYR,"FACILITYID LIKE '{}%'".format(PREFIX))
    arcpy.MakeFeatureLayer_management(FC,LYR+"_","FACILITYID NOT LIKE '{}%'".format(PREFIX))
    arcpy.MakeFeatureLayer_management(FC,LYR+"_1","FACILITYID IS NULL".format(PREFIX))
    count = arcpy.GetCount_management(LYR)
    count1 = arcpy.GetCount_management(LYR+"_")
    count2 = arcpy.GetCount_management(LYR+"_1")
    print("The correct count for {0} is {1}".format(FC,count))
    print("{0} of features in {1} are incorrect and {2} that is NULL".format(count1,FC,count2))
    return("The correct count for {0} is {1}".format(FC,count)) + '\r\n' + ("{0} of features in {1} are incorrect and {2} that is NULL".format(count1,FC,count2))
    



# Writing the output data as a txt file
# 'r\n\' is for making a new line in Windows 




#!/usr/bin/python

# Open a file
fo = open("CountFeatureClass.txt", "wb")
#Do your business
fo.write(CountFeatures("wLateralLine","ITLS","WLAT"));

# Close opend file
fo.close()


          
    


