import tkinter as tk
import random
import time

# Create main window
root = tk.Tk()
root.title("🎲 Dice Rolling Simulator")
root.geometry("400x500")
root.config(bg="#1e1e2f")

# Dice symbols
dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

# Title
title = tk.Label(root, text="Dice Rolling Simulator",
                 font=("Arial", 20, "bold"),
                 fg="white", bg="#1e1e2f")
title.pack(pady=20)

# Dice display label
dice_label = tk.Label(root, text="⚀",
                      font=("Arial", 100),
                      fg="#00ffcc", bg="#1e1e2f")
dice_label.pack(pady=20)

# Result text
result_label = tk.Label(root, text="Click Roll to start!",
                        font=("Arial", 14),
                        fg="yellow", bg="#1e1e2f")
result_label.pack(pady=10)

# Function to animate dice
def roll_dice():
    try:
        for _ in range(10):  # Animation loop
            face = random.choice(dice_faces)
            dice_label.config(text=face, fg=random_color())
            root.update()
            time.sleep(0.1)

        final = random.randint(1, 6)
        dice_label.config(text=dice_faces[final - 1], fg="#00ffcc")
        result_label.config(text=f"You rolled: {final}")

    except Exception as e:
        result_label.config(text="Error occurred!")

# Random color generator
def random_color():
    colors = ["#ff4d4d", "#4dff4d", "#4dd2ff", "#ffff4d", "#ff66ff"]
    return random.choice(colors)

# Roll button
roll_button = tk.Button(root, text="🎲 Roll Dice",
                        font=("Arial", 14, "bold"),
                        bg="#ff5722", fg="white",
                        padx=20, pady=10,
                        command=roll_dice)
roll_button.pack(pady=20)

# Exit button
exit_button = tk.Button(root, text="Exit",
                        font=("Arial", 12),
                        bg="red", fg="white",
                        command=root.quit)
exit_button.pack(pady=10)

# Run app
root.mainloop()