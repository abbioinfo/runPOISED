import gdown
from zipfile import ZipFile

url = 'https://drive.google.com/uc?id=1kbs5z1DLpo6o_LqZlrwcwtK6XSGYKtXI'
output = 'POISED_live.zip'
gdown.download(url, output, quiet=False)

# Create a ZipFile Object and load sample.zip in it
with ZipFile('POISED_live.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()




url = 'https://drive.google.com/uc?id=1_JpvX4slqiHU0kDXbd4tO6RtFaCWrXQS'
output = 'POISED_label.zip'
gdown.download(url, output, quiet=False)

# Create a ZipFile Object and load sample.zip in it
with ZipFile('POISED_label.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()



url = 'https://drive.google.com/uc?id=1EK2IPc2U6NKyotZJDU2493SD3cIAgKtw'
output = 'POISED_handgated.zip'
gdown.download(url, output, quiet=False)

# Create a ZipFile Object and load sample.zip in it
with ZipFile('POISED_handgated.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()


