import tkinter
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Root window
root = customtkinter.CTk()
root.geometry("500x400")

# Function to switch frames
def next_frame(current_frame, next_frame):
    current_frame.pack_forget()  # Hide the current frame
    next_frame.pack(pady=20, padx=60, fill="both", expand=True)  # Show the next frame

# Frame 1: Main Menu
frame_main = customtkinter.CTkFrame(master=root)
frame_main.pack(pady=20, padx=60, fill="both", expand=True)

label_main = customtkinter.CTkLabel(master=frame_main, text="Twordle", font=("Impact", 24))
label_main.pack(pady=12, padx=10)

continue_button = customtkinter.CTkButton(
    master=frame_main, 
    text="Continue", 
    command=lambda: next_frame(frame_main, frame_game)
)
continue_button.pack(pady=12, padx=10)

# Frame 2: Game Screen
frame_game = customtkinter.CTkFrame(master=root)

# Create a nested frame for grid layout
grid_frame = customtkinter.CTkFrame(master=frame_game)
grid_frame.pack(pady=10)  # Pack grid frame first to position it at the top

# Create a grid layout in the nested frame
for i in range(5):
    for j in range(5):
        label_grid = customtkinter.CTkLabel(master=grid_frame, text=f"{i},{j}")
        label_grid.grid(row=i, column=j, padx=5, pady=5)

# Create a label using pack
label_game = customtkinter.CTkLabel(master=frame_game, text="Game Screen", font=("Impact", 20))
label_game.pack(pady=12)

# Back button using pack
back_button = customtkinter.CTkButton(
    master=frame_game, 
    text="Back", 
    command=lambda: next_frame(frame_game, frame_main)
)
back_button.pack(pady=10)

# Start the application
root.mainloop()
