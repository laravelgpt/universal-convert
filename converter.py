import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, UnidentifiedImageError, ImageTk
from moviepy import VideoFileClip, AudioFileClip
import pypandoc
import customtkinter as ctk
import subprocess
import sys
import shutil

# Set appearance mode and color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def check_ffmpeg():
    """Check if FFmpeg is installed."""
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        messagebox.showerror("Error", "FFmpeg is not installed. Please install FFmpeg manually and add it to PATH.")
        sys.exit(1)

# Ensure FFmpeg is installed
check_ffmpeg()

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal File Converter")
        self.root.geometry("600x500")

        # File selection
        self.file_label = ctk.CTkLabel(root, text="Select a file to convert:", font=("Arial", 14))
        self.file_label.pack(pady=10)

        self.file_button = ctk.CTkButton(root, text="Browse", command=self.select_file)
        self.file_button.pack(pady=5)

        # Format selection
        self.format_label = ctk.CTkLabel(root, text="Select target format:", font=("Arial", 14))
        self.format_label.pack(pady=10)

        self.format_var = tk.StringVar(value="mp4")
        self.format_menu = ctk.CTkOptionMenu(root, variable=self.format_var, values=["mp4", "avi", "mov", "mp3", "wav", "jpg", "png", "pdf", "docx"])
        self.format_menu.pack(pady=5)

        # Convert button
        self.convert_button = ctk.CTkButton(root, text="Convert", command=self.convert_file)
        self.convert_button.pack(pady=20)

        self.selected_file = None

    def select_file(self):
        self.selected_file = filedialog.askopenfilename()
        if self.selected_file:
            self.file_label.configure(text=f"Selected: {os.path.basename(self.selected_file)}")

    def convert_file(self):
        if not self.selected_file:
            messagebox.showerror("Error", "No file selected!")
            return

        target_format = self.format_var.get()
        output_file = filedialog.asksaveasfilename(defaultextension=f".{target_format}")

        if output_file:
            try:
                file_extension = os.path.splitext(self.selected_file)[1].lower()
                if file_extension in [".mp4", ".avi", ".mov", ".mkv", ".flv", ".webm"]:
                    self.convert_video(output_file, target_format)
                elif file_extension in [".mp3", ".wav", ".ogg"]:
                    self.convert_audio(output_file, target_format)
                elif file_extension in [".jpg", ".png"]:
                    self.convert_image(output_file, target_format)
                elif file_extension in [".pdf", ".docx"]:
                    self.convert_document(output_file, target_format)
                messagebox.showinfo("Success", "File converted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Conversion failed: {e}")

    def convert_video(self, output_file, target_format):
        try:
            command = ["ffmpeg", "-i", self.selected_file, "-c:v", "libx264", "-preset", "fast", "-crf", "23", output_file]
            subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except Exception as e:
            raise Exception(f"Video conversion failed: {e}")

    def convert_audio(self, output_file, target_format):
        try:
            command = ["ffmpeg", "-i", self.selected_file, "-q:a", "0", "-map", "a", output_file]
            subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except Exception as e:
            raise Exception(f"Audio conversion failed: {e}")

    def convert_image(self, output_file, target_format):
        try:
            img = Image.open(self.selected_file)
            img.save(output_file, format=target_format.upper())
        except UnidentifiedImageError:
            raise Exception("Unsupported image format!")

    def convert_document(self, output_file, target_format):
        try:
            pypandoc.convert_file(self.selected_file, target_format, outputfile=output_file)
        except Exception as e:
            raise Exception(f"Document conversion failed: {e}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = ConverterApp(root)
    root.mainloop()
