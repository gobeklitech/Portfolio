"""
Author: Edward Hayden

Referenced: https://newbedev.com/getting-a-large-list-of-nouns-or-adjectives-in-python-with-nltk-or-python-mad-c

REFLECTIONS AND INSIGHTS:

# ----- PREFACE -----

# Our task is author classification, so it begs the question: which features in an author's prose
# are most unique to the specific author? Off the top of my (human) head, one's use of adjectives/adverbs
# is frequently a dead givaway.. "use of adjectives/adverbs" is somewhat ambiguous, so I will try a couple 
# disambiguation strategies... Hopefully it works! 

# Strategy 1: I will use a "bag of adverbs" and "bag of adjectives" and compare the results of each
# Strategy 2: I will try a "bag of adverb and adjectives" to see if it performs better than the separate bags

# After devising this strategy, I realized the words I am working with are un-tagged (duh), so the first 
# step will be to construct a large body of adjectives and adverbs. I will stay within NLTK for this, and 
# to achieve a more diverse body of language I will stray from the Brown corpus. 

# I will use WordNet, as it seems the most diverse corpus and pre-separated by POS. My "data generation" 
# step will be pretty slow, as my only option is a brute-force comparison. The training step should be OK
# though. 

# ----- REFLECTION ------

# As predicted, my "Data Generation" step is incredibly slow... there must be a faster way to perform my 
# "is this an adjective or adverb?" check, most obviously by using Numpy or another faster array technique,
# but there is likely something MUCH more obvious and fundamental that I am missing...
#
# In terms of results, my model did fairly well! I suppose that depends on how you look at the accuracy...
#
# I stuck with the MaxEnt classifier, as the structure of my program made it slow to try different models. 
# Again, I am somewhat inexperienced with python, so it wasn't immediately clear to me how to separate the 
# "load_dataset" method and call it in my Env so that I could train other models on it.. something else to 
# ask about in office hours.

# I settled on MaxEnt at 20 iterations and the combined adjectives + adverbs approach, which took reasonable 
# time to train on my laptop. The performance breakdown is as follows:

# The model reported accuracies of:

# - .793 after 5 iterations
# - .966 after 10 iterations 
# - converged to .994 after 20 iterations 

# - reported .912 against the test set, fairly overfit

"""

import nltk

# numpy isn't used directly -- this is just here to let you know that you need
# it installed in your Python environment for this code to work.
import numpy


class BaselineClassifier(nltk.classify.ClassifierI):
    """Baseline classifier -- always guesses the most common label."""
    def __init__(self):
        self.fd = nltk.probability.FreqDist()
    def train(self, labeled_featuresets):
        self.fd.clear()
        for (f,label) in labeled_featuresets:
            self.fd[label] += 1 
    def classify(self, featureset):
        return self.fd.max()
    def prob_classify(self, featureset):
        return nltk.probability.DictionaryProbDist({self.fd.max(): 1.0})


def get_adjectives_adverbs():

    """This just loads a giant list of adjective and adverbs from WordNet"""

    from nltk.corpus import wordnet 

    adjective_list = [word for synset in wordnet.all_synsets(wordnet.ADJ) for word in synset.lemma_names()]

    adverb_list = [word for synset in wordnet.all_synsets(wordnet.ADV) for word in synset.lemma_names()]

    adj_adv_list = adjective_list + adverb_list

    return [adjective_list,adverb_list,adj_adv_list]   




def text_to_features(text,feature = 'letter',pos_list = []):
    """Take some text and turn it into an NLTK feature dictionary, mapping from
    named features to numbers.

    I Implemented the adjective/adverb feature extraction described
    """
    out = nltk.FreqDist()

    if feature == 'letter':
        # count up all the letters!
        for c in text:
            out[c] +=1
    else:
        word_list = nltk.word_tokenize(text)


    if feature == 'adjectives':   

        for word in word_list:
            if word in pos_list:
                out[word] += 1

    elif feature == 'adverbs':       

        for word in word_list:
            if word in pos_list:
                out[word] += 1

    elif feature == 'adjectives/adverbs': 

        for word in word_list:
            if word in pos_list:
                out[word] += 1      
    
    #print(out)
    return out




def load_dataset(filename):
    """Given a filename, load the TSV data and do feature extraction on it.
    Return a list of (feature, label) pairs."""
    out = []
    count = 0
    pos_lists = get_adjectives_adverbs()
    with open(filename) as infile:
        for line in infile:
            line = line.strip()
            text, label = line.split("\t")
            #print(text)
            features = text_to_features(text,'adjectives/adverbs',pos_lists[2])
            instance = (features, label)
            out.append(instance)
            print(count)
            count += 1 
    #print(out)        
    return out



def build_classifier(training_set,classifier_type = 'maxent'):

    if classifier_type == 'maxent':
        classifier = nltk.classify.MaxentClassifier.train(training_set,
                                                      max_iter=20)

    return classifier

def main():
    training_set = load_dataset("author_data_train.tsv")
    dev_set = load_dataset("author_data_dev.tsv")

    baseline_classifier = BaselineClassifier()
    baseline_classifier.train(training_set)

    better_classifier = build_classifier(training_set)

    acc = nltk.classify.accuracy(baseline_classifier, dev_set)
    print("baseline classifier got an accuracy of:", acc)

    acc = nltk.classify.accuracy(better_classifier, dev_set)
    print("better classifier got an accuracy of:", acc)


if __name__ == "__main__": main()
