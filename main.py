import json
import cognitive_face as CF
import sys
from PIL import Image, ImageDraw, ImageFont

#import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
#from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw

SUBSCRIPTION_KEY = os.environ['COGNITIVE_SERVICE_KEY']
BASE_URL = os.environ['FACE_ENDPOINT']

def detect_face(foto):
    data = open(foto, 'rb')
    headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY} #Funciona porque tiene el content  type
    params = {
        'returnFaceAttributes': 'age,gender',
    }
    face_api_url = BASE_URL+'detect'
    response = requests.post(face_api_url, params=params,
                            headers=headers, data=data)
    json_detected = response.json()
    print(json_detected)
    
    image = Image.open(foto)
    draw = ImageDraw.Draw(image)
    for js in json_detected:
        faceRectangle = js['faceRectangle']
        faceAttributes = js['faceAttributes']
        width = faceRectangle['width']
        top = faceRectangle['top']
        height = faceRectangle['height']
        left = faceRectangle['left']

        draw.rectangle((left,top,left + width,top+height), outline='red')
        
        font = ImageFont.truetype('Roboto-Regular.ttf', 15)
        draw.text((left,top -20,left + width,top+height),faceAttributes['gender']+","+str(faceAttributes['age']), font=font,  fill="white")
        

    image.show()
    

      
detect_face('people.jpg')