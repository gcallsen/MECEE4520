from class_demo.constants import KEY_VECTORIZER, KEY_LOGISTIC_REGRESSION
import pickle


def predict(text, vectorizer, logistic_regression):
    """ Show how you use the models to run a prediction against text
    """
    # Invoke the model(s) using the provided text

    model_prediction = 'category_1'
    model_confidence = 0.9435

    return model_prediction, model_confidence


def main(model_dir='./'):
    """ Demonstrate how it would be invoked
    """
    # Retrieve Pickeled models and unpickle.
    if model_dir is not None:
        with open(model_dir + KEY_VECTORIZER, 'rb') as f:
            vectorizer = pickle.loads(f.read())
        with open(model_dir + KEY_LOGISTIC_REGRESSION, 'rb') as f:
            logistic_regression = pickle.loads(f.read())

    # This would be coming from somewhere else
    text_to_classify = "my unseen text"

    prediction, confidence =\
        predict(text_to_classify, vectorizer, logistic_regression)

    print('Prediction: {}, Confidence: {}'.format(prediction, confidence))


if __name__ == '__main__':
    main()
