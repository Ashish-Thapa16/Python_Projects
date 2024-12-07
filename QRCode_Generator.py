import qrcode

data = input("Enter the link you want to generate a QRcode for: ")

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill = "black", back_color = "white")

filename = input("Enter a filename to save the QR code (e.g., 'my_qr_code.png'): ")
img.save(filename)

img.show()