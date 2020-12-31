import pytube

print("""
╭━━━╮╱╱╱╭╮╱╱╱╭╮╱╱╱╱╭━╮╭━┳━━━╮
┃╭━╮┃╱╱╭╯╰╮╱╱┃┃╱╱╱╱╰╮╰╯╭┻╮╭╮┃
┃╰━╯┣╮╱┣╮╭╋╮╭┫╰━┳━━╮╰╮╭╯╱┃┃┃┃
┃╭━━┫┃╱┃┃┃┃┃┃┃╭╮┃┃━┫╭╯╰╮╱┃┃┃┃
┃┃╱╱┃╰━╯┃╰┫╰╯┃╰╯┃┃━╋╯╭╮╰┳╯╰╯┃
╰╯╱╱╰━╮╭┻━┻━━┻━━┻━━┻━╯╰━┻━━━╯
╱╱╱╱╭━╯┃
╱╱╱╱╰━━╯""")

video_url = input("inserte una URL:")

youtube = pytube.YouTube(video_url)

video = youtube.streams.first()

video.download()