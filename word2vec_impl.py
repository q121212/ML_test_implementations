#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''Freestyle implementation for word2vec.'''

import re

def corpus_load(path_to_file):
    '''Function for loading corpus from file.'''

    corpus, new_corpus = [], []
    with open(path_to_file, 'r') as f:
        text = f.readlines()
    for line in text:
        corpus.append(re.split('\W', line))
    corpus = [item for line_in_corpus in corpus for item in line_in_corpus]
    for item in corpus:
        if item.strip() != '':
            new_corpus.append(item.strip())
    return new_corpus

def freq_of_word(corpus):
    '''Function for counting frequencies of the words from corpus. Returns dict.'''

    words_frequency = dict()
    for item in corpus:
        if  item in words_frequency.keys():
            words_frequency[item]+=1
        else:
            words_frequency.update({item: 1})
    return words_frequency

def sort_and_del_gap_words(corpus, gap_level=1):
    '''Function for removing gap words with frequency == gap_level, and for sorting result.'''

    corpus_with_freq = dict()
    for word in corpus.keys():
        if corpus[word] > gap_level:
            corpus_with_freq.update({word: corpus[word]})
    corpus_with_freq = [{k: corpus_with_freq[k]} for k in sorted(corpus_with_freq, key = corpus_with_freq.get, reverse=True)]
    return corpus_with_freq



def n_gram(corpus, n=2):
    '''n_gram func. n should be 1 and more'''

    if n < 1:
        n = 1
        print('n_gram WARNING: n should be 1 or more. n was changed to 1.')
    n_gram_corpus = []
    for i in range(len(corpus[:-n])):
        n_items = corpus[i:i+n]
        n_gram_corpus.append(' '.join(n_items))
    # print(len(n_gram_corpus))
    n_gram_frequency = freq_of_word(n_gram_corpus)
    return n_gram_frequency


def create_n_subcorpuses(corpus, n=2):
    '''Function for creating n subcorpuses from a big corpus.'''

    len_of_part = int(len(corpus)/n)
    subcorpuses = []
    for i in range(n-1):
        subcorpuses.append(corpus[i*len_of_part:(i+1)*len_of_part])
    subcorpuses.append(corpus[n-1*len_of_part:])
    return subcorpuses




if __name__ == '__main__':
    
    corpus = corpus_load('_data/4.txt')
    # print(corpus[-400:])
    words_frequency = freq_of_word(corpus)
    gap_words = sort_and_del_gap_words(words_frequency, gap_level = 2)

    # print(gap_words[-400:])
    n_gram_frequency = n_gram(corpus, n=2)
    # print(n_gram_frequency)
    print('gap_words:', len(gap_words), 'words_freq:', len(words_frequency), 'corpus', len(corpus), 'n_gram_freq:', len(n_gram_frequency))

    subcorpuses = create_n_subcorpuses(corpus, n=250)
    
    for corp0 in subcorpuses:
        words_frequency = freq_of_word(corp0)
        gap_words = sort_and_del_gap_words(words_frequency, gap_level = 2)
        # print(gap_words[-400:])
        n_gram_frequency = n_gram(corp0, n=5)
        # print(n_gram_frequency)
        print('gap_words:', len(gap_words), 'words_freq:', len(words_frequency), 'corpus', len(corp0), 'n_gram_freq:', len(n_gram_frequency))
        print(sort_and_del_gap_words(n_gram_frequency))
    

    # for corpus in subcorpuses:
    #     # print(corpus[-400:])
    #     words_frequency = freq_of_word(corpus)
    #     gap_words = sort_and_del_gap_words(words_frequency, gap_level = 2)
    #     # print(gap_words[-400:])
    #     n_gram_frequency = n_gram(corpus, n=2)
    #     # print(n_gram_frequency)
    #     print('gap_words:', len(gap_words), 'words_freq:', len(words_frequency), 'corpus', len(corpus), 'n_gram_frequency:', len(n_gram_freq))
