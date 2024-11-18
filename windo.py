import os
import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import pygame
import threading
import time

class KeyboardSoundApp:
    def __init__(self):
        # Main window setup
        self.root = tk.Tk()
        self.root.title("Dynamic Keyboard Sounds")
        self.root.geometry("300x200")

        # Sound file path
        self.sound_file = r"sounds/click.mp3"
        
        # Pygame mixer initialization
        pygame.mixer.init()
        self.sound_channel = pygame.mixer.Channel(0)
        self.sound = pygame.mixer.Sound(self.sound_file)

        # State tracking
        self.sounds_enabled = False
        self.last_key_time = 0
        self.typing_timer = None

    def create_ui(self):
        # Sound status label
        self.status_label = tk.Label(self.root, text=f"Sound: {os.path.basename(self.sound_file)}")
        self.status_label.pack(pady=10)

        # Toggle button
        self.toggle_btn = tk.Button(self.root, text="Start Keyboard Sounds", command=self.toggle_sounds)
        self.toggle_btn.pack(pady=10)

    def play_sound(self):
        if not self.sound_channel.get_busy():
            self.sound_channel.play(self.sound)

    def on_press(self, key):
        if not self.sounds_enabled:
            return

        # Play sound immediately
        self.play_sound()
        
        # Reset the timer
        if self.typing_timer:
            self.typing_timer.cancel()
        
        # Set a new timer to stop sounds if no key is pressed for 0.5 seconds
        self.typing_timer = threading.Timer(0.5, self.stop_sounds)
        self.typing_timer.start()

    def stop_sounds(self):
        # Stop the sound channel
        self.sound_channel.stop()

    def toggle_sounds(self):
        self.sounds_enabled = not self.sounds_enabled
        if self.sounds_enabled:
            # Start keyboard listener
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()

            self.toggle_btn.config(text="Stop Keyboard Sounds")
            self.status_label.config(text="Keyboard sounds active")
        else:
            # Stop keyboard listener
            self.listener.stop()
            self.sound_channel.stop()
            if self.typing_timer:
                self.typing_timer.cancel()

            self.toggle_btn.config(text="Start Keyboard Sounds")
            self.status_label.config(text="Keyboard sounds stopped")

    def __init__(self):
        # Main window setup
        self.root = tk.Tk()
        self.root.title("Dynamic Keyboard Sounds")
        self.root.geometry("300x200")

        # Sound file path
        self.sound_file = r"sounds/click.mp3"
        
        # Pygame mixer initialization
        pygame.mixer.init()
        self.sound_channel = pygame.mixer.Channel(0)
        self.sound = pygame.mixer.Sound(self.sound_file)

        # State tracking
        self.sounds_enabled = False
        self.typing_timer = None

        # Create UI
        self.create_ui()

    def run(self):
        self.root.mainloop()

def main():
    app = KeyboardSoundApp()
    app.run()

if __name__ == "__main__":
    main()