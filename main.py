import requests
from bs4 import BeautifulSoup

URL = "https://hacktoberfest.com/participation/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
treeCount = 0
tShirtCount = 0
for element in soup.find_all(string=lambda string: string and "tree" in string):
    treeCount += 1
    #print(element.get_text())
for element in soup.find_all(string=lambda string: string and "trees" in string):
    treeCount += 1    
for element in soup.find_all(string=lambda string: string and "TREE" in string):
    treeCount += 1
for element in soup.find_all(string=lambda string: string and "Tree" in string):
    treeCount += 1
for element in soup.find_all(string=lambda string: string and "TREES" in string):
    treeCount += 1
for element in soup.find_all(string=lambda string: string and "Trees" in string):
    treeCount += 1

for element in soup.find_all(string=lambda string: string and "t-shirt" in string):
    tShirtCount += 1
for element in soup.find_all(string=lambda string: string and "t-shirts" in string):
    tShirtCount += 1
for element in soup.find_all(string=lambda string: string and "T-shirt" in string):
    tShirtCount += 1
for element in soup.find_all(string=lambda string: string and "T-shirts" in string):
    tShirtCount += 1
for element in soup.find_all(string=lambda string: string and "T-Shirt" in string):
    tShirtCount += 1
for element in soup.find_all(string=lambda string: string and "T-Shirts" in string):
    tShirtCount += 1
for element in soup.find_all(string=lambda string: string and "T-SHIRT" in string):
    tShirtCount += 1
for element in soup.find_all(string=lambda string: string and "T-SHIRTS" in string):
    tShirtCount += 1

print("Counted Trees" , treeCount)
print("Counted T Shirts" , tShirtCount)

if (treeCount > tShirtCount):
    print("Trees Win!")
if (treeCount == tShirtCount):
    print("It's a tie!")
else:
    print("T Shirts Win!")