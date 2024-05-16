import subprocess

def download_video(youtube_url, download_path):
    command = f'yt-dlp "{youtube_url}" -o "{download_path}"'
    subprocess.run(command, shell=True)

youtube_url = 'https://www.youtube.com/watch?v=6FFDUhpUizI'  
download_path = '../../Desktop/youtube-rips/%(title)s.%(ext)s' 
download_video(youtube_url, download_path)
