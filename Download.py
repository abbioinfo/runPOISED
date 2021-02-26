import gdown
from zipfile import ZipFile

url = 'https://drive.google.com/uc?id=1OsnbZ9Or18PngdRKqQQ42WWEkZ5same9'
output = 'POISED.zip'
gdown.download(url, output, quiet=False)

# Create a ZipFile Object and load sample.zip in it
with ZipFile('POISED.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()

