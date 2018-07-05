import requests
import datetime
from datetime import datetime, timedelta
import pathlib
import html
import math


def urls_and_titles(response, urls, titles):
	for i in range (0, len (response['articles'])):
	    urls.append(response['articles'][i]['url'])


	for i in range (0, len (response['articles'])):
	    titles.append(response['articles'][i]['title'])

print("Hi welcome to edNews- news all about Ed!")
print("Please enter your start date in this format: MM/DD/YYYY eg. 07/04/2018")
month, date, year = input().split('/')
full_date = str(year)+str(month)+str(date)
date_1 = datetime(year=int(full_date[0:4]), month=int(full_date[4:6]), day=int(full_date[6:8]))
date_1_iso = str(date_1.isoformat())[0:10]
print("How many days from " + date_1_iso + "?")
date_2 = date_1
date_2 += timedelta(days=int(input()))
print("Assuming endate: " + date_2.isoformat())
date_2_iso = str(date_2.isoformat())[0:10]

pathlib.Path('./'+date_1_iso + "_to_" +date_2_iso).mkdir(exist_ok=True) 

url = ('https://newsapi.org/v2/everything?'
       'q=Ed Markey&'
       'from=' +
       date_1_iso +
       'T13:00:30&'
       'to=' +
       date_2_iso +
       'T13:00:30&'
       'sortBy=popularity&'
       'apiKey=c206322b11c04e0c9a399dfba44f6a57')

response = requests.get(url).json()

numresponses = response['totalResults']
pages = math.ceil(numresponses / 20)

urls=[];
titles=[];


## PAGE 0
url = ('https://newsapi.org/v2/everything?'
       'q=Ed Markey&'
       'from=' +
       date_1_iso +
       'T13:00:30&'
       'to=' +
       date_2_iso +
       'T13:00:30&'
       'sortBy=popularity&'
       "apiKey=c206322b11c04e0c9a399dfba44f6a57")

response = requests.get(url).json()
urls_and_titles(response, urls, titles)


## PAGE 1+
if (pages > 0):
	for p in range(0, pages):
		try:
			url = ('https://newsapi.org/v2/everything?'
			       'q=Ed Markey&'
			       'from=' +
			       date_1_iso +
			       'T13:00:30&'
			       'to=' +
			       date_2_iso +
			       'T13:00:30&'
			       'sortBy=popularity&'
			       "apiKey=c206322b11c04e0c9a399dfba44f6a57&"
			       "page="+ str(p+1))
			print(url)

			response = requests.get(url).json()

			urls_and_titles(response, urls, titles)
		except:
			print("API overloaded :( not all articles shown")
			pass

## GENERATING ARTICLES

notparsed = []

from newspaper import fulltext

print("Number of articles: " + str(len(urls)))

for i in range(0, len(urls)):
	try :
		print(str(i)+ ":" + urls[i])
		html = requests.get(urls[i]).text
		text = fulltext(html)
		f= open(date_1_iso + "_to_" + date_2_iso + "/" + titles[i] + ".txt","w+")
		f.write(text)
		f.close()
	except:
		print("^not parsed")
		notparsed.append(i);
		pass

## FINAL FILE

final= open(date_1_iso + "_to_" + date_2_iso + "/FINAL.txt","w+")

for i in range(0, len(urls)):
	try:
		final.write("ARTICLE:" + titles[i])
		html = requests.get(urls[i]).text
		text = fulltext(html)
		final.write(text)
	except:
		pass

final.close()


## WEBSITE
website = open(date_1_iso + "_to_" + date_2_iso + "/LINKS.html","w+")
website.write("<!DOCTYPE html>"+"\n"+ 
		 "<html>"+"\n"+ 
		 "<head>"+"\n"+ 
		 "<title>edNews</title>"+"\n"+ 
		 "</head> "+"\n"+ 
		 "<body>"+"\n"+ 
		 "<h1> edNews! </h1>" +

		 "<h2>" +
		 date_1_iso + "_to_" + date_2_iso + "</h2>" + "\n")

written = []
for i in range(0, len(urls)):
	if (titles[i] not in written):
		if (i in notparsed):
			website.write("not parsed:" + "<br>")
		import html
		escaped_title = html.escape(titles[i], quote = True)
		website.write("<a href=\"" + urls[i] + "\">" + escaped_title + "</a>" + "<br>" + "<br>" +"\n")
		written.append(titles[i]) 

website.write("</body>" + "\n" + "</html>")
