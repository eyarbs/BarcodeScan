Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.request
>>> import json
>>> import pprint
>>> api_key = "jtlabesf3t0qxsinhka36kr9tpznke"
>>> url = "https://api.barcodelookup.com/v2/products?barcode=077341125112&formatted=y&key=jtlabesf3t0qxsinhka36kr9tpznke"
>>> with urllib.request.urlopen(url) as url:
	    data = json.loads(url.read().decode())

>>> barcode = data["products"][0]["barcode_number"]
print ("Barcode Number: ", barcode, "\n")
>>> name = data["products"][0]["product_name"]
 print ("Product Name: ", name, "\n")
 
>>> description = data["products"][0]["description"]
print ("description: ", description, "\n")
>>> manufacturer = data["products"][0]["manufacturer"]
print ("manufacturer: ", manufacturer, "\n")
>>> brand = data["products"][0]["brand"]
print ("brand: ", brand, "\n")
>>> print ("Entire Response:")
pprint.pprint(data)
Entire Response:
>>> 