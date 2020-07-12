# gen2sim-doccompare
Brief demo on optimizing your resume for job recruitment platform, based on keywords and similarity.

# Introduction
As a mid-level engineer transitioning to a data analyst role it can be sometimes tricky to update your profile properly. You are bogged down with questions such as which keywords do I use? and which skills or duties do I highlight? It is no secret that the use of recruitment platforms or applicant tracking systems (ATS) are prolific and having the right profile for the role can help applicants immensely. Here is a brief and intuitive scripts in order to solve this problem.

![Input / Process / Output](https://miro.medium.com/max/656/1*Ymgn-pZJJ978a2Vu0cuifQ.png)

# Input
The input data is quite simple to gather and format. First, you can scour the desired jobs and their requirements, from multiple sites like LinkedIn.com, Indeed.com, Monster.com, this consists of duties and skills required. Afterwards, format them as plain text and save each of them into a directory. This is all you need for your input data.

# Process
Next, using the python gensim library, which allows you to use sophisticated algorithms intuitively and easily, we will be able to covert those input documents into a corpus (a collection of documents), train our model with it, and compare it with own document (your job profile).

# Output
The output metrics are straightforward. First, you will know how similar your job profile is compared with the corpus, rated between 0% (dissimilar) to 100% (similar). Next, we can get the word frequency among the corpus which gives us an idea of the most common words, phrases, and even sentences to use.
Note that we are not using a standard Boolean search, we are using Latent Semantic Indexing (LSI) which better corresponds with intuitive / human-like search.

![Sample token / keyword output](https://miro.medium.com/max/656/1*ke-McwlBqQx2BB1cAiNK-A.png)
![Sample similarity output](https://miro.medium.com/max/372/1*C_kWbvpeJdrQ7n1wET1ReA.jpeg)

# Conclusion
Overall, you have learned how to use job profile/roles as input training data to the gensim model and have an intuitive understanding of its output. We got an idea of how close your profile is and which phrases or words to use. These information are helpful in creating a good profile suitable for use in recruitment platforms and application tracking systems
