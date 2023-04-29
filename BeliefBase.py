

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
        self.not_entailment = True

    def add(self, formula, order):
        """
        Add a belief to the base (sorted by order) without checking the validity.
        """
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
         # Set of maximal subset of KB that not imply other
        prop_cnf = to_cnf(formula)
        _validate_order(order)

        _to_delete = []
        self.not_entailment = True
        for i, belief in enumerate(self.beliefs):
            if entailment(self.beliefs[0:i+1], prop_cnf) and order >= belief.order:
                _to_delete.append(belief)
            elif entailment(self.beliefs[0:i+1], prop_cnf) and order < belief.order:
                self.not_entailment = False

        self.beliefs = [belief for belief in self.beliefs if belief not in _to_delete]
       
    def expand(self, formula, order):
        """
        Add the belief to the Base by expanding it
        """
         # Check if the order is within range
        _validate_order(order)
        self.add(formula, order)
    
    def revise(self, formula, order):
        """
        The belief is added and other things are removed,
        so that the resulting new belief set is consistent
        """
        _validate_order(order)

        cnf = to_cnf(formula)

        # Check for contradiction in proposition
        if not entailment([], ~cnf):
            # this is a tautology
            if entailment([], cnf):
                order = 1
            elif not entailment(self.beliefs, cnf):
                print(" in else")
                negated_cnf = to_cnf(f'~({cnf})')
                self.contract(negated_cnf, order)
            else:
                self.contract(cnf, order)

            if (self.not_entailment):
                self.expand(formula, order)
        else:
            Warning("Contradiction in proposition")
    def clear(self):
        """
        Empty the Belief base
        """
        self.beliefs.clear()

    # TO DO - other methods here such as:
    # clear (empty the belief set), 
    # len(return the length of the belief set),
    # getitem(return the belief on a certain index)
    # repr (print method for the Belief base)

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
    
    def print(self):
        return f'Belief({self.formula}, order={self.order})'