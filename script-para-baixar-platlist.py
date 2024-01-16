from pytube import Playlist, YouTube
import os

def on_progress(stream, chunk, bytes_remaining):
    # Calcula a porcentagem concluída e exibe
    percent = (1 - bytes_remaining / stream.filesize) * 100
    print(f"Baixando... {percent:.1f}% concluído", end='\r')

def download_video_or_playlist(url, output_path="."):
    try:
        # Verifica se o diretório existe e tenta criar se não existir
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        if 'playlist' in url:
            # Se o URL contiver 'playlist', assume que é uma playlist
            playlist = Playlist(url)
            for video_url in playlist.video_urls:
                download_single_video(video_url, output_path)
            print("\nDownload da playlist concluído com sucesso!")
        else:
            # Caso contrário, assume que é um único vídeo
            download_single_video(url, output_path)
            print("\nDownload do vídeo concluído com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def download_single_video(video_url, output_path="."):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    video = yt.streams.get_highest_resolution()
    video.download(output_path)

if __name__ == "__main__":
    # Insira o URL do vídeo ou da playlist do YouTube que você deseja baixar
    media_url = "https://www.youtube.com/watch?v=b_TcupRrXo4"
    # Ou para uma playlist:
    #media_url = "https://www.youtube.com/watch?v=URwAFE68gmU&list=PLv2e03XKuK2ktxBEdOYcw2GP6Mub16l8s"

    # Insira o caminho para o diretório onde deseja salvar o vídeo ou os vídeos da playlist (opcional)
    output_directory = r"C:\Users\aulas\Desktop\AulaGit\teste"

    download_video_or_playlist(media_url, output_directory)
