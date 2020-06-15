# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 10:38:05 2020

@author: Dawid
"""

import SimpleITK as sitk
import gui

fixed_image = sitk.ReadImage("IR.PNG", sitk.sitkFloat32) 
moving_image = sitk.ReadImage("VIS.JPG", sitk.sitkFloat32)


fixed_image_points = [(19,68), 
                      (206, 50), 
                      (88, 197), 
                      (173,188)]
moving_image_points = [(2792, 1392), 
                       (4462, 1172), 
                       (3412, 2404), 
                       (4080, 2300)]

fixed_image_points_flat = [c for p in fixed_image_points for c in p]        
moving_image_points_flat = [c for p in moving_image_points for c in p]

initial_transformation = sitk.LandmarkBasedTransformInitializer(sitk.VersorRigid3DTransform(), 
                                                                fixed_image_points_flat, 
                                                                moving_image_points_flat)
ct_window_level = (1050,500)
mr_window_level = (1050,500)


gui.RegistrationPointDataAquisition(fixed_image, moving_image, figure_size=(8,4), 
                                    known_transformation=initial_transformation, 
                                    fixed_window_level=ct_window_level, moving_window_level=mr_window_level);