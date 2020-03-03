""" Basic demonstration of running a model in 'prediction' mode.
"""
import sys
import pickle
import random
import copy
from ds.constants import KEY_VECTORIZER, KEY_LOGISTIC_REGRESSION, CLASSIFIER_CATEGORIES


def predict(text, vectorizer, logistic_regression):
    """ Show how you use the models to run a prediction against text
    """
    # "Invoke" the model(s) using the provided text
    #
    categories = copy.copy(CLASSIFIER_CATEGORIES)
    random.shuffle(categories)
    confidences = [0.9435, 0.6231, 0.8432, 0.2127]
    random.shuffle(confidences)
    model_prediction = categories[0]
    model_confidence = confidences[0]

    return model_prediction, model_confidence


def predict_entrypoint(text_to_classify, model_dir='./'):
    """ Show how one would invoke a model against some provided text.
    """
    # Retrieve Pickeled models and unpickle.
    # Typically these would come from some external service, NOT the local disk.
    if model_dir is not None:
        with open(model_dir + KEY_VECTORIZER, 'rb') as f:
            vectorizer = pickle.loads(f.read())
        with open(model_dir + KEY_LOGISTIC_REGRESSION, 'rb') as f:
            logistic_regression = pickle.loads(f.read())

    prediction, confidence =\
        predict(text_to_classify, vectorizer, logistic_regression)

    print('Attempting to classify text:')
    print('    {}'.format(text_to_classify))
    print('-'*28)
    print('Prediction: {}\nConfidence: {}'.format(prediction, confidence))
    print('-'*28)
    print('')

if __name__ == '__main__':
    try:
        text = sys.argv[1]
    except Exception:
        text = "Default text ..."

    predict_entrypoint(text)
