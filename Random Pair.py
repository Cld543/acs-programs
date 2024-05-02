'''
Uses a tkinter window to generate randomly chosen pairs of 
letters and numbers. This is done without replacement
'''

#!/usr/bin/env python

import tkinter as tk
import random

nums = ['1', '2', '3', '4', '5', '6', '7']
chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T']

pairs = []

for x in nums:
    for y in chars:
        pairs.append(x+y)
        
print(pairs)
def generate_string():
    # List of possible characters

    
    # Generate the string without replacement
    random_string = pairs.pop(random.randint(0,len(pairs)))
    # Update the label with the generated string
    num_left = len(pairs)
    if num_left == 0:
        result_label.configure(text="No More Choices")
    else:
        result_label.configure(text=random_string)
    

# Create the main window
window = tk.Tk()
window.title("Random String Generator")

# Create the label to display the generated string
result_label = tk.Label(window, text="", font=("Helvetica", 24))
result_label.pack(pady=20)

# Create the button to generate the string
generate_button = tk.Button(window, text="Generate", command=generate_string)
generate_button.pack()

# Run the GUI event loop
window.mainloop()
