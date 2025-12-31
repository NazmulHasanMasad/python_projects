#.strip() :Removes leading and trailing whitespace from a string:
#Why it’s used here: If the user accidentally adds spaces at the beginning or end, they won’t affect the QR data.
#Returns: A new cleaned string (strings are immutable; it does not modify in place)




import qrcode 

data=input('Enter the text or url:/').strip()
filename=input('Enter the file name:').strip()
qr=qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
image=qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'Qrcode saved as : {filename}')
