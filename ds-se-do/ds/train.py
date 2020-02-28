from class_demo.constants import KEY_VECTORIZER, KEY_LOGISTIC_REGRESSION
import random
import pickle


def train_model(training_data):
    """ Train the model ...
    """

    # See previous code for real-world example.

    # Train stuff ... using training_data ...
    vectorizer = 'my vectorizer'
    logistic_regression = 'my logistic regression model'

    return vectorizer, logistic_regression


def query_and_clean():
    """ Get documents for training/testing.
    """

    # Query database(s) and data store(s) for data.

    # Clean up as necessary to get into useable state.
    cleaned_data = [
        {'label': 'category_1', 'text': 'bar'},
        {'label': 'category_1', 'text': 'baz'},
        {'label': 'category_2', 'text': 'boo'},
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
    print('Training model ...')
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
