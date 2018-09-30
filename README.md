# esri-mxd2png
with arcpy opens desired .mxd and zoom to selected records based in criteria and  iterate through records get &amp; save screenshot.

required parameters are,
* Location of the given mxd (must be a valid mxd with layers on)
* location of the exported images folder
* lastly the layername

## latest version 1.0.1

## installation
-```pip install mxd2jpg``` <br>
-```python -m pip install mxd2jpg ```

## dependencies
Please ensure that you need to have ArcGIS 10.x installed on your computer in order to use this module.

## usage

```
import mxd2jpg

mxdj2jpgObject = mxd2jpg.mxd2jpg('A:\buildings.mxd', 'A:\exported-images')
mxdj2jpgObject.selectLayer("BUILDING")

print "DONE!"
```
## screenshots
![alt text](https://ibb.co/cscuMz)
