from PIL import Image,ImageDraw,ImageFile
import os

def encrytpion(message):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    Alpha_dir = {chr(i):i*5 for i in range(32,127)}
    a = Image.new('RGB',(127*5,len(message)),'White')
    draw = ImageDraw.Draw(a)
    for y in range(len(message)):
        for x in range(Alpha_dir[message[y]]):
            draw.point((x,y), fill=(0,0,0))
    a.save('message.png',quality = 100)
    f = open('message.png','rb')
    a = f.read()
    f.close()
    os.remove('message.png')
    return a 

def decryption(image):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    f = open('enmessage.png','wb')
    f.write(image)
    f.close()
    Alpha_dir = {i*5:chr(i) for i in range(32,127)}
    im = Image.open('enmessage.png')
    a = im.size
    pix = im.load()
    c = []
    d = []
    for y in range(a[1]):
        count =0
        for x in range(a[0]):
            if pix[x,y][0] == 0:
                count +=1
        c.append(count)
    for i in c:
        d.append(Alpha_dir[i])
    e = ''.join(d)
    os.remove('enmessage.png')
    return e




