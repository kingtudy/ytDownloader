from tkinter import *
from pytube import YouTube
from moviepy.editor import *

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("youtube mp3/video downloader")

Label(root, text='Youtube MP3/VIDEO Downloader', font='arial 20 bold').pack()

link = StringVar()
Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


def download_video(url, video_output_path):
    try:
        # Debug link name
        print("the link is: " + link.get())

        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        print("Downloading video...")
        video_stream.download(video_output_path)
        print("Video downloaded successfully.")
    except Exception as e:
        print("Error occurred while downloading the video:", str(e))


def download_audio(url, audio_output_path):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(only_audio=True).first()

        print("Downloading mp3...")
        out_file = video_stream.download(output_path=audio_output_path)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("MP3 downloaded successfully.")

    except Exception as e:
        print("Error downloading MP3:", str(e))

def Downloader():
    # YouTube video URL
    youtube_url = str(link.get())

    # Output paths for downloaded video and converted MP3
    video_output_path = "video"
    audio_output_path = "audio"

    # Download the video
    download_video(youtube_url, video_output_path)

    # Convert the video to MP3
    download_audio(youtube_url, audio_output_path)

    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=Downloader).place(x=180,
                                                                                                            y=150)
root.mainloop()

