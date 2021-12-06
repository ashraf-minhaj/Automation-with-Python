""" extract emotion from text 

author: ashraf minhaj
mail  : ashraf_minhaj@yahoo.com
"""

""" install -
$ pip install nltk      # textblob depends on nltk
$ pip install textblob
"""

import textblob

text = 'Woul you like to come over my place?'

# convert into textblob object
blob_text = textblob.TextBlob(text)
print(blob_text)

# finally get seniment from -1 to 1
# -1 being most negative and +1 most positive
sentiment = blob_text.sentiment.polarity
print(sentiment)