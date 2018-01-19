from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['figure.figsize'] = (16.0, 9.0)

script = open("fightclub.txt").read()
stopwords = set(STOPWORDS)
tyler_durden = np.array(Image.open("fightclub.png"))

# Custom Colormap
from matplotlib.colors import LinearSegmentedColormap
colors = ["#000000", "#111111", "#101010", "#121212", "#212121", "#222222"]
cmap = LinearSegmentedColormap.from_list("mycmap", colors)

wc = WordCloud(background_color="white", stopwords=stopwords, mask=tyler_durden,
               width=1987, height=736, colormap=cmap)
wc.generate(script)
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
