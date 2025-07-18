import tkinter as tk
import time
import math

# --- Function to update time ---
def update_time():
    current_time = time.strftime("%H:%M:%S")
    canvas.itemconfig(time_text, text=current_time)
    root.after(1000, update_time)

# --- Main Window ---
root = tk.Tk()
root.title("Circular Digital Clock")
root.geometry("400x400")
root.configure(bg="#0f172a")

# --- Create a Canvas (for drawing circle and text) ---
canvas = tk.Canvas(root, width=400, height=400, bg="#0f172a", highlightthickness=0)
canvas.pack()

# --- Draw Circular Clock Outline ---
circle = canvas.create_oval(50, 50, 350, 350, fill="#0f172a", outline="#38bdf8", width=8)

# --- Add glowing background effect (optional halo) ---
glow = canvas.create_oval(40, 40, 360, 360, outline="#1e3a8a", width=2)

# --- Add Time Text in Center ---
time_text = canvas.create_text(200, 200, text="", fill="#38bdf8", font=("Arial", 36, "bold"))

# --- Start the time update loop ---
update_time()

# --- Run the Application ---
root.mainloop()
