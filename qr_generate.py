
# Install the qrcode library
# pip install qrcode[pil]

import qrcode

#personal data

data = {
    "Name": "Purna Bahadur Khatri",
    "Address": "Kathmandu, Nepal",
    "Phone": "9829845767",
    "Email": "purnakhatri630@gmail.com",
    "Website": "https://www.purnabahadurkhatri.name.np"
}

#create a qr code

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    error_correction= qrcode.constants.ERROR_CORRECT_L,
    border=5
)

# Add data to the qr code
qr.add_data(data)
qr.make(fit=True)

#Save the image
img = qr.make_image(fill_color="black", back_color="white").save("site.png")
print("QR code generated successfully")
