This open source project is a an example of how to scan barcodes using a smartphone and present data from your system using Python and the flask framework.

How it works:

A user scans a barcode using their smartphone
Orca Scan sends a HTTP GET request to your endpoint with ?barcode=value
Your system queries a database or internal API for a barcode match
Your system returns the data in JSON format with keys matching column names
The Orca Scan mobile app presents that data to the user
If the mobile user has update permission and saves the data, it will saved to your Orca sheet.
