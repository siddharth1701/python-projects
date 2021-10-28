try:
    import requests
    from bs4 import BeautifulSoup
    import csv
except ImportError:
    print("No module named 'requests or BeautifulSoup' found")


# parsing the HTML content from webpage without beautification of HTML code
# URL = "https://www.geeksforgeeks.org/data-structures/"
# r = requests.get(URL)
# print(r.content)

# Step 3: Parsing the HTML content with beautification of HTML code
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
# soup = BeautifulSoup(r.content)
# print(soup.prettify())

# Step 4: Searching and navigating through the parse tree

quotes=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'id':'all_quotes'}) 
   
for row in table.findAll('div',
                         attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)
   
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)