import requests
image = requests.get('https://cataas.com/cat')
with open('new_image.gif', 'wb') as f:
       f.write(image.content)