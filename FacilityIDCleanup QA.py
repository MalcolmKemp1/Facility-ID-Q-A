# CountFeatures is a function for taking the (Feature Class, Feature Layer, WHERE_CLAUSE )

import arcpy
# Setting the workspace
arcpy.env.workspace = 'Z:\FacilityIDCleanup.gdb'
# FC = Feature Class, LYR = Feature Layer
def CountFeatures(FC,LYR,PREFIX):
    arcpy.MakeFeatureLayer_management(FC,LYR,"FACILITYID  LIKE '{}%'".format(PREFIX))
    arcpy.MakeFeatureLayer_management(FC,LYR+"_","FACILITYID NOT  LIKE '{}%'".format(PREFIX))
    count = arcpy.GetCount_management(LYR)
    count1 = arcpy.GetCount_management(LYR+"_")
    print("The correct count for {0} is {1}".format(FC,count))
    print("{0} of features in {1} are incorrect".format(count1,FC))
     

CountFeatures("wLateralLine","HYDRANNNNNNNNNNTTTTT","WLAT")
CountFeatures("wControlValve","JOE","WCV")



          
    


