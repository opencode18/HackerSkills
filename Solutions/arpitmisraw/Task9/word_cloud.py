import wikipedia
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np




def wiki(query):
    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)
    return page.content


def word_cloud(text):
    mask = np.array(Image.open('dc.jpg'))
    stop_words = set(STOPWORDS)
    wc = WordCloud(background_color = 'white', mask = mask, max_words = 200, stopwords = stop_words)
    wc.generate(text)
    wc.to_file('wc.png')


word_cloud(wiki('Dunkirk (2017 film)'))




