from pydoc import resolve
import tkinter as tk
from sympy import *
from sympy.logic.boolalg import to_cnf, And, Or, Not

#Define a class for the GUI
class BeliefRevisionGUI:

    def __init__(self):
        # Initialize GUI window
        self.window = tk.Tk()
        self.window.title("Belief Revision GUI")

        # Create input box for propositional formula
        self.formula_label = tk.Label(self.window, text="Enter a propositional formula:")
        self.formula_label.pack()
        self.formula_entry = tk.Entry(self.window, width=70)
        self.formula_entry.pack()

        # Create dropdown menu for operation selection
        self.operation_label = tk.Label(self.window, text="Select an operation:")
        self.operation_label.pack()
        self.operation_options = ["Contraction", "Revision", "Expansion"]
        self.operation_var = tk.StringVar(self.window)
        self.operation_var.set(self.operation_options[0])
        self.operation_dropdown = tk.OptionMenu(self.window, self.operation_var, *self.operation_options)
        self.operation_dropdown.pack()

        # Create input box for revision formula (for revision operation)
        self.revision_label = tk.Label(self.window, text="Enter a revision formula (for revision operation):")
        self.revision_label.pack()
        self.revision_entry = tk.Entry(self.window, width=70)
        self.revision_entry.pack()
        self.revision_label.pack_forget()
        self.revision_entry.pack_forget()

        # Create button to revise formula
        self.revise_button = tk.Button(self.window, text="Revise Formula", command=self.revise_formula)
        self.revise_button.pack()

        # Create output box for revised formula
        self.output_label = tk.Label(self.window, text="Revised Formula:")
        self.output_label.pack()
        self.output_text = tk.Text(self.window, height=7, width=70)
        self.output_text.pack()

        self.window.mainloop()

    def revise_formula(self):
        # Get the input formula and selected operation from th
        formula_str = self.formula_entry.get()
        operation = self.operation_var.get()
        # Perform the appropriate belief revision operation
        if operation == "Revision":
        # Get the revision formula and revise the input formula
            revision_formula_str = self.revision_entry.get()
            revised_formula_str = str(revision(formula_str, revision_formula_str))
        elif operation == "Contraction":
            # Contract the input formula
            revised_formula_str = str(contract(formula_str))
        elif operation == "Expansion":
            # Expand the input formula
            revised_formula_str = str(expand(formula_str))
        # Update the output box with the revised formula
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, revised_formula_str)
        # Return the revised formula string (not strictly necessary)
        return revised_formula_str

# Define helper functions for belief revision operations
def contract(formula_str):
    # Convert the formula string into a symbolic expression
    formula = sympify(formula_str)
    # Convert the formula into CNF
    cnf = to_cnf(formula)
    # Extract the clauses from the CNF
    clauses = cnf.args
    # Create a set to store the resolvents
    resolvents = set()
    # Iterate over all pairs of clauses and find their resolvent
    """loop through all pairs of clauses in the CNF and computes their resolvent. 
    If the resolvent is empty, the loop continues to the next pair of clauses. 
    If the resolvent is already in the set of clauses, the loop continues to the
    next pair. Otherwise, the resolvent is added to the resolvents set."""
    for i, clause1 in enumerate(clauses):
        for j, clause2 in enumerate(clauses):
            if j <= i:
                continue
            resolvent = resolve(clause1, clause2)
            if not resolvent:
                continue
            if resolvent in clauses:
                continue
            resolvents.add(resolvent)
    if not resolvents:
        return formula
    return And(*resolvents)

#Revises the given propositional formula with the given revision formula.
def revision(formula_str, revision_formula_str): 
    """     Parameters:
        formula_str (str): The propositional formula to revise.
        revision_formula_str (str): The revision formula to use for revision.
            Returns:
        revised_formula (sympy expression): The revised formula."""
    formula = sympify(formula_str)
    revision_formula = sympify(revision_formula_str)
    return contract(Or(formula, revision_formula))

def expand(formula_str):
    formula = sympify(formula_str)
    return simplify(to_cnf(formula))

# Run GUI
BeliefRevisionGUI()
