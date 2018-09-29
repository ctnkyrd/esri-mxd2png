import arcpy
from arcpy import env  
  
env.overwriteOutput = True 
#open mxd file
class mxd2jpg:
    def __init__(self, mxdPath, imagePath,pk="OBJECTID", width=363, height=300):
        self.mxdPath = mxdPath
        self.imagePath = imagePath
        self.width = width
        self.height = height
        self.pk = pk
    #select records from desired layer with given SQL criteria in given table with ArcMap Standards
    def selectLayer(self, layerName, whereClause=""):
        try:
            mxd = arcpy.mapping.MapDocument(self.mxdPath)
            df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
            selectedLayer = arcpy.mapping.ListLayers(mxd, layerName, df)[0]
            print "MXD File: "+ self.mxdPath
            print "Image Path: "+ self.imagePath
            print "Image Height/Width: "+ str(self.width) + "/" + str(self.height)
            print layerName+" Started Total of "+str(arcpy.GetCount_management(selectedLayer))+" rows"
            cursor = arcpy.SearchCursor(selectedLayer,whereClause)
            for row in cursor:
                selected = arcpy.SelectLayerByAttribute_management(selectedLayer,"NEW_SELECTION",self.pk+" = "+str(row.getValue(self.pk)))
                df.zoomToSelectedFeatures()
                df.scale *= 1.5
                arcpy.RefreshActiveView()
                arcpy.mapping.ExportToJPEG(mxd,self.imagePath+'\\'+layerName+"_"+str(row.getValue(self.pk))+".jpg",df,df_export_width=self.width,df_export_height=self.height)
            print layerName + " Completed Successfully"
        except BaseException as Be:
            print Be.message
        