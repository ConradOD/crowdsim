#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:30:39 2022

@author: conradodriscoll
Agent Classes for Initial Static Model


"""
import numpy as np
import math
import random

pi = math.pi 


        

class Static_Spectator_Static_Performer():
    
    def __init__(self, radius, x_pos, y_pos):
        self.radius = radius
        self.x = x_pos
        self.y = y_pos
        self.pos = [x_pos, y_pos]
        
        self.visibility = 1
        self.r_length = math.sqrt((x_pos**2)+(y_pos**2))
        if x_pos < 0 :
            self.theta = math.pi - math.atan(y_pos/abs(x_pos))
        elif x_pos == 0:
            self.theta = math.pi / 2
        else:
            
            self.theta = math.atan(y_pos/x_pos)
        
    def obstruction_field(self, performer_pos, blocked_region_dataset):
        distance = math.dist(self.pos, performer_pos)
        field_phi = math.atan(self.radius/distance)
        lower_lim_blocked = self.theta - field_phi
        upper_lim_blocked = self.theta + field_phi
        phi_blocked_array = [lower_lim_blocked, upper_lim_blocked]
        
        blocked_region_dataset.append([distance, phi_blocked_array])
        self.obstructed_view(blocked_region_dataset)
        
        return blocked_region_dataset
    
    def obstructed_view(self, blocked_region_dataset):
        for blocked_region in blocked_region_dataset:
            region_start_distance = blocked_region[0]
            region_angle = blocked_region[1]
            
            if self.r_length > (region_start_distance + 0.5)  and region_angle[0] <= self.theta <= region_angle[1] :
                    self.visibility=0
            
            else: 
                
                continue
            
    
        
        
            
                    
            
    
    
        
    
        


        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
    