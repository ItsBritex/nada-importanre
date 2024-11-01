import os
import yt_dlp

def descargar_youtube(url, formato):
    try:
        ydl_opts = {}
        
        if formato.lower() == 'mp3':
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': '%(title)s.%(ext)s',
            }
        elif formato.lower() == 'mp4':
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': '%(title)s.%(ext)s',
            }
        else:
            print("Formato no válido. Por favor, elige 'mp3' o 'mp4'.")
            return

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("Descarga completada.")
    
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

# Solicitar entrada del usuario
url = input("Ingresa la URL del video de YouTube: ")
formato = input("Elige el formato (mp3/mp4): ")

# Llamar a la función
descargar_youtube(url, formato)