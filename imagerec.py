#Saisha kapoor
#Period 3

#Start by importing the necessary libraries
import random
from PIL import Image
import requests
from io import BytesIO


icecreamList = ["https://tinyurl.com/2s4k5m92",   #cookie dough ice cream
"https://tinyurl.com/2p9ww97e",     #vanilla ice cream
"https://tinyurl.com/2w66ty3b",     #chocolate ice cream
"https://tinyurl.com/644a2wb8",     #Strawberry ice cream
"https://tinyurl.com/5n7yafce"      #Pistacio ice cream
]

#Functions
#Define a function called open_image with a url parameter for the image address
def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


#Call your function with an image URL

#DO NOT FORGET TO CITE YOUR SOURCE
#Some amazing looking ice cream sundae! Image source: The Dog API. 2009. Accessed via https://cdn2.thedogapi.com/images/0LJiOVlxp.jpg CC BY-NC 2.0

#Main

#Intro
while True:
    print("Welcome to the ice cream recommender app!")
    ans = input("Would you like a recommendation?")
    if ans == "yes":
        image = random.choice(icecreamList)
        if image == "https://tinyurl.com/2s4k5m92":
            open_image(image)
            print("I recommend this delicious cookie dough ice cream! It is very yummy!")
        elif image == "https://tinyurl.com/2p9ww97e":
            open_image(image)
            print("I recommed this classic vanilla ice cream! It is so sweet!")
        elif image == "https://tinyurl.com/2w66ty3b":
            open_image(image)
            print("I recommend this rich, creamy chocolate ice cream! It is so amazing!")
        elif image == "https://tinyurl.com/644a2wb8":
            open_image(image)
            print("I recommend this fresh strawberry ice cream! It is so refreshing!")
        else:
            open_image(image)
            print("I recommend this nutty pistacio ice cream! It is so creamy!")
    else:
        print("Thank you for playing!")
        break
