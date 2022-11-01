# Install the filestack-python package
from filestack import Client
import os

filepath="file.txt"

# Sign up at dev.filestack.com (I m using a free account)
# Copy the API KEY to an environment variable

client=Client(os.getenv("filestackapikey"))
newlink=client.upload(filepath=filepath)

# Print out the public url to the uploaded file
print(newlink.url)
