# esri-mxd2jpg
choose your mxd file with layers and zoom to selected records based in criteria and  iterate through records get &amp; save screenshot.

required parameters are,
###mxd2jpg class
* mxdPath: path to the valid mxd file
* images path: folder at which the images installed
* pk: primary key (objectid) of the layer's table (deafult: "OBJECTID")
* widht: px witdh of the images (default: 363)
* height: px height of the images (default: 300)
###mxd2jpg.selectLayer def
* layerName: name of the layer which is valid at the dataframe
* whereClause: arcgis select layerByAttribute like where clauses (default: "")
  * example whereClause: "AREA > 300"

## latest version 1.0.1

## installation
-```pip install mxd2jpg``` <br>
-```python -m pip install mxd2jpg ```

## dependencies
Please ensure that you need to have ArcGIS 10.x installed on your computer in order to use this module.

## usage

```
import mxd2jpg

mxdj2jpgObject = mxd2jpg.mxd2jpg(r'A:\buildings.mxd', 'A:\exported-images', pk="OBJECTID")
mxdj2jpgObject.selectLayer("BUILDING")

print "DONE!"
```
## screenshots
<a><img src="https://image.ibb.co/mzSGZK/PARSEL_ESKI_71.jpg" alt="PARSEL_ESKI_71" border="0"></a><br>

<a><img src="https://preview.ibb.co/cvb4Mz/mxd2jpg_imagesfolder.jpg" alt="mxd2jpg_imagesfolder" border="0"></a>
