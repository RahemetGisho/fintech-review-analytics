import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")


def preprocess_text(text, lemmatize=True):
    """
    Preprocess review text using spaCy.

    Steps:
    - Lowercasing
    - Tokenization
    - Stop-word removal
    - Punctuation removal
    - Optional lemmatization
    """

    doc = nlp(str(text).lower())

    tokens = []

    for token in doc:

        if (
            not token.is_stop and
            not token.is_punct and
            token.is_alpha
        ):

            if lemmatize:
                tokens.append(token.lemma_)
            else:
                tokens.append(token.text)

    return " ".join(tokens)