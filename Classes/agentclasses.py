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
        self.pos = [self.x, self.y]
        
        self.visibility = 1
        self.r_length = math.sqrt((self.x**2)+(self.y**2))
        if self.x < 0 :
            self.theta = math.pi - math.atan(self.y/abs(self.x))
        elif self.x == 0:
            self.theta = math.pi / 2
        else:
            
            self.theta = math.atan(self.y/self.x)
        
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
            
            if self.r_length > (blocked_region[0]+ 0.25)  and blocked_region[1][0] <= self.theta <= blocked_region[1][1] :
                        self.visibility=0
                        break
            
            else:
                        continue
            
    
        
        
            
                    
            
    
    
        
    
        


        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
    
