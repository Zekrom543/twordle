import tkinter
import customtkinter
import main
import five_letter_word
import wordle_logic
import requests

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Root window
root = customtkinter.CTk()
root.geometry("900x700")

# Function to manage frame switching
def next_frame(current_frame, next_frame):
    current_frame.pack_forget()  # Hide the current frame
    next_frame.pack(pady=20, padx=60, fill="both", expand=True)  # Show the next frame

# Frame 1: Main Menu
frame_main = customtkinter.CTkFrame(master=root)
frame_main.pack(pady=20, padx=60, fill="both", expand=True)

label_main = customtkinter.CTkLabel(master=frame_main, text="Twordle", font=("Impact", 24))
label_main.pack(pady=12, padx=10)

label_instructions = customtkinter.CTkLabel(master=frame_main, text="Hello and welcome to Twordle! \nThis game was made during our 2024 Destin, FL trip \nbecause we were bored and decided to code our boredom away.\n", font=("Ariel", 16))
label_instructions.pack(pady = 12, anchor = "n")


continue_button = customtkinter.CTkButton(
    master=frame_main, 
    text="Continue", 
    command=lambda: next_frame(frame_main, frame_game)
)
continue_button.pack(pady=12, padx=10)

quit_button = customtkinter.CTkButton(master=frame_main, text = "Quit", fg_color= '#EA0000', hover_color = '#B20000', command=root.destroy)
quit_button.pack(pady = 12, padx = 10)

# Frame 2: Game Screen
frame_game = customtkinter.CTkFrame(master=root)

label_game = customtkinter.CTkLabel(master=frame_game, text="Twordle", font=("Impact", 24))
label_game.pack(pady=12, anchor = "n")

grid_frame = customtkinter.CTkFrame(master=frame_game)
grid_frame.pack(pady=10, anchor="n")

entry_game = customtkinter.CTkEntry(master=frame_game, placeholder_text="Enter Word")
entry_game.pack(pady=12, padx=10)

enter_button = customtkinter.CTkButton(master=frame_game, text="Enter", command=lambda: None)
enter_button.pack(pady=12, padx=10)

back_button = customtkinter.CTkButton(master=frame_game, text="Back", command=lambda: next_frame(frame_game, frame_main))
back_button.pack(pady=12, padx=10)

quit_button = customtkinter.CTkButton(master=frame_game, text = "Quit", fg_color= '#EA0000', hover_color = '#B20000', command=root.destroy)
quit_button.pack(pady = 12, padx = 10)

#grid making
grid = []
for i in range(6):
    row = []
    for j in range(5):
        label_grid = customtkinter.CTkLabel(master=grid_frame, text = "", width=50, height=50, fg_color="grey")
        label_grid.grid(row=i, column=j, padx = 5, pady = 5)
        row.append(label_grid)
    grid.append(row)

# Start the application
root.mainloop()
