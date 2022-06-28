"""
Author: Edward Hayden

"""

"""
REFLECTIONS AND INSIGHTS:

# ----- PREFACE -----

# Our goal here is to develop N-gram language models via NLTK, using The Time Machine
# as our corpus. We will use this to generate random sentences. 

# I chose 'The Time Machine' by H.G. Wells because I have actually read it and it's a 
# wonderful book. It is rather short, however Wells' diversity of language should (hopefully) 
# prove to construct a good basis for a model. 

# ----- REFLECTION -----

# The manual tagging part was somewhat brutal.. but definitely worthwhile!

# I had a bit of trouble with the 'one_sentence_per_line' module, so I build an 'equivalent' 
# called 'clean_text_document', which I use throughout this file.

# I have two core methods: build_digram_language_model and build_trigram_language_model 
# that allow me to independently explore the results of the LMs produced with these two
# methods. 

# With the output of these, I can call 'sample_sentences' with these LMs as
# inputs in order to conveniently analyze their perfomance.
 
# The random sentences are awesome! My Trigram model seemed to produce more coherent sentences..
# I'm not sure if this was a coincidence or a product of a better model. In any case this 
# part was pretty fun. 

# I build a heirarchical N-gram tagger structured off the example provided. It performed with 
# an accuracy of .913, which is so-so. I could think of a few ways to improve the accuracy of this
# tagger if I were to reapproach. 


"""

import nltk

# numpy isn't used directly -- this is just here to let you know that you need
# it installed in your Python environment for this code to work.

import numpy

import one_sentence_per_line

# -- PART ONE -- 

def manually_tag_sentences():

    """Here I maually tag some sentences. Returns a list of the original sentences and the list of tagged sentences"""

    s0 = 'Now, it is very remarkable that this is so extensively overlooked continued the Time Traveller, with a slight accession of cheerfulness'
  
    s1 = 'Our mental existences, which are immaterial and have no dimensions, are passing along the Time-Dimension with a uniform velocity from the cradle to the grave'
  
    s2 = 'To discover a society, said I, erected on a strictly communistic basis'
  
    s3 = 'This saddle represents the seat of a time traveller'
   
    s4 = 'We cannot see it, nor can we appreciate this machine, any more than we can the spoke of a wheel spinning, or a bullet flying through the air'
   
    s5 = 'Mrs. Watchett came in and walked, apparently without seeing me, towards garden door'
   
    s6 = 'Once they were there, they would no doubt have to pay rent, and not a little of it, for the ventilation of their caverns; and if they refused, they would starve or be suffocated for arrears'
   
    s7 = 'Living, as they did, in what appeared to me impenetrable darkness, their eyes were abnormally large and sensitive, just as are the pupils of the abysmal fishes, and they reflected the light in the same way'
  
    s8 = 'No Morlocks had approached us'
   
    s9 = 'She wanted to run to it and play with it'



    s0_pos = ['adverb',',','pronoun','verb','adverb','adjective','preposition','determiner','verb','adverb','adverb','verb','verb','determiner','noun','noun',',','preposition','determiner','adjective','noun','preposition','noun']

    s1_pos =['pronoun','adjective','noun',',','determiner','verb','adjective','conjunction','verb','determiner','noun',',','verb','verb','preposition','determiner','noun','preposition','determiner','adjective','noun','preposition','determiner','noun','determiner','determiner','noun']

    s2_pos =['determiner','verb','determiner','noun',',','verb','pronoun',',','verb','preposition','determiner','adverb','adjective','noun']

    s3_pos =['determiner','noun','verb','determiner','noun','preposition','determiner','noun','noun']

    s4_pos =['pronoun','verb','adverb','verb','pronoun',',','conjunction','verb','pronoun','verb','determiner','noun',',','determiner','adjective','preposition','pronoun','verb','determiner','verb','preposition','determiner','noun','adjective',',','conjunction','determiner','noun','verb','preposition','determiner','noun']

    s5_pos = ['noun','noun','verb','preposition','conjunction','verb',',','adverb','preposition','verb','pronoun',',','preposition','noun','noun']

    s6_pos = ['adverb','pronoun','verb','adverb',',','pronoun','verb','determiner','noun','verb','determiner','verb','noun',',','conjunction','adverb','determiner','adjective','preposition','pronoun',',','preposition','determiner','noun','preposition','pronoun','noun',',','conjunction','preposition','pronoun','verb',',','pronoun','verb','verb','conjunction','verb','verb','preposition','noun']

    s7_pos = ['verb',',','preposition','pronoun','verb',',','preposition','pronoun','verb','determiner','pronoun','adjective','noun',',','pronoun','noun','verb','adverb','adjective','conjunction','adjective',',','adverb','adverb','verb','determiner','noun','preposition','determiner','adjective','noun',',','conjunction','pronoun','verb','determiner','noun','preposition','determiner','adjective','noun']

    s8_pos = ['determiner','noun','verb','verb','pronoun']

    s9_pos = ['pronoun','verb','determiner','verb','determiner','pronoun','conjunction','verb','preposition','pronoun']


    Univ_POS_list = ['ADJ','ADP','ADV','AUX','CCONJ','DET','INTJ','NOUN','NUM','PART','PRON','PROPN','PUNCT','SCONJ','SYM','VERB']

    My_POS_list = ['adjective','preposition','adverb','auxilary','conjunction','determiner','interjection','noun','number','particle','pronoun','proper noun',',','conjunction','symbol','verb']


    sent_list = [s0,s1,s2,s3,s4,s5,s6,s7,s8,s9]

    sent_pos_list = [s0_pos,s1_pos,s2_pos,s3_pos,s4_pos,s5_pos,s6_pos,s7_pos,s8_pos,s9_pos]

    for sent_pos in sent_pos_list:

        count = 0

        for elem in sent_pos:

            elem = Univ_POS_list[My_POS_list.index(elem)]

            sent_pos[count] = elem

            count += 1 

    #return sent_pos_list        

    count = 0 

    tagged_sents_list = []

    #print(sent_pos_list)

    #print('\n\n\n\n\n')

    #print(sent_list)

    #print('\n\n\n\n\n')

    for sent in sent_list:

        words = nltk.word_tokenize(sent)

        tags = sent_pos_list[count]

        newcount = 0

        tagged_sent = []

        for word in words:

            tagged_sent.append((word,tags[newcount]))

            newcount += 1 

        tagged_sents_list.append(tagged_sent)    

        count += 1 

    print(tagged_sents_list)

    return tagged_sents_list    


# -- PART TWO -- 


def clean_text_document(infile):

    text = open(infile).read()

    text = nltk.sent_tokenize(text)

    new_text_list = []

    words_list = []

    for sent in text:

        sent = sent.replace('\n',' ')

        words = nltk.word_tokenize(sent)

        words.append('</s>')

        new_text_list.append(sent)

        words_list.append(words)

    return new_text_list , words_list




def build_digram_model(text):

    from nltk.lm.preprocessing import padded_everygram_pipeline 

    train , vocab = padded_everygram_pipeline(2,text)

    return train , vocab 




def build_trigram_model(text):

    from nltk.lm.preprocessing import padded_everygram_pipeline 

    train , vocab = padded_everygram_pipeline(3,text)

    return train , vocab 




def build_digram_language_model(text):

    from nltk.lm import MLE 

    lm = MLE(2)

    train , vocab = build_digram_model(text)

    lm.fit(train,vocab)

    return lm




def build_trigram_language_model(text):

    from nltk.lm import MLE 

    lm = MLE(3)

    train , vocab = build_trigram_model(text)

    lm.fit(train,vocab)

    return lm 



def sample_sentences(lm):

    sents_list = []

    for i in range(5):

        text_seed = 'a'

        sent = ''

        while text_seed != ['</s>']:

            new_seed = lm.generate(1,text_seed = text_seed)

            sent = sent + ' ' + new_seed

            text_seed = [new_seed]

        print(str(i + 1) + ': ' + sent)   
        
        print('\n') 

        sents_list.append(sent);   

    return(sents_list)


def build_tagger():

    tagged_sents = list(nltk.corpus.brown.tagged_sents())

    l = int(len(tagged_sents)*.9)

    training_set = tagged_sents[:l]

    test_set = tagged_sents[l:]

    base_tag  = nltk.DefaultTagger('NN')

    tagger_0 = nltk.UnigramTagger(training_set,backoff = base_tag)

    tagger_1 = nltk.BigramTagger(training_set,backoff = tagger_0)

    tagger_2 = nltk.TrigramTagger(training_set,backoff = tagger_1)

    print('Tagger Accuracy : \n')

    print(tagger_2.evaluate(test_set))

    print('\n')




def main():

    print('\n')
    print('---- INIT ----')
    print('\n')
    print('---- MANUALLY TAGGING SENTENCES ----')
    print('\n')
    manually_tag_sentences()

    clean_sents , clean_words  = clean_text_document('The_Time_Machine.txt')

   
    print('\n')
    print('(cleaned_sents , cleaned_words) assigned to the output of preprocessing The Time Machine by H.G. Wells')
    print('\n')
    print('---- TRAINING DIGRAM LM ----')
    print('\n')

    digram_lm = build_digram_language_model(clean_words)

    print('digram_lm assigned to our digram language model')
    print('\n')
    print('---- TRAINING TRIGRAM LM ----')
    print('\n')

    trigram_lm = build_trigram_language_model(clean_words)

    print('trigram_lm assigned to our digram language model')
    print('\n')
    print('---- GENERATING SAMPLE SENTENCES - DIGRAM LM ----')
    print('\n')

    digram_samples = sample_sentences(digram_lm)

    print('---- GENERATING SAMPLE SENTENCES - TRIGRAM LM ----')
    print('\n')

    trigram_samples = sample_sentences(trigram_lm)

    print('\n')
    print('---- TRAINING TAGGER ----')
    print('\n')
    build_tagger()


if __name__ == "__main__": main()
