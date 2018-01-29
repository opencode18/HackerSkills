from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

matplotlib.rcParams['figure.figsize'] = (16.0, 9.0)
mask = np.array(Image.open("fma.jpg"))
script = open("fma.txt").read()
stopwords = set(STOPWORDS)
wc = WordCloud(background_color="white", stopwords=stopwords, width=1600, height=900, mask=mask)
wc.generate(script)
image_colors = ImageColorGenerator(mask)

plt.figure()
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.savefig("wordcloud")
plt.show()

