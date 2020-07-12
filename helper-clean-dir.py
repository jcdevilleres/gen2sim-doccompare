# First, here is the helper function to consolidate all your documents in a single directory (i.e., job duties) into one .txt file:
import os

# Initialize variables
directory = str(input("Enter directory for documents: ")) # Wait for input directory
document = ""
corpus = ""

# Utility functions
def doc_to_cor(document):
    fedit = open(directory.replace('/','') + ".cor", "a")
    fedit.write(document + '\n')

def clean_doc(filename):
    document = ""
    for line in open(directory + filename, "r"):
        line = line.lower().replace('\n','')
        document += line
    return document

# Iterate through directory
for filename in os.listdir(directory):
    # Iterate through the file
    if filename.endswith(".txt"):
        document = clean_doc(filename)
        doc_to_cor(document)
        print(os.path.join(directory, filename))
        continue
    else:
        continue
