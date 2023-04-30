from pydoc import resolve
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from sympy import *
from sympy.logic.boolalg import to_cnf, And, Or, Not
from BeliefBase import *
#Define a class for the GUI
class BeliefRevisionGUI:

    def __init__(self):
        # Initialize GUI window
        self.obj = BeliefBase() 
        self.window = tk.Tk()
<<<<<<< HEAD
        self.window.geometry("400x350")
=======
        self.window.geometry("500x300")
>>>>>>> f7af75720740fdb4d47a66d37bdf330572dd448b
        self.window.title("Belief Revision GUI")
        self.window.configure(bg="#fce2ab")

        # Create input box for propositional formula
        self.formula_label = tk.Label(self.window, text="Enter a propositional formula:", bg="#fce2ab")
        self.formula_label.pack()
<<<<<<< HEAD
        self.formula_entry = tk.Entry(self.window, width=20)
=======
        self.formula_entry = tk.Entry(self.window, width=40)
>>>>>>> f7af75720740fdb4d47a66d37bdf330572dd448b
        self.formula_entry.pack()

        # Create input box for formula order
        self.order = tk.Label(self.window, text="Enter the order for the above formula:", bg="#fce2ab")
        self.order.pack()
<<<<<<< HEAD
        self.order = tk.Entry(self.window, width=20)
=======
        self.order = tk.Entry(self.window, width=40)
>>>>>>> f7af75720740fdb4d47a66d37bdf330572dd448b
        self.order.pack()

        buttonFrame = Frame(self.window)
        buttonFrame.pack()

        # Create button to revise formula
        self.revise_button = tk.Button(buttonFrame, text="Revise", command = lambda obj=self.obj: self.revise_function(obj), bg="#cbedee")
        self.revise_button.grid(row=0, column=1)
        self.revise_button.grid_rowconfigure(0, weight=1)

        # Create button to contract formula
        self.contract_button = tk.Button(buttonFrame, text="Contract", command = lambda obj=self.obj: self.contract_function(obj), bg="#cbedee")
        self.contract_button.grid(row=0, column=2)

        # Create button to expand formula
        self.expand_button = tk.Button(buttonFrame, text="Expand", command = lambda obj=self.obj: self.expand_function(obj), bg="#cbedee")
        self.expand_button.grid(row=0, column=3)

        # Create button to delete the belief base
        self.empty_button = tk.Button(buttonFrame, text="Empty", command = lambda obj=self.obj: self.empty_function(obj), bg="#cbedee")
        self.empty_button.grid(row=1, column=2)

        # Create textbox for belief base
        self.output_label = tk.Label(self.window, text="Belief Base:", bg="#fce2ab")
        self.output_label.pack()
<<<<<<< HEAD
        self.output_text = tk.Label(self.window, height=7, width=30, borderwidth=3, relief="sunken", bg="#f2bb70")
=======
        self.output_text = tk.Label(self.window, height=7, width=30, borderwidth=3, relief="sunken")
>>>>>>> f7af75720740fdb4d47a66d37bdf330572dd448b
        self.output_text.pack()
        
        self.window.mainloop()

<<<<<<< HEAD
    def empty_function(self, obj):
            # Delete all beliefs from the belief base
            obj.clear()
            
             # Update the content of the belief base
            display_base(self, obj.beliefs)


    def contract_function(self, obj):
        formula_str, order = get_parameters(self)
        if formula_str != "":
            order = float(self.order.get())
            # Perform the belief contraction operation
            obj.contract(formula_str, order)
=======
    def revise_formula(self, obj):
        # Get the input formula and selected operation from th
        formula_str = self.formula_entry.get()
        operation = self.operation_var.get()

        if formula_str == "" or self.order.get() == "":
            messagebox.showinfo("Warnig", "Formula and order cannot be empty!")
        else:
            order = float(self.order.get())
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
>>>>>>> f7af75720740fdb4d47a66d37bdf330572dd448b
            
            # Update the content of the belief base       
            display_base(self, obj.beliefs)
    
    def expand_function(self, obj):
        formula_str, order = get_parameters(self)
        if formula_str != "":
            # Perform the belief expand operation
            obj.expand(formula_str, order)
            
            # Update the content of the belief base       
            display_base(self, obj.beliefs)

    def revise_function(self, obj):
        formula_str, order = get_parameters(self)
        if formula_str != "":
            # Perform the belief revision operation
            obj.revise(formula_str, order)
            
            # Update the content of the belief base
            display_base(self, obj.beliefs)
              
def get_parameters(self):
    # Get the input formula and selected operation from th
    formula_str = self.formula_entry.get()

    if formula_str == "" or self.order.get() == "":
        messagebox.showinfo("Warnig", "Formula and order cannot be empty!")
        return "", 0
    else:
        order = float(self.order.get())
        return formula_str, order

def display_base(self, beliefs):
    belief_base_content = ""
    for belief in beliefs:
        belief_base_content = belief_base_content + " (" + str(belief.formula) + ", " + str(belief.order) +")"
        print (belief.formula)
        print(belief.order)
    self.output_text["text"] = belief_base_content


BeliefRevisionGUI()