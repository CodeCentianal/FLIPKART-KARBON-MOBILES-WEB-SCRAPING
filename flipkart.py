import requests
from pprint import pprint
from bs4 import BeautifulSoup
#flipkart scaping

import json
import time
list_flipkart = []

for i in range(1,6):
	url = "https://www.flipkart.com/search?q=karbonn+mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&page="+str(i)
	time.sleep(1)
	response = requests.get(url)
	soup = BeautifulSoup(response.text,"html.parser")
	mobiles_name = soup.find_all("div",class_="_3wU53n")
	mobiles_cost = soup.find_all("div",class_="_1vC4OE _2rQ-NK")
	mobile_img = soup.find_all("div",class_="_3BTv9X")
	mobiles_ram_rom = soup.find_all("ul",class_="vFw0gD")

	for j in range(len(mobiles_name)):
		dict_for_each_mobile = {}
		li = mobiles_ram_rom[j].find_all("li",class_="tVe95H")
		img_link = mobile_img[j].find("img")
		dict_for_each_mobile["mobile_name"]=mobiles_name[j].text
		dict_for_each_mobile["mobile_cost"]=mobiles_cost[j].text
		dict_for_each_mobile["ram_rom"]=li[0].text
		dict_for_each_mobile["camera_quality"] = li[2].text
		dict_for_each_mobile["mobile_image"]=img_link["src"][2:]
		list_flipkart.append(dict_for_each_mobile)

flipkart_json = open("flipkart.json","w+")
json.dump(list_flipkart,flipkart_json,indent=2)

	
