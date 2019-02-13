#!/usr/bin/python
import sys, getopt
from optparse import OptionParser
#import nltk
#from nltk.book import text1

from textblob import TextBlob
from textblob import Word
from textblob.wordnet import NOUN
import random
import sys

def main(argv):
    #nltkTest()
    textblobTest()

def textblobTest():
    blob = TextBlob("ITP is a two-year graduate program good located in the Tisch School of the Arts. "
                    "Perhaps the best way to describe great us is as a Center for the Recently Possible.")

    print(str(blob.sentiment.__getattribute__('polarity')))

    # """
    # Sentence Printer
    # """
    # for sentence in blob.sentences:
    #     print(sentence)
    #
    # """
    # Tokenize words
    # """
    # # for word in blob.sentences[1].words:
    # #     print(word)
    #
    # """
    # Identify Noun Phrases
    # """
    # # for np in blob.noun_phrases:
    # #     print(np)
    #
    # """
    #     part of speech each word in a text corresponds
    # """
    # # for word, pos in blob.tags:
    # #     print(word, pos)
    #
    # """
    # Pluralize
    # """
    # w = Word("university")
    # print(w.pluralize())
    #
    # """
    # Remove Morphology
    # """
    # w = Word("universities")
    # print(w.lemmatize())
    #
    #
    # """
    # Identify words by part of speech in a text
    # """
    # blob = TextBlob("I spy a lion, a tiger, and a bear.")
    # sentence = blob.sentences[0]
    # for word, pos in sentence.tags:
    #     if pos == 'NN':
    #         print(word.pluralize())
    #
    # """
    #     Call: python hemingwayize.py < austen.txt
    #     stdin's read() method just reads in all of standard input as a string;
    #     use the decode method to convert to ascii (textblob prefers ascii)
    # """
    # text = sys.stdin.read().decode('ascii', errors="replace")   # decode removes any non-ascii characters from the text
    # blob = TextBlob(text)
    #
    # short_sentences = list()
    # for sentence in blob.sentences:
    #     if len(sentence.words) <= 5:
    #         short_sentences.append(sentence.replace("\n", " "))
    #
    # for item in random.sample(short_sentences, 10):
    #     print(item)
    #
    #
    #
    # """
    #     Call: python hemingwayize.py < austen.txt
    #     Turn text into list of 'instructions'
    #     Identify all nouns and verbs and make a random selection and list them
    # """
    # text = sys.stdin.read().decode('ascii', errors="replace")
    # blob = TextBlob(text)
    #
    # noun_phrases = blob.noun_phrases
    #
    # verbs = list()
    # for word, tag in blob.tags:
    #   if tag == 'VB':
    #     verbs.append(word.lemmatize())
    #
    # for i in range(1, 11):
    #   print("Step " + str(i) + ". " + random.choice(verbs).title() + " " + random.choice(noun_phrases))
    #
    # """
    #     Call: python hemingwayize.py < austen.txt
    #     This program “summarizes” a text in a very basic way. It does so by examining the part of speech of each word,
    #     and appending the word to a list if the word is a noun; it then prints out five random nouns from the text in plural form
    # """
    # text = sys.stdin.read().decode('ascii', errors="ignore")
    # blob = TextBlob(text)
    #
    # nouns = list()
    # for word, tag in blob.tags:
    #     if tag == 'NN':
    #         nouns.append(word.lemmatize())
    #
    # print "This text is about..."
    # for item in random.sample(nouns, 5):
    #     word = Word(item)
    #     print word.pluralize()


    """
        Synset (similarity set)
        Words belong to multiple synsets
    """
    # bank = Word("bank")
    # synsets = bank.synsets
    # print(synsets)

    # synsets = Word("bank").synsets
    # for synset in synsets:
    #     print(synset.definition())

    # synsets = Word("bank").get_synsets(pos=NOUN)
    # for synset in synsets:
    #     #print(synset.definition()) # get from multiple synsets
    #     print(synsets[1].lemma_names()) # Synonyms
    #
    #
    # """
    # Synonymize
    # This program reads in a ext, parses it into words, and then replaces each word with a random synonym
    # (according to WordNet). Only words with three or more letters that have synonyms in WordNet are replaced.
    # """
    # for line in sys.stdin:
    #     line = line.strip()
    #     line = line.decode('ascii', errors="replace")
    #     words = line.split(" ")
    #     output = list()
    #     for word_str in words:
    #         word_obj = Word(word_str)
    #         if len(word_str) > 3 and len(word_obj.synsets) > 0:
    #             random_synset = random.choice(word_obj.synsets)
    #             random_lemma = random.choice(random_synset.lemma_names)
    #             output.append(random_lemma.replace('_', ' '))
    #         else:
    #             output.append(word_str)
    #     print(" ".join(output))

def nltkTest():
    #print(book.text1)

    # Handlers
    #print(nltk._treebank_word_tokenizer(text1))

    #print(text1.common_contexts(['big','likey'])) # allows us to examine just the contexts that are shared by two or more words, such as monstrous and very.
    print('------------------------')
    #print(text1.similar('big'))


    # print(text1.concordance('monstrous'))
    print(text1.generate()) #generate random text

    """
    Visualize vocabulary and frequency used in text
    """
    print(text1.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"]))


    """
    Lengths of text, vocabulary used
    """
    len(text1)
    sorted(set(text1))  # Sorted list of vocabulary
    len(set(text1))


    """
    The next example shows us that the number of distinct words is just 6% of the total number of words,
    or equivalently that each word is used 16 times on average
    """

    def lexical_diversity(text):
        return len(set(text)) / len(text)

    def percentage(count, total):
        return 100 * count / total

    print(lexical_diversity(text1))
    print(percentage(text1.count('a'), len(text1)))



if __name__ == "__main__":
    main(sys.argv[1:])