def build_classifier(training_set):
    """Here we employ the Scikit-learn logistic regression classifier and train it on
    the relevant training set"""
    
    #classifier = nltk.classify.MaxentClassifier.train(training_set,
                                                      #max_iter=20)

    classifier = LogisticRegression(max_iter = 5000)

    classifier.fit(training_set)                                         

    return classifier


def main():





if __name__ == "__main__": main() 