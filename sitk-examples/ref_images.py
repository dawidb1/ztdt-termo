# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:47:11 2020

@author: Dawid
"""


import SimpleITK as sitk

def showImage(img, title="Untitled image"):
    image_viewer = sitk.ImageViewer()
    image_viewer.SetApplication('C:/Program Files/ITK-SNAP 3.8/bin/ITK-SNAP.exe')
    image_viewer.SetTitle(title)
    image_viewer.Execute(img)



# image_viewer = sitk.ImageViewer()
# image_viewer.SetApplication('C:/Program Files/ITK-SNAP 3.8/bin/ITK-SNAP.exe')

# image_viewer.SetTitle("VIS")
# image_viewer.Execute(VIS_ref_image)

# reader = sitk.ImageFileReader()
# reader.SetFileName(IR_ref_image_path)
# IR_ref_image = reader.Execute();

# reader.SetFileName(VIS_ref_image_path)
# VIS_ref_image = reader.Execute();

# show image
