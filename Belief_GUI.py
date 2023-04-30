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
        self.window.geometry("400x350")
        self.window.title("Belief Revision GUI")
        self.window.configure(bg="#fce2ab")

        # Create input box for propositional formula
        self.formula_label = tk.Label(self.window, text="Enter a propositional formula:", bg="#fce2ab")
        self.formula_label.pack()
        self.formula_entry = tk.Entry(self.window, width=20)
        self.formula_entry.pack()

        # Create input box for formula order
        self.order = tk.Label(self.window, text="Enter the order for the above formula:", bg="#fce2ab")
        self.order.pack()
        self.order = tk.Entry(self.window, width=20)
        self.order.pack()

        buttonFrame = Frame(self.window, bg="#fce2ab", pady=15)
        buttonFrame.pack()

        # Create button to revise formula
        self.revise_button = tk.Button(buttonFrame, text="Revise", command = lambda obj=self.obj: self.revise_function(obj), bg="#d6b181")
        self.revise_button.grid(row=0, column=1)
        self.revise_button.grid_rowconfigure(0, weight=1)

        # Create button to contract formula
        self.contract_button = tk.Button(buttonFrame, text="Contract", command = lambda obj=self.obj: self.contract_function(obj), bg="#d6b181")
        self.contract_button.grid(row=0, column=2)

        # Create button to expand formula
        self.expand_button = tk.Button(buttonFrame, text="Expand", command = lambda obj=self.obj: self.expand_function(obj), bg="#d6b181")
        self.expand_button.grid(row=0, column=3)

        # Create button to delete the belief base
        self.empty_button = tk.Button(buttonFrame, text="Empty", command = lambda obj=self.obj: self.empty_function(obj), bg="#d6b181")
        self.empty_button.grid(row=1, column=2)

        # Create textbox for belief base
        self.output_label = tk.Label(self.window, text="Belief Base:", bg="#fce2ab", )
        self.output_label.pack()
        self.output_text = tk.Label(self.window, height=7, width=50, borderwidth=3, relief="sunken", bg="#f2bb70", wraplength= 300)
        self.output_text.pack()
        
        self.window.mainloop()

    def empty_function(self, obj):
            # Delete all beliefs from the belief base
            obj.clear()
            
             # Update the content of the belief base
            display_base(self, obj.beliefs)
            self.formula_entry.delete(0, END)
            self.order.delete(0, END)

    def contract_function(self, obj):
        formula_str, order = get_parameters(self)
        if formula_str != "":
            order = float(self.order.get())
            # Perform the belief contraction operation
            if "<>" in formula_str:
                formula_str = obj.parsing_bicond(formula_str)
            obj.contract(formula_str, order)
            
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
        messagebox.showinfo("Warning", "Formula and order cannot be empty!")
        return "", 0
    else:
        order = float(self.order.get())
        return formula_str, order

def display_base(self, beliefs):
    belief_base_content = ""
    for belief in beliefs:
        belief_base_content = belief_base_content + " (" + str(belief.formula) + ", " + str(belief.order) +")"
    self.output_text["text"] = belief_base_content


BeliefRevisionGUI()