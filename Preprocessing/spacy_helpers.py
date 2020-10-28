import pickle

def prepare_spacy_data(data: list) -> list:
    """
    Convert the data into spacy train data format.
    Here data should be in following format, [(word, postag, tag), ...]
    """

    target_label = "FOOD"
    spacy_data = []

    for row in data:
        words = []
        entities = []
        for i, (token, postag, tag) in enumerate(row):
            words.append(token)

            if tag == target_label:
                if i == 0:
                    entities.append((i, len(token), target_label))
                else:
                    st_pos = sum([len(word) for word in words[:-1]]) + i
                    end_pos = st_pos + len(token)
                    entities.append((st_pos, end_pos, target_label))

        spacy_data.append((" ".join(words[:-1])+words[-1], {"entities": entities}))

    return spacy_data



if __name__ == "__main__":

    
    with open("train_sentences.pkl", "rb") as f:
        train_sentences = pickle.load(f)

    with open("test_sentences.pkl", "rb") as f:
        test_sentences = pickle.load(f)

    all_sentences = train_sentences + test_sentences

    spacy_data = prepare_spacy_data(all_sentences)

    with open("spacy_format_data.pkl", "wb") as f:
        pickle.dump(spacy_data, f)
