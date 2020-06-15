# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:17:07 2020

@author: Dawid
"""


class ImageStorage:    
    
    def __init__(self, path):
        self.data_path = path
        self.IR_path = self.data_path + '/IR'
        self.VIS_path = self.data_path + '/VIS'
        
        self.IR_ref_image_path = self.IR_path + '/IMGT0449.png'
        self.VIS_ref_image_path = self.VIS_path + '/_MG_1464.JPG'