# Belief_Revision_Agent

### Description
A Python project for the implementation of a belief revision agent. A GUI with three operation(revise, expand, and contract) is used to manage the belief base. The user should introduce the proposition and the order of the beliefs, and choose the desired operation. After pressing the desired button, the new belief base will be updated and displayed on the output box. The library Sympy has been used to ease the handle of the proposition formulas.

### Project distribution
* `Belief_GUI.py`: Contains the classes and methods used for handling the graphical display of the project. 
* `BeliefBase.pyy`: Contains the class for the belief base and the class for beliefs. Handles most of the logic and main code for defining the agent.
* `entailment.py`: Implementation of the entailment check between the belief base and the new proposition.

### Installation and run
Before running the project, **sympy** package should be installed.(in conda terminal run: ***pip install sympy***).
To run the project run the **Belief_GUI.py** script: ***python Belief_GUI.py***




