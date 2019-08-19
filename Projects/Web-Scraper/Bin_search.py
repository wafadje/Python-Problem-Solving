from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def start_search():

	search = input("Enter search term : ")
	params = {"q":search}
	dir_name = search.replace(" ", "_").lower()

	if not os.path.isdir(dir_name):
		os.makedirs(dir_name)

	r = requests.get("https://www.bing.com/search", params=params)
	m = requests.get("https://www.bing.com/images/search", params=params)

	soup = BeautifulSoup(r.text, "html5lib")
	soup_image = BeautifulSoup(m.text, "html5lib")
	results = soup.find("ol", {"id":"b_results"}) 
	links = results.findAll("li", {"class":"b_algo"})


	for item in links:
		item_text = item.find("a").text
		item_href = item.find("a").attrs["href"]


		if item_href and item_text:
			print(item_text)
			#print(item_href)
			#print("Summary :", item.find("a").parent.parent.find("p").text)

	img_links = soup_image.findAll("a", {"class":"thumb"})
	for image in img_links:
		try:
			img_obg = requests.get(image.attrs["href"])
			print("Getting", image.attrs["href"])
			title = image.attrs["href"].split("/")[-1]
			try:
				img = Image.open(BytesIO(img_obg.content))
				img.save("./"+ dir_name +"/"+ title, img.format)
			except:
				print("Counld not save image.")
		except:
			print("Counld not request image")

	start_search()

start_search()
