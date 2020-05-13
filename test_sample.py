import encryption_decryption

f = open('test.txt','w')
f.write('this data sample is used for testing a new encryption algorithm called the bar code encryption algorithm in which a give letter is encrypted into a bar of a specific number of block dots or pixels thanks')
f.close()
f = open('test.txt','r')
lines = ''.join(f.readlines())
f.close()
print(lines)
encryption_decryption.encrytpion(lines)
b = encryption_decryption.encrytpion(lines)
print(b)
print(len(b))

























# import os
# os.remove('enmessage.png')








# from PIL import Image,ImageDraw
# import random




# # Alpha_dir = {chr(ord('a')+i):i for i in range(26) }

# Alpha_dir = {chr(i):'' for i in range(32,127)}
# b = input('Enter a message = ')

# a = Image.new('RGB',(60,len(b)),'White')
# draw = ImageDraw.Draw(a)

# for y in range(len(b)):
#     for x in range(Alpha_dir[b[y]]):
#         draw.point((x,y), fill=(0,0,0))

# a.show()
# a.save('message.png',quality = 100)