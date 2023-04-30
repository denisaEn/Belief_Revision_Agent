
import re
from sympy.logic.boolalg import to_cnf
from entailment import *


def _validate_order(order):
    """
    Checks if the order of the belief is within range (0<=order<=1)
    0 - it is never true
    1 - it is a tautology
    """
    if not ((0 <= order) and (order <= 1)):
        raise Exception ('The order must be between 0 and 1')

class BeliefBase:
    def __init__(self):
        # we can sort the belief set here
        self.beliefs = []
        self.expanded = True
    
    def parsing_bicond(self, belief):
        """ Formats biconditionality to match requirements for sympy logic to_cnf """
        bicond_patt = "<>"
        belief = re.sub(bicond_patt, '>>', belief)
        belief = re.sub(r"[()]", "", belief)
        return_belief = '('+belief+')&('+belief[-1]+'>>'+belief[0]+')'
        
        return return_belief

    def add(self, formula, order):
        """
        Add a belief to the base (sorted by order) without checking the validity.
        """
        if "<>" in formula:
            formula = self.parsing_bicond(formula)
        formula = to_cnf(formula)
        #Remove dupplicates
        self.delete(formula)

        if order > 0:
            new_belief = Belief(formula, order)
            # add at the end if there is no belief in the list or the order is maximum
            if len(self.beliefs) == 0 or self.beliefs[-1] >= new_belief:
                self.beliefs.append(new_belief)
            else:
                for i, belief in enumerate(self.beliefs):
                    if new_belief >= belief:
                        self.beliefs.insert(i, new_belief)
                        break


    def delete(self, formula):
        """
        Remove any belief with given formula (in case there are any dupplicates)
        """
        for i, belief in enumerate(self.beliefs):
            if belief.formula == formula:
                self.beliefs.pop(i)


    def contract(self, formula, order):
        """
        Remove the belief from the Base
        """
        prop_cnf = to_cnf(formula)
        _validate_order(order)

        to_delete = []
        new_beliefs = []

        self.expanded = True
        for i, belief in enumerate(self.beliefs):
            new_beliefs.append(belief)
            
            if entailment(new_beliefs, prop_cnf) and order >= belief.order:
                to_delete.append(belief)
                new_beliefs.pop(len(new_beliefs) -1)
            elif entailment(new_beliefs, prop_cnf) and order < belief.order:
                self.expanded = False

        self.beliefs = [belief for belief in self.beliefs if belief not in to_delete]
       
    def expand(self, formula, order):
        """
        Add the belief to the Base by expanding it
        """
         # Check if the order is within range
        _validate_order(order)
        if "<>" in formula:
            formula = self.parsing_bicond(formula)
        self.add(formula, order)
    
    def revise(self, formula, order):
        """
        The belief is added and other things are removed,
        so that the resulting new belief set is consistent
        """
        _validate_order(order)
        if "<>" in formula:
            formula = self.parsing_bicond(formula)
        cnf = to_cnf(formula)

        # Check for contradiction in proposition
        if not entailment([], ~cnf):
            # this is a tautology
            if entailment([], cnf):
                order = 1
            elif not entailment(self.beliefs, cnf):
                negated_cnf = to_cnf(f'~({cnf})')
                self.contract(negated_cnf, order)
            else:
                self.contract(cnf, order)

            if (self.expanded):
                self.expand(formula, order)
        else:
            Warning("Contradiction in proposition")

    def clear(self):
        """
        Empty the Belief base
        """
        self.beliefs.clear()
  

class Belief:
    def __init__(self, formula, order=None):
        self.formula = formula
        self.order = order

    def __eq__(self, newBelief):
        return self.order == newBelief.order and self.formula == newBelief.formula
    
    def __ge__(self, newBelief):
        return self.order >= newBelief.order

    def __gt__(self,newBelief):
        return self.order > newBelief.order