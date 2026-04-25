import youtube_dl

video_url = input("Enter the video url:\n")
with youtube_dl.YoutubeDL() as ydl:
    ydl.download([video_url])



    