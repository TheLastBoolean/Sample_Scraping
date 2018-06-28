import pyautogui
import time
import webbrowser
from bs4 import BeautifulSoup
import requests
import urllib.request




########## Go to Amazon site with ASIN ##########

ASIN = "B00ZK3KUE8"
genre = ""
url = "http://www.amazon.com/dp/" + ASIN
response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
soup = BeautifulSoup(response.content, "lxml")
soup_str = str(soup)





########## title = sliced page title. print with webbrowser request ##########

title = str(soup.title)

if "Amazon" in title[0:20]:
	title_end = title.find("Kindle")
	print (title[19:title_end - 2])
else:
	title_beginning = 7
	title_end = title.find("-")
	title = title[title_beginning:title_end - 1]



webbrowser.open("https://bookrunes.com/wp-admin/post-new.php")


time.sleep(2)
pyautogui.typewrite(title)





########## Download image from Amazon then upload to wordpress ##########

image_soup = soup.find("img", class_="a-dynamic-image frontImage")
image_soup_str = str(image_soup)
first_http = image_soup_str.find('"https')
image_start = image_soup_str.find('"https', first_http + 1)
image_end = image_soup_str.find('"', image_start + 1)
image_src = image_soup_str[image_start + 1 : image_end]
urllib.request.urlretrieve(image_src, "image.jpg")



for i in range(30):
	pyautogui.press("tab")

pyautogui.press("return")

for i in range(2):
	pyautogui.press("tab")

pyautogui.press("return")

for i in range(2):
	pyautogui.press("tab")

pyautogui.press("return")

time.sleep(1)

pyautogui.press("down")

pyautogui.press("return")

time.sleep(2)

for i in range(8):
	pyautogui.press("tab")

pyautogui.press("return")



########## Get author name + Upload all other links ##########


time.sleep(2)

for i in range(4):
	pyautogui.press("tab")

start_index = soup_str.find("Kindle edition by")
end_index = soup_str.find("Download", start_index)
author_name = (soup_str[start_index + 17 : end_index - 2])


pyautogui.typewrite(author_name)
pyautogui.press("tab")
pyautogui.press("$")
pyautogui.typewrite("2.99")
pyautogui.press("tab")
pyautogui.typewrite("https://www.amazon.com/dp/" + ASIN)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.typewrite("https://www.amazon.uk.co/dp/" + ASIN)
pyautogui.press("tab")
pyautogui.typewrite("https://www.amazon.com.au/dp/" + ASIN)
pyautogui.press("tab")
pyautogui.typewrite("https://www.amazon.in/dp/" + ASIN)
pyautogui.press("tab")
pyautogui.typewrite("https://www.amazon.ca/dp/" + ASIN)





