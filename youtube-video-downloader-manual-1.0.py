import pytube
from time import sleep
from tqdm import tqdm
tipo_video = None

video_url = input("Inserte la url del video: ")
youtube = pytube.YouTube(video_url)

comando_calidad = youtube.streams.get_highest_resolution() #you can change highest_resolution to lowest_resulition or audio_only

sleep (0.5)
print("Descargando video...")

video = comando_calidad





for i in tqdm(range(100)):
    sleep(.1)

video.download(r'/home/rainyis/Descargas') #downloader rute

print("Descarga finalizada")