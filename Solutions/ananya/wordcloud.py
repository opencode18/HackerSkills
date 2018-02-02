from wordcloud import WordCloud, STOPWORDS
import matplotlib
import matplotlib.pyplot as plt

% matplotlib inline
matplotlib.rcParams['figure.figsize'] = (16.0, 9.0)

# Reading the script
script = open("iiit.txt").read()
# Set of Stop words
stopwords = set(STOPWORDS)
stopwords.add("will")
# Create WordCloud Object
wc = WordCloud(background_color="white", stopwords=stopwords, 
               width=1600, height=900, colormap=matplotlib.cm.inferno)
# Generate WordCloud
wc.generate(script)
# Show the WordCloud
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
