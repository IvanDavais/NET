import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def download_img(img_url, img_name):
	req = urllib.request.urlopen(img_url)
	url_content = req.read()
	with open(img_name, "wb") as f:
		f.write(url_content)

def main():
	gevent.joinall([
		gevent.spawn(download_img, "https://rpic.douyucdn.cn/live-cover/roomCover/2019/04/13/ed08ab4599e130f5938525934a7308a6_big.jpg","/home/fanwan666/Desktop/4.JPEG"),
		gevent.spawn(download_img, "https://rpic.douyucdn.cn/live-cover/roomCover/2019/04/13/ed08ab4599e130f5938525934a7308a6_big.jpg","/home/fanwan666/Desktop/5.JPEG"),
])

if __name__ == "__main__":
	main()
