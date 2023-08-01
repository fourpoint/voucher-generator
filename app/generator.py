import jinja2
import pdfkit
import secrets
import string
import sys
import os
import shutil


def generate(n_clients, wlan, directory):
    keys = set()

    while len(keys) < n_clients:
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
        pdfkit.from_string(html_out, output_path=f"{directory}/voucher-{key}.pdf")

    csv_file = open(f"{directory}/voucher.csv", "wt")
    csv_file.write(vouchers)
    csv_file.close()


def print_help():
    print("Usage: generator.py <wlan_name> <n_vouchers> <output_dir>")


def main():
    if len(sys.argv) < 3:
        print("Not enough arguments")
        print_help()
        exit()
    wlan = sys.argv[1]
    n = int(sys.argv[2])
    out_dir = sys.argv[3] if len(sys.argv) > 3 else "vouchers"
    if os.path.isdir(out_dir):
        if os.listdir(out_dir):
            print("Directory is not empty!")
            while True:
                res = input("Override? (N/y)") or "n"
                if res == "y":
                    print("Overriding...")
                    shutil.rmtree(out_dir)
                    os.mkdir(out_dir)
                    break
                elif res == "n":
                    print("Exiting")
                    exit()
                else:
                    print("Not a valid option!")
    else:
        os.mkdir(out_dir)

    generate(n_clients=n, wlan=wlan, directory=out_dir)


if __name__ == "__main__":
    main()
