import urllib.request

def main():
	req = urllib.request.urlopen("https://rpic.douyucdn.cn/live-cover/appCovers/2019/03/25/6271667_20190325085629_small.jpg")
	img_content = req.read()
	with open("/home/fanwan666/Desktop/1.jpg", "wb") as f:
		f.write(img_content)

if __name__ == "__main__":
	main()
