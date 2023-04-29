


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

    def add(self, formula, order):
        """
        Add a belief to the base (sorted by order) without checking the validity.
        """
        # Or we can add the belief to the belief base to the correspondent index (sorted by order)
        # To do
        return 1

    def delete(self, formula, order):
        """
        Remove any belief with given formula (in case there are any dupplicates)
        """
        # To do
        return 1

    def contract(self, formula, order):
        """
        Remove the belief from the Base
        """
        return 1
    
    def expand(self, formula, order):
        """
        Add the belief to the Base by expanding it
        """
        return 1
    
    def revise(self, formula, order):
        """
        The belief is added and other things are removed,
        so that the resulting new belief set is consistent
        """
        return 1
    
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
    
    def __repr__(self):
        return f'Belief({self.formula}, order={self.order})'