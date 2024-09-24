from PyQt5 import QtGui
for i in QtGui.QImageReader.supportedImageFormats():
    print(str(i, "ascii").upper(), end=" ")
# BMP CUR GIF ICNS ICO JPEG JPG PBM PGM PNG PPM SVG SVGZ TGA TIF TIFF WBMP WEBP XBM XPM
