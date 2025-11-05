#North Sussex Judo Monthly Fees Calculator

import tkinter as tk
from tkinter import messagebox

#Constants
WEEKLY_FEES = { 
    "Beginner": 25.00,
    "Intermediate": 30.00,
    "Elite": 35.00
}
COMPETITION_COST = 22.00
PRIVATE_HOUR_RATE = 9.50
MAX_PRIVATE_HOURS = 20
CATEGORY_LIMITS = {
    "Flyweight": 60,
    "Lightweight": 66,
    "Light-Middleweight": 73,
    "Middleweight": 81,
    "Light-Heavyweight": 90,
    "Heavyweight": "Unlimited" 
}

#Class Definition 
class Athlete: 
    """Represents an athlete with attributes and calculation methods."""

    def __init__(self, name, plan, weight, category, private_hours, competitions):
        self.name = name
        self.plan = plan 
        self.weight = weight
        self.category = category 
        self.private_hours = private_hours
        self.competitions = competitions 

    def validate_inputs(self):
        """Validate athlete data securely"""
        if self.plan not in WEEKLY_FEES:
            raise ValueError("Invalid training plan selected.") 
        if self.category not in CATEGORY_LIMITS:
            raise ValueError("Invalid category.")
    
    #Auto-cap private hours to MAX_PRIVATE_HOURS
        if self.private_hours < 0:
            raise ValueError("Private training hours cannot be negative.") 
        if self.private_hours > MAX_PRIVATE_HOURS:
            messagebox.showinfo("Info", f"Private training hours capped to 20 hours.")
            self.private_hours = MAX_PRIVATE_HOURS
        
        if self.competitions < 0: 
            raise ValueError("Number of competitions cannot be negative.") 
        
        #Beginners cannot enter competitions
        if self.plan == "Beginner": 
            self.competitions = 0 #Beginners cannot compete #TEST Beginner + any competitions entered = Competition Cost should be £0.00

    def calculate_fees(self): 
        """Procedural control: Control total monthly cost"""
        weekly_fee = WEEKLY_FEES[self.plan] 
        training_cost = weekly_fee * 4 
        private_cost = self.private_hours * PRIVATE_HOUR_RATE 
        competition_cost = self.competitions * COMPETITION_COST 
        total_cost = training_cost + private_cost + competition_cost 
        return training_cost, private_cost, competition_cost, total_cost 

    def weight_message(self): 
        """Return appropriate weight category message""" 
        limit = CATEGORY_LIMITS[self.category] 
        if limit == "Unlimited":
            return "No upper limit for Heavyweight category." #TEST Heavyweight 
        elif self.weight > limit: 
            return f"OVER by {self.weight - limit:.1f} kg."
        elif self.weight < limit:
            return f"UNDER by {limit - self.weight:.1f} kg."
        else: 
            return "Exactly on the limit." 

#GUI Setup 
root = tk.Tk() 
root.title("North Sussex Judo Monthly Fees Calculator") 
root.geometry("500x600") 

#Input Fields 
tk.Label(root, text= "Athlete Name:").pack() 
name_entry = tk.Entry(root) 
name_entry.pack()

tk.Label(root, text = "Training Plan:").pack() 
plan_var = tk.StringVar(value="Beginner")
tk.OptionMenu(root, plan_var, * WEEKLY_FEES.keys()).pack()

tk.Label(root, text = "Weight (kg):").pack() 
weight_entry = tk.Entry(root) 
weight_entry.pack()

tk.Label(root, text = "Competition Category:").pack() 
category_var = tk.StringVar(value="Flyweight") 
tk.OptionMenu(root, category_var, * CATEGORY_LIMITS.keys()).pack()

tk.Label(root, text = "Private Training Hours (0-20):").pack() 
private_hours_entry = tk.Entry(root) 
private_hours_entry.pack() 

tk.Label(root, text = "Number of Competitions:").pack()
competitions_entry = tk.Entry(root)
competitions_entry.pack() 

#Output Label
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text).pack(pady=20)
        
#Event-Driven GUI Functions
def calculate_button_clicked(): 
    """Triggered when the user clicks 'Calculate'."""
    try:
        name = name_entry.get().title().strip()
        plan = plan_var.get() 
        weight = float(weight_entry.get()) 
        category = category_var.get() 
        private_hours = float(private_hours_entry.get()) 
        competitions = int(competitions_entry.get()) 

        athlete = Athlete(name, plan, weight, category, private_hours, competitions)
        athlete.validate_inputs() 

        training_cost, private_cost, competition_cost, total_cost = athlete.calculate_fees() 
        weight_msg = athlete.weight_message() 

        result_text.set(
            f"Athlete: {athlete.name}\n"
            f"Plan: {athlete.plan}\n"
            f"Training Cost: £{training_cost:.2f}\n"
            f"Private Coaching: £{private_cost:.2f}\n"
            f"Competition Cost: £{competition_cost:.2f}\n"
            f"TOTAL: £{total_cost:.2f}\n"
            f"Weight Message: {weight_msg}"
        )
    except ValueError as ve: 
        messagebox.showerror("Input Error", str(ve)) 
    except Exception as e: 
        messagebox.showerror("Unexpected Error", f"{e}") 

#Calculate Buttons
calculate_button = tk.Button(root, text="Calculate Monthly Fees", command=calculate_button_clicked).pack(pady=10) 
tk.Button(root, text="Reset", command=lambda: result_text.set("")).pack(pady=5)

#Start GUI Loop
root.mainloop() 