# Main library import
import qrcode

# Read URL input from the user
url = input("Enter the URL: ").strip()

# Path where the QR image will be saved
file_path = "D:\\Pictures\\QR-Codes\\qrcode.png"

# Create a QRCode object
qr = qrcode.QRCode()

# Add data (URL) to the QR code
qr.add_data(url)

# Generate the QR Code image
img  = qr.make_image()

# Save the image to the given file path
img.save(file_path)

# Display success message
print("QR Code was generated successfully")
