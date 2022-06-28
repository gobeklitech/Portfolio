import nltk 

def get_sample_CFG():

    grammar1 = nltk.CFG.fromstring("""
        S -> NP VP
        VP -> V NP | V NP PP
        PP -> P NP
        V -> "saw" | "ate" | "walked"
        NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
        Det -> "a" | "an" | "the" | "my"
        N -> "man" | "dog" | "cat" | "telescope" | "park"
        P -> "in" | "on" | "by" | "with"
        """)

    return grammar1


def CYK_parse_sent(sentence,grammar_in_CNF):

    words = sentence.split()

    size = len(words)

    # -- temp -- 

    parser = nltk.ChartParser(grammar_in_CNF)

    parse_table = parser.parse(words)

    return parse_table



def RD_parse_sent(sentence,grammar_in_CNF):

    words = sentence.split()

    parser = nltk.RecursiveDescentParser(grammar_in_CNF)

    parse_table = parser.parse(words)

    return parse_table    



def get_sents():

    s1 = "the dog saw a man in the park"

    s2 = "Mary walked a cat"

    s3 = "the cat saw Mary with a telescope"

    s4 = "the cat saw the man with a telescope"

    sents_list = [s1,s2,s3,s4];

    return sents_list



def main():

    sample_CFG = get_sample_CFG()

    CNF_grammar = sample_CFG.chomsky_normal_form()

    sents_list = get_sents()

    print('------ CYK parse ------')

    for sent in sents_list:

        parse_table = CYK_parse_sent(sent,CNF_grammar)

        for element in parse_table:

            print(element)

    print('--------------------- \n\n --------------------\n')

    print('------ RD parse ------')

    for sent in sents_list:

        parse_table = RD_parse_sent(sent,CNF_grammar)

        for element in parse_table:

            print(element)




if __name__ == "__main__": main()