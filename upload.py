from instapy_cli import client
import os
import subprocess
import schedule
import time

password = os.environ['INSTAPASSWORD']
username = 'Username goes here'
cookie_file = 'To store and reuse cookie' # username_ig.json
# Get most recently modified image
image = subprocess.check_output('ls -t /path/of/directory/to/track', shell=True)
image = image.decode('utf-8').split("\n")[0] # Convert bytes to string 

# Prepend path to the image
path = '/path/of/directory/to/track'
image = path+image

# Set caption
text = 'Python is awesome!'

def post():
    with client(username, password,cookie_file=cookie_file, write_cookie_file=True) as cli:
        # cookies = cli.get_cookie()
        print(image,text)
        cli.upload(image,text)

schedule.every().day.at("01:40").do(post)

while True:
    schedule.run_pending()
    time.sleep(1)