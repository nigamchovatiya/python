# -------------------------------

from bs4 import BeautifulSoup

# -------------------------------

html = """
<title>Tutorial</title>

<div id="main">
  <p class="first">First paragraph.</p>
  <p id="second">Second paragraph.</p>
  <a href="https://google.com" class="link">Google</a>
  <a href="https://example.com">Example</a>
</div>

<p class="first second">First paragraph.</p>

"""


soup = BeautifulSoup(html, "html.parser")

# select()
links = soup.select('a')
for link in links:
    print(link) # return list

# select_one()
links = soup.select_one('a')
for link in links:
    print(link) # return first match 

# select by tag
print("\n----paragraph-----")
paragraphs = soup.select('p')
for paragraph in paragraphs:
    print(paragraph)

# select by class
print("\n----class select----")
selects = soup.select('p.first')
for select in selects:
    print(select)

# select by id
print("\n----id select----")
selects = soup.select('p#second')
for select in selects:
    print(select)

# select by attribute
print("\n----attribut select----")
selects = soup.select('a[href]')
for select in selects:
    print(select)    

# nested selection
print("\n----nested select----")
selects = soup.select('div p')
for select in selects:
    print(select)


# multiple child
print("\n----mulitple classes select----")
selects = soup.select('p.first.second')
for select in selects:
    print(select)       
    

# multiple child
print("\n----direct child select----")
selects = soup.select('div > p')
for select in selects:
    print(select)       


# extract attribute
print("\n----extract attribute-----")
links = soup.select('a.link')
for link in links:
    print(link.get('href')) # link
    print(link.get('class')) # name
    print(link.get('id')) # none bcz no id set

    