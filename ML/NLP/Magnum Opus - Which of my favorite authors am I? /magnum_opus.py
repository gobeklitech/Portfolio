"""

My goal for this cumulative project was to build off of whoami.py wherer we classify text based on the 
author. For that assignment, I decided to try an adjective / adverb frequency distribution approach. 
I ended up building a model that performed with ~98% accuracy against the development set and ~91% 
accuracy against the test set. This model used the standard NLTK Maximum Entropy classifier, which  has 
features that make it sub-optimal for this kind of task. I intended to revisit this assignment and 
experiment with different classifiers, but have been busy and didn’t get around to it.

As such, I decided to revisit and expand upon this concept for the final project. 

My goals were threefold:

- To refine the model with a different classifier and different parameters so it is more accurate on the 
HW2 data

- To collect corpora composed of 500,000 words of prose from 5 of my favorite authors and arrange this into
 the correct form to perform feature extraction required from the refined model

- To retrain the model on my 5 author’ dataset, test the model on an established test set, and then apply 
the model to my own writing in order to analyze how my own adjective and adverb usage relates to that of my 
favorite authors.

Refining the model was fun! I tried a few approaches with mixed results, but settled on the scikit-learn 
Logistic Regression classifier. It obtained an accuracy of 95.4% against the test set, which was good compared
to the MaxEnt number. Not too much to be said here.

Collecting the corpora of 500,000 words of writing from my 5 favorite authors faired incredibly tedious, but 
I was committed to the 500,000 number because it felt like a sufficient volume (an average book from these 
authors is around 130,000). I settled on John Steinbeck, Tom Robbins, Douglas Adams, Jose Luis Borges, and 
Kurt Vonnegut. Most of the writing I got came from the UCSC online library in ePub format, which I then needed
to convert into .txt via .pdf... I’m sure there is a better way, but this took hours and hours to find and 
download over 40 books spanning these authors.

Once I assembled the plain text, I cleaned the sentences and removed all punctuation and other special 
characters. Then I split the data into 500 (at first 100) equal-sized subsections per author, and created an 
aggregated list of (subsection,author) pairs. I shuffled this list (just in case??) and then partitioned it 
90/10 into training/test sets and exported them as TSVs. Thus, these TSVs are in the correct form for the HW2-based
model.

The model trained in ~20 minutes from scratch, which is OK considering this approach. The vast majority of the time 
is spent iterating through and labeling the POS in the corpora. The first time I ran it, I had partitioned each corpus 
into 100 pieces, yielding 450 for the training set and 50 for the test set. The model scored an accuracy of 1.0
against this 50 element test set, so I decided to make the partition finer and raise the number of elements in the 
test set to 250. This yielded an accuracy of .98 on the first go, and ~.975 on average (I guess the RNG seed changes
each time and the shuffle call causes a slight difference each time the program is run?). This is great!
I’m glad the approach generalized to other writing, and the higher accuracy is likely due to the greater volume of
writing per author we used to train this model compared to that in HW2. This was a great learning experience, taking 
the data from its source and processing it into a functional model.

The last step is to apply the model to my own work. I assembled 17 documents that I have written over my time at UCSC 
and labeled them myPiece_1-17.txt. You are welcome to read these if you want! They are mostly creative writing pieces
 and many are pretty out there, but there are a couple random papers in there. I downloaded these as plain text, 
 preprocessed them in the same way as I did the other documents, and aggregated them into a list. Then I fed each element
  of the list to my feature extractor and finally gave the output of each to the classifier.
The results were.. well, interesting? The model predicted that 15 of the 17 pieces of writing were written by Tom Robbins.. 
and in retrospect, there’s an obvious reason: Tom Robbins uses the most adjectives of these 5 by far. Thus, his frequency
 distribution seems more powerful in this model. Either that, or I did something terribly wrong. I ran it multiple times 
 and the results were consistent .

Given infinite time, I would reexamine this and maybe omit Robbins from the bunch.. but in any case, this has been an 
interesting exploration for me, I hope you enjoyed it as well! The takeaway is that either 1) Robbins is the king of wordy 
descriptions or 2) I write like Tom Robbins, which I’m not sure is the case nor if I want it to be.

"""






import nltk

import numpy as np

import random

import csv

from sklearn.linear_model import LogisticRegression 

from nltk.classify.scikitlearn import SklearnClassifier 


def get_adjectives_adverbs():

    """ This just loads a giant list of adjective and adverbs from WordNet"""

    from nltk.corpus import wordnet 

    adjective_list = [word for synset in wordnet.all_synsets(wordnet.ADJ) for word in synset.lemma_names()]

    adverb_list = [word for synset in wordnet.all_synsets(wordnet.ADV) for word in synset.lemma_names()]

    adj_adv_list = adjective_list + adverb_list

    return adj_adv_list


def clean_corpus(text):
    """ This extracts the numbers, newlines, and periods from the text, then truncates the text to a list of 500,000 words"""

    newtext = ''.join([t for t in text if not t.isdigit()])

    newtext = newtext.replace('\\','')

    newtext = newtext.replace('\n','')

    newtext = newtext.replace('.','')

    newtext = newtext.replace('"','')

    newtext = newtext.replace(',','')

    words = nltk.word_tokenize(newtext);

    words = words[:500000]

    return words


def gen_labeled_datasets(words,author):
    """ This generates a (training_set,test_set) pair of labeled TSVs """

    dataset = []

    space = ' '

    for j in range(1000,500000,1000):

        dataset.append([space.join(words[j-1000:j]),author])


    return dataset


def TSV_generator(data_list,outfile_name):

    """ This just writes a list to a TSV for the next step"""

    with open(outfile_name,'w',newline='') as output:  

        tsv_output = csv.writer(output,delimiter = '\t')  

        for row in data_list:

            tsv_output.writerow(row)



def get_model_data(data_list):

    """This partitions our data 90/10 training/test and outputs the two TSVs"""

    big_data = []

    for elem in data_list:

        big_data = big_data + elem

    random.shuffle(big_data)

    length = len(big_data)

    partition = int(.9*length)

    training_set = big_data[:partition]

    test_set = big_data[partition:]

    TSV_generator(training_set,'author_data_training.tsv')

    TSV_generator(test_set,'author_data_test.tsv')



def extract_features(text,pos_list):
    """This creates an adjective / adverb usage fequency distribution using 
    the 
    
    """
    out = nltk.FreqDist()

    word_list = nltk.word_tokenize(text)

    for word in word_list:
        if word in pos_list:
            out[word] += 1      
    
    #print(out)
    return out



def dataset_loader(file):
    """Here we load the TSVs (first those provided in HW2 for testing the new model, then
	the TSVs I constructed. We then call our extract_features method to perform the adjective /
	adverb analysis."""

    out = []
    count = 0
    pos_lists = get_adjectives_adverbs()

    with open(file) as infile:
        for line in infile:
            line = line.strip()
            text, label = line.split("\t")
            #print(text)
            features = extract_features(text,pos_lists)
            instance = (features, label)
            out.append(instance)
            print(count)   # for debugging 
            count += 1 
    #print(out)        
    return out 




def build_classifier(training_set):
    """Here we employ the Scikit-learn logistic regression classifier and train it on
    the relevant training set"""
    

    classifier = SklearnClassifier(LogisticRegression(max_iter = 5000))

    classifier.train(training_set)    


    return classifier



def load_my_writing():

    document_list = []

    space = ' '

    for i in range(17):

        doc_words = clean_corpus(open('myPiece_{}.txt'.format(i+1)).read())

        document_list.append(space.join(doc_words))


    return document_list




def classify_my_writing(document_list,pos_list,classifier):

    for doc in document_list:

        featureset = extract_features(doc,pos_list)

        print(classifier.classify(featureset))





def main():


    Steinbeck_corpus = clean_corpus(open('Steinbeck_corpus.txt').read())

    print(len(Steinbeck_corpus))

    Adams_corpus = clean_corpus(open('Adams_corpus.txt').read())

    print(len(Adams_corpus))

    Robbins_corpus = clean_corpus(open('Robbins_corpus.txt').read())

    print(len(Robbins_corpus))

    Vonnegut_corpus = clean_corpus(open('Vonnegut_corpus.txt').read())

    print(len(Vonnegut_corpus))

    Borges_corpus = clean_corpus(open('Borges_corpus.txt').read())

    print(len(Borges_corpus))





    Steinbeck_dataset = gen_labeled_datasets(Steinbeck_corpus,'John Steinbeck')

    print(len(Steinbeck_dataset))

    Adams_dataset = gen_labeled_datasets(Adams_corpus,'Douglas Adams')

    print(len(Adams_dataset))

    Robbins_dataset = gen_labeled_datasets(Robbins_corpus,'Tom Robbins')

    print(len(Robbins_dataset))

    Vonnegut_dataset = gen_labeled_datasets(Vonnegut_corpus,'Kurt Vonnegut')

    print(len(Vonnegut_dataset))

    Borges_dataset = gen_labeled_datasets(Borges_corpus,'Jorge Luis Borges')

    print(len(Borges_dataset))






    get_model_data([Steinbeck_dataset,Adams_dataset,Robbins_dataset,Vonnegut_dataset,Borges_dataset])


    training_set = dataset_loader('author_data_training.tsv')

    dev_set = dataset_loader('author_data_test.tsv')

    classifier = build_classifier(training_set)

    acc = nltk.classify.accuracy(classifier, dev_set)

    print("Refined classifier got an accuracy of:", acc , " on the new data")




    document_list = load_my_writing()

    pos_list = get_adjectives_adverbs()


    classify_my_writing(document_list,pos_list,classifier)


    #return classifier , training_set , dev_set


if __name__ == "__main__": main()
