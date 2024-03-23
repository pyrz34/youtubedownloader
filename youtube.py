import pytube

url = input("enter url of video :")

path = ""

pytube.YouTube(url).streams.get_highest_resolution().download(path)
