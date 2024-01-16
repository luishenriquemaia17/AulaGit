from pytube import YouTube

def download_video(url, output_path="."):
    try:
        # Cria um objeto YouTube
        yt = YouTube(url)

        # Seleciona a melhor qualidade disponível
        video = yt.streams.get_highest_resolution()

        # Baixa o vídeo para o diretório especificado
        video.download(output_path)

        print("Download concluído com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    # Insira o URL do vídeo do YouTube que você deseja baixar
    video_url = "https://www.youtube.com/watch?v=96G0ngElPWk"

    # Insira o caminho para o diretório onde deseja salvar o vídeo (opcional)
    output_directory = r"C:\Users\aulas\Desktop\AulaGit"

    download_video(video_url, output_directory)

