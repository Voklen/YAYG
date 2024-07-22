import tkinter as tk
from tkinter import font
from tkinter import filedialog
import tkinter.ttk as ttk
from yt_dlp import YoutubeDL, utils

folder_selected = ""


def main():
    title_font = font.Font(size=36)
    lbl_title = ttk.Label(
        text="Youtube Downloader",
        font=title_font,
        padding=30,
    )
    lbl_title.pack()

    btn_select_file = ttk.Button(text="Select folder", command=select_folder)
    btn_select_file.pack()

    ent_url = ttk.Entry(width=50)
    ent_url.pack()

    btn_download_mp3 = ttk.Button(
        text="Download mp3",
        command=lambda: download_mp3(ent_url),
    )
    btn_download_mp3.pack()
    btn_download_mp4 = ttk.Button(text="Download mp4")
    btn_download_mp4.pack()


def select_folder():
    global folder_selected
    folder_selected = filedialog.askdirectory()


def download_mp3(ent_url):
    download(ent_url.get())


def download(url):
    global folder_selected
    URLS = [url]
    params = {"paths": {"home": folder_selected}}
    with YoutubeDL(params) as ydl:
        try:
            ydl.download(URLS)
        except utils.YoutubeDLError as e:
            tk.messagebox.showerror(
                title="An error occured",
                message=e.msg,
            )


if __name__ == "__main__":
    window = tk.Tk()
    main()
    window.mainloop()
