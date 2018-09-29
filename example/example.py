import sys
sys.path.insert(0, '../mxd2jpg')
import mxd2jpg


a = mxd2jpg.mxd2jpg(r'C:\Users\PC1\Desktop\theCode.mxd', 'A:\Balikesir_KAIP\esri-mxd2png\images')
a.selectLayer("PARSEL_ESKI")