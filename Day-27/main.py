import tkinter as tk

window = tk.Tk()
window.title("Miles to KM Converter")

miles_input = tk.Entry()
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = tk.Label(text="0")
km_label.grid(column=1, row=1)  

calculate_button = tk.Button(text="Calculate")
calculate_button.grid(column=1, row=2)

def convert_miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    km_label.config(text=f"{km:.2f}")   
calculate_button.config(command=convert_miles_to_km)

window.mainloop()