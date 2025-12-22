import webview
import yt_dlp
import os
import subprocess
import platform
from pathlib import Path # Librería para rutas universales

class Api:
    def __init__(self):
        self._window = None
        # Ubicación de los ejecutables (ffmpeg) dentro del EXE
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # UBICACIÓN DE DESCARGAS REAL: Carpeta "Downloads" del sistema
        self.download_path = os.path.join(Path.home(), "Downloads", "GreenLoader")
        self.setup_folders()

    def set_window(self, window):
        self._window = window

    def setup_folders(self):
        # Crea la carpeta GreenLoader en Descargas si no existe
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)
        for sub in ["Audio", "Video"]:
            path = os.path.join(self.download_path, sub)
            if not os.path.exists(path):
                os.makedirs(path)

    def open_folder(self):
        try:
            # Abrir la carpeta real de Descargas de Windows
            ruta = os.path.abspath(self.download_path)
            if platform.system() == "Windows":
                os.startfile(ruta)
            else:
                opener = "open" if platform.system() == "Darwin" else "xdg-open"
                subprocess.call([opener, ruta])
            return "Carpeta abierta"
        except: return "Error al abrir"

    def descargar(self, urls_raw, tipo, calidad):
        urls = [u.strip() for u in urls_raw.split('\n') if u.strip()]
        if not urls: return "Error: Sin enlaces"
        
        sub_dir = "Audio" if tipo == "audio" else "Video"
        ruta_final = os.path.join(self.download_path, sub_dir)
        
        ydl_opts = {
            'outtmpl': os.path.join(ruta_final, '%(title)s.%(ext)s'),
            'ffmpeg_location': self.base_dir, # FFmpeg se busca donde se descomprime el EXE
            'writethumbnail': True,
            'quiet': True,
            'no_warnings': True
        }
        
        if tipo == 'audio':
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [
                    {'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '320' if 'best' in calidad else '128'},
                    {'key': 'FFmpegThumbnailsConvertor','format': 'jpg'},
                    {'key': 'EmbedThumbnail'},
                    {'key': 'FFmpegMetadata','add_metadata': True}
                ]
            })
        else:
            ydl_opts.update({
                'format': f'bestvideo[height<={calidad}]+bestaudio/best/best',
                'merge_output_format': 'mp4',
                'postprocessors': [
                    {'key': 'FFmpegThumbnailsConvertor', 'format': 'jpg'},
                    {'key': 'EmbedThumbnail'},
                    {'key': 'FFmpegMetadata', 'add_metadata': True}
                ]
            })
            
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(urls)
            return f"Guardado en Descargas/GreenLoader/{sub_dir}"
        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == '__main__':
    api = Api()
    window = webview.create_window(
        'GreenLoader V7.0', 
        'index.html', 
        js_api=api, 
        width=700, 
        height=850, 
        resizable=False,
        background_color='#050505'
    )
    api.set_window(window)
    webview.start()