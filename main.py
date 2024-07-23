import tkinter as tk
from tkinter import font
from tkinter import filedialog
import tkinter.ttk as ttk
from yt_dlp import YoutubeDL, utils
import os

folder_selected = os.getcwd()
lbl_current_folder = None


def main():
    title_font = font.Font(size=36)
    lbl_title = ttk.Label(
        text="Youtube Downloader",
        font=title_font,
        padding=30,
    )
    lbl_title.pack()

    btn_select_file = ttk.Button(text="Change folder", command=select_folder)
    btn_select_file.pack()
    global lbl_current_folder
    lbl_current_folder = ttk.Label(text=f"Current folder: {folder_selected}")
    lbl_current_folder.pack()

    ent_url = ttk.Entry(width=50)
    ent_url.pack()

    btn_download_audio = ttk.Button(
        text="Download audio",
        command=lambda: download_audio(ent_url.get()),
    )
    btn_download_audio.pack()
    btn_download_video = ttk.Button(
        text="Download video",
        command=lambda: download(ent_url.get()),
    )
    btn_download_video.pack()


def select_folder():
    global folder_selected
    folder_selected = filedialog.askdirectory()
    lbl_current_folder["text"] = f"Current folder: {folder_selected}"


def download_audio(url):
    download(
        url,
        {
            "format": "mp3/bestaudio/best",
            "postprocessors": [
                {  # Extract audio using ffmpeg
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                }
            ],
        },
    )


def download(url, additional_params=None):
    global folder_selected
    URLS = [url]
    params = {
        "paths": {"home": folder_selected},
    }
    if additional_params != None:
        params = {**params, **additional_params}
    with YoutubeDL(params) as ydl:
        try:
            ydl.download(URLS)
        except utils.YoutubeDLError as e:
            tk.messagebox.showerror(title="Error", message=e.msg)


if __name__ == "__main__":
    window = tk.Tk()
    main()
    window.mainloop()
