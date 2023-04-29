from pydoc import resolve
import tkinter as tk
from tkinter import messagebox
from sympy import *
from sympy.logic.boolalg import to_cnf, And, Or, Not
from BeliefBase import *
#Define a class for the GUI
class BeliefRevisionGUI:

    def __init__(self):
        # Initialize GUI window
        self.obj = BeliefBase() 
        self.window = tk.Tk()
        self.window.title("Belief Revision GUI")

        # Create input box for propositional formula
        self.formula_label = tk.Label(self.window, text="Enter a propositional formula:")
        self.formula_label.pack()
        self.formula_entry = tk.Entry(self.window, width=70)
        self.formula_entry.pack()

        # Create input box for order formula
        self.order = tk.Label(self.window, text="Enter the order:")
        self.order.pack()
        self.order = tk.Entry(self.window, width=70)
        self.order.pack()

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
        self.revise_button = tk.Button(self.window, text="Revise Formula", command = lambda obj=self.obj: self.revise_formula(obj))
        self.revise_button.pack()

        # Create output box for revised formula
        self.output_label = tk.Label(self.window, text="Revised Formula:")
        self.output_label.pack()
        self.output_text = tk.Label(self.window, height=7, width=70)
        self.output_text.pack()
        
        self.window.mainloop()

    def revise_formula(self, obj):
        # Get the input formula and selected operation from th
        formula_str = self.formula_entry.get()
        operation = self.operation_var.get()
        order = float(self.order.get())

        if formula_str == "" or self.order.get() == "":
            messagebox.showinfo("Warnig", "Formula and order cannot be empty!")
        else:
            # Perform the appropriate belief revision operation
            if operation == "Revision":
            # Get the revision formula and revise the input formula 
                obj.revise(formula_str, order)
            elif operation == "Contraction":
                # Contract the input formula
                obj.contract(formula_str, order)
            elif operation == "Expansion":
                # Expand the input formula
                obj.expand(formula_str, order)
            
            revised_formula_str = display_base(obj.beliefs)
            # Update the output box with the revised formula
            
            self.output_text["text"] = revised_formula_str
    
def display_base(beliefs):
    revised_formula_str = ""
    for belief in beliefs:
        revised_formula_str = revised_formula_str + " (" + str(belief.formula) + ", " + str(belief.order) +")"
        print (belief.formula)
        print(belief.order)
    return revised_formula_str


BeliefRevisionGUI()