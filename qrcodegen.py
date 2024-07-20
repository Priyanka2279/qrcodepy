import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #15 means the version of the qr code high the number the biggger the code image and complicated picture
    box_size = 10, #size of the box where the qr code will be displayed
    border = 2 #it is the white part of image in all 4 sides with white color
)
data = "https://www.youtube.com/@-Priyanka02" 
# i have given the path for the linkedIn 
# if you dont want give the path then give the text

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", black_color="white")
img.save("test.png")

