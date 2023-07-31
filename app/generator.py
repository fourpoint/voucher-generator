import jinja2
import pdfkit
import secrets
import string

wlan = "Residence A"

keys = set()

while len(keys) < 10:
    keys.add(''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(6)))

# Load the template
env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
template = env.get_template("voucher-template.html")

vouchers = "#Guest Name (Must),Remarks,Key (Empty implies random key)\n"

for key in keys:
    vouchers += f"Guest-{key},,{key}\n"
    # pass key and generate pdf
    html_out = template.render(guest_key=key, wlan_name=wlan)

    # write the pdf to file
    pdfkit.from_string(html_out, output_path=f"vouchers/voucher-{key}.pdf")

csv_file = open("vouchers/voucher.csv", "wt")
csv_file.write(vouchers)
csv_file.close()
