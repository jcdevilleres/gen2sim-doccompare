import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [12, 10] # Set out plot size

# Import required libraries, including gensim, matplotlib, and pandas
import pprint
import sys
from collections import defaultdict

import gensim
from gensim import corpora
from gensim import models
from gensim import similarities

import matplotlib.pyplot as plt
import pandas as pd

## Load text corpus

# Helper function to load text file containing duties / responsibilities 
# Note that each line is a separate document of job description
def open_cor(filename):
    text_corpus = []
    for line in open(filename, "r"):
        text_corpus.append(line)
    return text_corpus

filename ="duties.txt"
text_corpus = open_cor(filename)

# Create a set of frequent words, this will be removed from our processed text
stoplist = set('for a of the and to in & or be with by that'.split(' '))

# Lowercase each document, split it by white space and filter out stopwords
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in text_corpus]

# Count word frequencies
frequency = defaultdict(int) # Create defaultdict class with each word and their frequency
for text in texts: # Iterate through each text document from our texts corpus
    for token in text:
        frequency[token] += 1

# Only keep words that appear more than once
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
pprint.pprint(processed_corpus)

# Saved processed corpus into our corpora.Dictionary object this is our most important object
# it contains the tokens as well as their frequencies
dictionary = corpora.Dictionary(processed_corpus)
print(dictionary)

# The token2id attribute returns dictionary of our tokens and their ids 
pprint.pprint(dictionary.token2id) 

# The cfs attribute returns ow many instances of this token are contained in the documents.
dictionary.dfs

# Save output dictionary into text file for later use
dictionary.save_as_text("dict_text.txt")

## Comparison of new document with corpus

# We can convert our entire original corpus to a list of vectors:
bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
pprint.pprint(bow_corpus)

## Training our model

# train the model using our bag-of-words corpus from original corpus
tfidf = models.TfidfModel(bow_corpus)

# We are initializing our 'SparseMatrixSimilarity' which will be used to compute cosine similarity of document against corpus
# Note that 'num_features' must be updated to same size as dictionary or len(dictionary).
index = similarities.SparseMatrixSimilarity(tfidf[bow_corpus], num_features=len(dictionary)) 
# I spent quite some time troubleshooting this parameter and do not want you to waste your time as well!

# We can insert our job description details as new_doc. This is the document to compare with corpus
query_document = 'responsibilities    collecting and interpreting data    analyzing results    reporting the results back to the relevant members of the business    identifying patterns and trends in data sets    working alongside teams within the business or the management team to establish business needs    defining new data collection and analysis processes    controlling existing database    processing weekly and monthly reports of sm and websites accounts    developing records management processes and policies    identifying areas to increase efficiency and automation of processes    setting up and maintain automated data processes    identifying, evaluating and implementing external services and tools to support data validation and cleansing    producing and track key performance indicators    developing and support reporting processes    monitoring and auditing data quality    liaising with internal and external clients to fully understand data content    gathering, understanding and documenting detailed business requirements using appropriate tools and techniques    designing and carrying out surveys and analysing survey data    manipulating, analysing and interpreting complex data sets relating to the employers business    preparing reports for internal and external audiences using business analytics reporting tools    creating data dashboards, graphs and visualisations    providing sector and competitor benchmarking in market research    mining and analysing large datasets, drawing valid inferences and presenting them successfully to management using a reporting tool.    processing weekly and monthly reports of sm and websites accounts.'.split()

# Query our new document with our corpus and model to find how 'similar' it is to each of our documents in the corpus
query_bow = dictionary.doc2bow(query_document)
tfidf[query_bow]
sims = index[tfidf[query_bow]]

# Similarity values near '1' means it is very. The greater the values, mean more similarity.
print(list(enumerate(sims)))

# Same output but sorted according to score.
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(document_number, score)

## Visualization

# Load previous saved text file of our dictionary
data = pd.read_csv('dict_text.txt', sep="\t", header=None, skiprows = 1)
data.columns = ["token_id", "token_name", "token_frequency"]

data.head()

# Display tokens sorted according to frequency
data.sort_values(by='token_frequency', ascending=False)

# Plot tokens and their frequency
sorted_data = data.sort_values(by='token_frequency', ascending=True)
plt.barh(sorted_data.token_name, sorted_data.token_frequency)

# Plot tokens which appear more than once
filtered_data = sorted_data[sorted_data.token_frequency > 1]
plt.barh(filtered_data.token_name, filtered_data.token_frequency)
