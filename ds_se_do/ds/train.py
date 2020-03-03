""" Basic demonstration of 'training' some classifier model.
"""
import random
import pickle
from ds.constants import KEY_VECTORIZER, KEY_LOGISTIC_REGRESSION, CLASSIFIER_CATEGORIES


def train_model(training_data):
    """ Train the model

        Review previous lectures for real-world examples.
    """
    # Train stuff ... using training_data ...
    # These are clearly NOT functional models, they are just strings of text.
    vectorizer = 'my vectorizer'
    logistic_regression = 'my logistic regression model'

    return vectorizer, logistic_regression


def query_and_clean():
    """ Get documents for training/testing.

        Review previous lectures for real-world examples.
    """
    # Query database(s) and data store(s) for data ...

    # Clean up as necessary to get into useable state.
    cleaned_data = [
        {'label': CLASSIFIER_CATEGORIES[0], 'text': 'fuji'},
        {'label': CLASSIFIER_CATEGORIES[0], 'text': 'golden delicious'},
        {'label': CLASSIFIER_CATEGORIES[1], 'text': 'pepper jack'},
        {'label': CLASSIFIER_CATEGORIES[1], 'text': 'swiss'},
        {'label': CLASSIFIER_CATEGORIES[2], 'text': 'zebra'},
        {'label': CLASSIFIER_CATEGORIES[2], 'text': 'lion'},
    ]

    # Could optionally save these cleaned data locally or in another data store

    return cleaned_data


def load_data(limit=0, split=0.8):
    """ Load the data for the training and deals with train/test split.
    """

    train_data = query_and_clean()  # Load it up
    random.shuffle(train_data)  # Shuffle it
    train_data = train_data[-limit:]  # Limit to # requested
    split = int(len(train_data) * split)  # Get split idx
    return train_data[:split]  # Return data to be used for training


def main(output_dir='./'):
    """ Gather all training / testing data, train models, save trained models.
    """
    print('Training model ...\n')
    training_data = load_data(limit=1000)

    vectorizer, logistic_regression = train_model(training_data=training_data)

    pickled_vectorizer = pickle.dumps(vectorizer)
    pickled_logistic_regression = pickle.dumps(logistic_regression)

    # Save Pickeled models. Normally this would be to cloud storage/db of
    # some kind.
    if output_dir is not None:
        vectorizer_path = output_dir + KEY_VECTORIZER
        print("Saving vectorizer to {}".format(vectorizer_path))
        with open(vectorizer_path, 'wb') as f:
            f.write(pickled_vectorizer)
        lr_path = output_dir + KEY_LOGISTIC_REGRESSION
        print("Saving LR to {}".format(lr_path))
        with open(lr_path, 'wb') as f:
            f.write(pickled_logistic_regression)

if __name__ == '__main__':
    main()
