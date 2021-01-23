import pytube
from time import sleep
from tqdm import tqdm
tipo_video = None

video_url = input("Inserte la url del video: ")
youtube = pytube.YouTube(video_url)
while tipo_video != "Alta" or tipo_video != "alta" or tipo_video != "Media" or tipo_video != "media" or tipo_video != "Baja" or tipo_video != "baja" or tipo_video != "Audio" or tipo_video != "audio":
    tipo_video = input(str("¿Como quieres descargar el video? Calidad: Alta, Media, Baja Tipo: Audio (Si quieres audio no especifiques la calidad)\n"))
    if tipo_video == "Alta" or tipo_video == "alta":
        comando_calidad = youtube.streams.get_highest_resolution()
        break
    elif tipo_video == "Media" or tipo_video == "media":
        comando_calidad = youtube.streams.first()
        break
    elif tipo_video == "Baja" or tipo_video == "baja":
        comando_calidad = youtube.streams.get_lowest_resolution()
        break
    elif tipo_video == "Audio" or tipo_video == "audio":
        comando_calidad = youtube.streams.get_audio_only()
        break
    else:
        print("ERROR: Debe poner el formato, un ejempo es en caso de que quiera alta calidad solo deberá poner Alta")

ruta_descarga1 = input("¿En que ruta quieres descargar el video? Debe poner la ruta de esta manera: C:/usuarios/usuario/videos\n")
ruta_descarga = (r'{}'.format(ruta_descarga1))

sleep (0.5)
print("Descargando video...")

video = comando_calidad





for i in tqdm(range(100)):
    sleep(.1)

video.download(ruta_descarga) #Downloader rute

print("Descarga finalizada")