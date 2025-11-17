import qrcode

url = input("Enter the URL: ").strip()
file_path = "D:\\Pictures\\QR-Codes\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)
