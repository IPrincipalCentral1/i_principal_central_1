














import os


os.system("pip install requests")



import requests



url = "https://github.com/IPrincipalCentral/i_principal_central/archive/refs/heads/main.zip"

resp = requests.head(url, allow_redirects=True)

size = resp.headers.get("Content-Length")

if size:

    print(f"File size: {int(size):,} bytes ({int(size)/1e6:.2f} MB)")

else:

    print("❗ لا يوجد Content-Length (ربما يستخدم chunked transfer encoding).")
















