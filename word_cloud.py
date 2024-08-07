import matplotlib.pyplot as plt
from wordcloud import WordCloud
from words import all_words


# Convert list of words to a single string
text = ' '.join(all_words)

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()