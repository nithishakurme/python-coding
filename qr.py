import qrcode
qr=qrcode.QRCode()
a="TVK is rocking"
qr.add_data(a)
qr.make(Fit=True)
res=qr.make_image(fill_colour="black",black_colour="white")
res.save("nithisha.png")
print("created nithisha")
