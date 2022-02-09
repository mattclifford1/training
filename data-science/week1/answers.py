from bs4 import BeautifulSoup
import requests

# %% md
# # Task 1

# %%
# get webpage source code
url = 'https://www.theguardian.com/books/2022/jan/24/the-big-idea-should-animals-have-the-same-rights-as-humans'
source = requests.get(url)
soup = BeautifulSoup(source.text, "html.parser")
# get href links
links = soup.find_all('a', attrs={
    'data-link-name':'in body link'
})
hrefs = []
for link in links:
    hrefs.append(link['href'])

print('number of links: ', len(hrefs))

# %% md
# # Task 2

# %%
# no longer works as webspage source has changed
links = soup.find_all('a', attrs={
    'class':'submeta__link'
})


# %%% TASK 3
url = 'https://www.theguardian.com/uk/technology'
req = requests.get(url)
source = req.text
soup = BeautifulSoup(source, 'html.parser')
tech = soup.find_all('section', attrs={
    'id': 'technology'
})

articles = tech[0].find_all('a', attrs={
    'class': 'js-headline-text'
})

for article in articles:
    print(article['href'][:], article.text[:20])

# %% md
# # Task 4

# %%
def get_soup(url):
    req = requests.get(url)
    source = req.text
    return BeautifulSoup(source, 'html.parser')

num_to_get = 50
finished = False
stories = []
page = 1
while not finished:
    url = 'https://www.theguardian.com/technology?page='+str(page)
    soup = get_soup(url)
    tech_page = soup.find_all('a', attrs={
        'data-link-name': 'article'
    })
    for link in tech_page:
        if link['href'] not in stories:
            stories.append(link['href'])
        if len(stories) == num_to_get:
            finished = True
            break
    page += 1
print(len(stories))
print(stories[1])
