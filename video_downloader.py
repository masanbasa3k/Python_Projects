from pytube import YouTube

# module
def download_youtube_video():
    link = input("Enter the YouTube video URL: ")
    yt_object = YouTube(link)
    # getting best resolution
    yt_object = yt_object.streams.get_highest_resolution()
    try:
        # download
        yt_object.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

if __name__ == '__main__':
    download_youtube_video()