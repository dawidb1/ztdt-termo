# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:49:17 2020

@author: Dawid
"""

# Always write output to a separate directory, we don't want to pollute the source directory. 
import os
import SimpleITK as sitk

from ImageStorage import ImageStorage
from utilities import read_image
from ref_images import showImage

def command_iteration(method) :
    print("{0:3} = {1:10.5f} : {2}".format(method.GetOptimizerIteration(),
                                   method.GetMetricValue(),
                                   method.GetOptimizerPosition()))

OUTPUT_DIR = 'Output'

data_path  = 'C:/Users/Dawid/OneDrive/Studia/MGR/SEMESTR 3/ZTDT/shared/HTO_DANE/S1'
image_storage = ImageStorage(data_path)


fixed = sitk.ReadImage(image_storage.IR_ref_image_path, sitk.sitkFloat32) 
moving = sitk.ReadImage(image_storage.VIS_ref_image_path, sitk.sitkFloat32)

R = sitk.ImageRegistrationMethod()
R.SetInitialTransform(sitk.TranslationTransform(fixed.GetDimension()))
R.SetMetricAsMeanSquares()
R.SetOptimizerAsRegularStepGradientDescent(4.0, .01, 500 )
R.SetInterpolator(sitk.sitkLinear)

# R.AddCommand( sitk.sitkIterationEvent, lambda: command_iteration(R) )

outTx = R.Execute(fixed, moving)

# print("-------")
# print(outTx)
# print("Optimizer stop condition: {0}".format(R.GetOptimizerStopConditionDescription()))
# print(" Iteration: {0}".format(R.GetOptimizerIteration()))
# print(" Metric value: {0}".format(R.GetMetricValue()))

resampler = sitk.ResampleImageFilter()
resampler.SetReferenceImage(fixed);
resampler.SetInterpolator(sitk.sitkLinear)
resampler.SetDefaultPixelValue(100)
resampler.SetTransform(outTx)

out = resampler.Execute(moving)
simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
cimg = sitk.Compose(simg1, simg2, simg1//2.+simg2//2.)
# showImage( simg2, "ImageRegistration1 Composition" )

from utilities import save_image
save_image(simg2, 'sigm2.png')
