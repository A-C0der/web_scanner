import requests


def detail(url):
	det=requests.get(url).headers
	print("\n\t\t\t#### HEADER DETAILS #####")
	for info in det:
		print(info,":\t\t\t",det[info])
		
		

