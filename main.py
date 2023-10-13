import requests
from bs4 import BeautifulSoup

URL = "https://hacktoberfest.com/participation/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

tree_variations = ["tree", "trees", "TREE", "Tree", "TREES", "Trees"]
tshirt_variations = ["t-shirt", "t-shirts", "T-shirt", "T-shirts", "T-Shirt", "T-Shirts", "T-SHIRT", "T-SHIRTS"]

tree_count = 0
tshirt_count = 0

for word in tree_variations:
    for element in soup.find_all(string=lambda string: string and word in string):
        tree_count += 1

for word in tshirt_variations:
    for element in soup.find_all(string=lambda string: string and word in string):
        tshirt_count += 1

print("Counted Trees:", tree_count)
print("Counted T-Shirts:", tshirt_count)

if tree_count > tshirt_count:
    print("Trees Win!")
elif tree_count == tshirt_count:
    print("It's a tie!")
else:
    print("T-Shirts Win!")
