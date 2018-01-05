from PIL import Image

from InstagramAPI import InstagramAPI
user,pwd = 'the_fourth_sangam', '@wes0meme-insta'

InstagramAPI = InstagramAPI(user,pwd)
InstagramAPI.login() # login

im = Image.open('custom2.png')
im.save('poem1.jpg')

photo_path ='poem1.jpg'
caption    = """

Haiku by Kobayashi Issa 

Dew evaporates
And all our world 
is dew
So dear,
So fresh, 
So fleeting

Kobayashi Issa (1763–1828) was a Japanese poet and lay Buddhist priest known for his haiku poems and journals. He is better known as simply Issa, a pen name meaning Cup-of-tea. He is regarded as one of the four haiku masters in Japan, along with Basho, Buson and Shiki.

He lost two children at a young age, and many of his poems reflect the sorrow and fleeting nature of our existence.

#Kobayashi #Issa #haiku #japan #poetry #poetsofinstagram #poem #instapic #love #instagood #photooftheday #beautiful #art #instadaily #life #amazing #instamood #instagram #motivation

Photo by @ShyamValsan"""

InstagramAPI.uploadPhoto(photo_path, caption = caption)
print InstagramAPI.LastResponse.text
InstagramAPI.logout() # logout

