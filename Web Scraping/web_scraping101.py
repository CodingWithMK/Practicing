from bs4 import BeautifulSoup

# with open("index.html", 'r') as file:
#     soup = BeautifulSoup(file, 'html.parser')
    
# # Print out everything    
# print(soup.prettify())

# # Printing out title tag
# tag = soup.title
# print(tag)

# # Printing out title text
# print(tag.string)


# # Modifing text in any tag
# # tag.string = "New title"
# # print(tag)

# # Accessing the first of any tag
# a_tag = soup.find('a')
# p_tag = soup.find('p')
# h1_tag = soup.find('H1')
# h2_tag = soup.find('H2')

# print(a_tag)
# print(p_tag)
# print(h1_tag)
# print(h2_tag)

# # Accessing all of any tag
# a_tags = soup.find_all('a')
# p_tags = soup.find_all('p')
# h1_tags = soup.find_all('H1')
# h2_tags = soup.find_all('H2')

# print(a_tags)
# print(p_tags)
# print(h1_tags)
# print(h2_tags)

# # Accessing the nested tag şn first 'p' tag
# p_tag = soup.find_all('p')[0]
# print(p_tag.find_all('b'))


# Accessing a specific value on a website
import requests
url = "https://www.newegg.ca/msi-geforce-rtx-3060-rtx-3060-ventus-2x-12g-oc/p/N82E16814137632"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

price = soup.find_all(string="$")
parent_tag = price[0].parent
# print(parent_tag)
strong_tag = parent_tag.find("strong")
print(f"{strong_tag.string}€")