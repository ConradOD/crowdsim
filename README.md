# Crowd Vision Simulator
This project is a python based program to simulate a venue space (like a night club or concert) with agent based crowd members and performers. The main scope of the project is the visibility of the crowd members in relation to the performer or target. More specifically, can a crowd member see the target, and given different movement motivations (including the desire to see) how do their individual movements combine with many other  agent space with the same movement mechanisms and what if any trends or patterns are created.


## Agent Based model of a crowd in a venue space.

Crowd members are modelled as instances of the spectator agent class with different properties combined with visibility and movement algorithms to determine their state transition between time steps. 

The program is developed from a basic concept of obstructed regions,  simply put if an agent                                       e. 

This is in contrast to visibility algorithms which check whether **all** other agents are at least a minimal distance away from the desired visibility line of an agent in question such that they dont obstruct the view. This method is computationally intense ( since you must calculate the distance of every agents location for each agents visibility and adding another agent = n-1 more calculations) and relies on perfect knowledge of the location of the desired target. 

Due to the assumed linear directional properties of light waves, we can reverse our visibility algorithm to show the regions which cannot 
be seen by the agent in question due to other agents, this allows more accurate assumptions for movement alogrithms based on the knowledge each agent would have in a real life scenario. 

This can be shown here: 

