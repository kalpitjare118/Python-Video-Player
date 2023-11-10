'''
This is video player made in Python by ' github.com/kalpitjare118 ' using vlc and tkinter library 
'''

import tkinter as tk
from tkinter import ttk, filedialog
import vlc
from ttkthemes import ThemedStyle

# Create a Tkinter window
root = tk.Tk()
root.title("Modern Video Player")

# Set a fixed window size
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Initialize VLC player
instance = vlc.Instance()
player = instance.media_player_new()

# Create a Frame to hold the controls
control_frame = ttk.Frame(root)
control_frame.grid(row=0, column=0, sticky='nsew')
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Create a Canvas to hold the video player
canvas = tk.Canvas(control_frame, bg='black')
canvas.grid(row=0, column=0, sticky='nsew')

# Create a Frame to hold the control buttons and volume slider
button_frame = ttk.Frame(root)
button_frame.grid(row=1, column=0, sticky='ew')

# Function to play the video
def play_video():
    player.play()

# Function to pause the video
def pause_video():
    player.pause()

# Function to play the next video (update with your logic)
def play_next_video():
    # Add your logic to play the next video
    pass

# Function to play the previous video (update with your logic)
def play_previous_video():
    # Add your logic to play the previous video
    pass

# Function to browse for a video file
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.mkv *.avi")])
    if file_path:
        media = instance.media_new(file_path)
        player.set_media(media)

# Create control buttons with modern styling
style = ThemedStyle(root)
style.set_theme("plastik")

play_button = ttk.Button(button_frame, text="Play", command=play_video)
pause_button = ttk.Button(button_frame, text="Pause", command=pause_video)
next_button = ttk.Button(button_frame, text="Next", command=play_next_video)
previous_button = ttk.Button(button_frame, text="Previous", command=play_previous_video)
browse_button = ttk.Button(button_frame, text="Browse", command=browse_file)

play_button.grid(row=0, column=0)
pause_button.grid(row=0, column=1)
next_button.grid(row=0, column=2)
previous_button.grid(row=0, column=3)
browse_button.grid(row=0, column=4)

# Create a volume slider
volume_label = ttk.Label(button_frame, text="Volume:")
volume_slider = ttk.Scale(button_frame, from_=0, to=100, orient="horizontal")
volume_label.grid(row=0, column=5)
volume_slider.grid(row=0, column=6)

# Bind the volume slider to the player's audio_set_volume method
def set_volume(value):
    player.audio_set_volume(int(value))

volume_slider.set(100)  # Initialize the volume to maximum
volume_slider.bind("<Motion>", lambda event: set_volume(volume_slider.get()))

# Function to toggle between fullscreen and windowed mode
def toggle_fullscreen():
    if root.attributes("-fullscreen") == 0:
        root.attributes("-fullscreen", 1)
        root.geometry("")  # Clear the fixed size
    else:
        root.attributes("-fullscreen", 0)
        root.geometry(f"{window_width}x{window_height}")

# Create a fullscreen button
fullscreen_button = ttk.Button(button_frame, text="Fullscreen", command=toggle_fullscreen)
fullscreen_button.grid(row=0, column=7)

# Function to resize the video player canvas
def resize(event):
    canvas.configure(width=event.width, height=event.height)

control_frame.bind("<Configure>", resize)

# Embed the video player in the Canvas
player.set_hwnd(canvas.winfo_id())

# Start the Tkinter main loop
root.mainloop()
