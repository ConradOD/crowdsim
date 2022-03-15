#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:26:27 2022

@author: conradodriscoll
"""



"""

USAGE:
    
    Performer only able to be placed at [0,0] very simple update coming to change this
use the setup(a , b , c, d) function to setup and run a  static placement simulation 
a = number of spectators to simulate
b = desired width of venue
c = desired length of venue
d = radius of spectator

This will create all necesary data for the followiong visualise commands:
    
    
visualise (a , b, c)
a = list of instances class created ( in this case 'agents')
b = x dimension (same as b for setup)
c = y dimension (same as c for setup)
Creates and shows a  plot of each spectator and their line of sight, 
The spectator and their line of sight is red if their view is blocked
green if they can see unobstructed


PLS Message me for any guidance or errors / bugs you find or any new features to add
Thank you 


"""
agents =[]
block_region = []

PerformerPosition = [0,0]

from Classes.agentclasses import Static_Spectator_Static_Performer
import matplotlib.pyplot as plt

import random

def setup(number, x_dim, y_dim, radius):
    
    lower_y_lim = 0
    upper_y_lim = y_dim
    
    lower_x_lim = (x_dim/2) *-1
    upper_x_lim = (x_dim/2)
    
    
    for i in range(number):
        agents.append(Static_Spectator_Static_Performer(radius, random.randint(lower_x_lim , upper_x_lim), random.randint(lower_y_lim , upper_y_lim) ))
        agents.sort(key=lambda x: x.r_length, reverse = False)
    for agent in agents:
        
        agent.obstruction_field(PerformerPosition, block_region)
        
        
        

    
plots = []

def visualise(list_of_agents, x_dim, y_dim):
    ax = plt.gca()
    
    UX = x_dim/2
    LX = UX * -1
    LY = 0
    UY = y_dim
    ax.set_xlim((LX,UX))
    ax.set_ylim((LY,UY))
    ax.plot((0),(0), 'o' , color='b')
    for agent in list_of_agents:
        if agent.visibility == 1:
            
            plots.append(plt.Circle((agent.x,agent.y), agent.radius, color='g'))
            plt.plot([0,agent.x], [0,agent.y], 'g--')
            
        else:
            plots.append(plt.Circle((agent.x,agent.y), agent.radius, color='r'))
            plt.plot([0,agent.x], [0,agent.y], 'r--')
            
    for circle in plots:
        ax.add_patch(circle)

        
    plt.show()
    
    
    
    
    
    
    
setup(10, 60, 60, 1)

visualise(agents,60 ,60 )

