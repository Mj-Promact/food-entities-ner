import numpy as np

def word2features(sent: list, i: int) -> dict:
    """
    Define word features.
    """

    word = sent[i][0]
    postag = sent[i][1]

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'postag': postag,
        'postag[:2]': postag[:2],
        }

    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1.word.isdigit()': word1.isdigit(),
            '-1:postag': postag1,
            '-1:postag[:2]': postag1[:2],
            })

    if i > 1:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        word2 = sent[i-1][0]
        postag2 = sent[i-2][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1.word.isdigit()': word1.isdigit(),
            '-1:postag': postag1,
            '-1:postag[:2]': postag1[:2],
            '-2:word.lower()': word2.lower(),
            '-2:word.istitle()': word2.istitle(),
            '-2:word.isupper()': word2.isupper(),
            '-2:postag': postag2,
            '-2:postag[:2]': postag2[:2],
            })

    else:
        features['BOS'] = True

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:postag': postag1,
            '+1:postag[:2]': postag1[:2],
            })

    if i < len(sent)-2:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        word2 = sent[i+2][0]
        postag2 = sent[i+2][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:postag': postag1,
            '+1:postag[:2]': postag1[:2],
            '+2:word.lower()': word2.lower(),
            '+2:word.istitle()': word2.istitle(),
            '+2:word.isupper()': word2.isupper(),
            '+2:postag': postag2,
            '+2:postag[:2]': postag2[:2],
            })
    else:
        features['EOS'] = True

    return features


def sent2features(sent: list) -> list:
    """
    Convert sentence into features.
    """

    return [word2features(sent, i) for i in range(len(sent))]


def sent2labels(sent: list) -> list:
    """
    Extract label from the sentence list.
    """

    return [label for token, postag, label in sent]


def sent2tokens(sent: list) -> list:
    """
    Extract token from sentence list.
    """

    return [token for token, postag, label in sent]


def extract_label(prediction: list) -> list:
    """
    Find the label from the predicted array.
    """

    labels = ["FOOD", "O"]
    predicted_labels = []
    for row in prediction:
        food_count = row.count(labels[0])
        nofood_count = row.count(labels[1])

        food_score = food_count / len(row)
        nofood_score = nofood_count / len(row)

        pred_ind = np.argmax([food_score, nofood_score])

        predicted_labels.append(labels[pred_ind])

    return predicted_labels
