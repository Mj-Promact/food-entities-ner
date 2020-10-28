import re
##import nltk
import random
import pickle
import unicodedata
import numpy as np
##import pandas as pd


def comb_id_review(df: pd.core.frame.DataFrame) -> list:
    """Create tuple of user id and individual review for all reviews."""

    list_reviews = []
    for row in df.itertuples(index=False, name=None):
        list_reviews.append(row)

    return list_reviews


def split_sentence(list_reviews: list) -> list:
    """
    Split individual reviews into sentences.
    Format - (user id, [sentences])
    """

    review_sentences = []
    for user_id, review in list_reviews:
        sentence = unicodedata.normalize('NFKD', review).encode('ascii', 'ignore')
        sentences = nltk.sent_tokenize(sentence, language="english")
        review_sentences.append((user_id, sentences))

    return review_sentences

def index_sentence(review_sentences: list) -> list:
    """
    Append an index value to all sentences.
    """

    sentences_list = []
    for review in review_sentences:
        sentences_list.extend(review[1])

    sentences_list = [(i, row) for i, row in enumerate(sentences_list)]

    return sentences_list


def pos_tagger(sentences_list: list) -> list:
    """
    POS tag all words in each sentence.
    """

    pos_tag_list = []
    for sentence in sentences_list:
        pos_tag_list.append(nltk.pos_tag(re.findall(r"[\w']+|[(.,!?;)]",
                                                    sentence[1])))

    return pos_tag_list
