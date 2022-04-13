# Crowd Vision Simulator
This project is a python based program to simulate a venue space (like a night club or concert) with agent based crowd members and performers. The main scope of the project is the visibility of the crowd members in relation to the performer or target. More specifically, can a crowd member see the target, and given different movement motivations (including the desire to see) how do their individual movements combine with many other agents in the space with the same movement mechanisms and what if any trends or patterns are created?


## Agent Based model of a crowd in a venue space.

An initial discrete static model version is created for proof of concept of the visibility algorithms, this is then optimised and refined to increase efficiency and is then brought into a dynamic space by using discrete time steps. 
Collisions and overlap is not incorporated into the static model since its purpose is to display the functionality of the visibility algorithms. 
However, collisions are also not incorporated in the dynamic time step model. This is for the following reasons:

Collision detection is computationally expensive in comparison to its usefulness. We would rather observe the behaviour of a larger number of agents without excessive processing time (and without collision mechanics) than have a more tight restriction on the number of agents and take longer processing simulations but have nice collision features. 

Collision detection would suggest collision mechanics and movement mechanics based on collisions, although it would be interesting and a nice feature, it isnt necesary as for over 50% of cases of overlap or collision, the visibility and movement algorithms already account for overlapping agents and motivate a movement away from each other by means of blocked vision. We want a sense of consistency in the movement algorithms to promote repeatable analysis of the emerging patterns.


Justifying and specifying the coefficients of restitution and other collisional properties being incorporated into the movement algorithms may shadow the movement patterns we want to observe when based mostly on the desire to see. 

"Bumping", "overlapping" and the general multiple occupation of areas of space are very common to the application of night clubs and venue spaces, the collision mechanics arising from these do not have a significant effect on motion as the collisions are almost always at very low speeds and are very inelastic collisions ( such as shoulder rubbing and brushing past people) 

###The program


Crowd members are modelled as instances of a "spectator" class with different properties which are input into visibility and movement algorithms to determine their state transition between time steps. The options are generally to either remain in the same position or perform a unit length movement in a direction determined by the algorithm and program version used.


The program is developed from a basic concept of obstructed regions, simply put if an agent has the positional properties which indicate they lie within a region which has been predetermined to have an obstrcuted view, then the algorithm decides they cannot see.

Please see the (badly drawn sorry) Diagram showing the basics of the aglorithm (1)  and the reverse application (2) of the algorithm which can have uses to determine an agents visible information field (i.e the agent can't know what lies behind the obstruction but the first application (1) assumes perfect knowledge that their view of the target is blocked by knowing that the performer is at a given point behind the obstruction, if that makes sense?, application (2) just suggests they can't see what, if anything, in that certain field) 



![readmediagram1-2](https://user-images.githubusercontent.com/101503093/163177829-74ea19cc-0b99-479d-ad48-2ec4e8f57148.jpg)




This is in contrast to visibility algorithms which check whether **all** other agents are at least a minimal distance (1 Radius) away from the visibility line of the agent in question such that they dont obstruct the view. This method is computationally intense ( since you must calculate the distance of every agents' location for each agent's visibility and adding another agent = n-1 more calculations) and relies on perfect knowledge of the location of the desired target. 

My algorithm keeps an array of obstructed view regions which are each determined by an individual agent, therefore if an agent does not move, the region that they block does not need to be updated ( in the static performer target version). This saves expensive, unnecessary computations when the properties of agents have not changed. This is particularly important whhen 


Due to the assumed linear directional properties of light waves, we can reverse our visibility algorithm to show the regions which cannot 
be seen by the agent in question due to other agents, this allows more accurate assumptions for movement alogrithms based on the knowledge each agent would have in a real life scenario. 

This can be shown here: 

