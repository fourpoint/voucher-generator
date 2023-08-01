# Ruckus SmartZone Guest Pass generator

Basic script for generating Guest Pass vouchers for residents.

## Requirements

- Python3
- Jinja2
- pdfkit

Pdfkit needs wkhtmltopdf to function. Installation instructions are here https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf.

## Usage

Download project using Git or zip file and enter app directory.

Install required packages.
```
pip3 install -r requirements.txt
```
Generate vouchers
```
python generator.py wlan_name n_vouchers [output_dir]
```
wlan_name - Name of hotspot Wi-Fi network.  
n_vouchers - Number of vouchers to generate.  
output_dir - Optional output folder where the vouchers will be created.  
