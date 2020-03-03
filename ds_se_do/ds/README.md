# Data Scientist (DS)

From our lecture slides, The "Data Scientist" cares about:

* Rapid Iteration
* Performance Metrics
* _Functional Models_

This is a short demonstration of some 'functional models' one might produce
(they are all examples / not actually functional).

## Usage

This will use the same environment as the previous Lecture. Your system
must have a functional [Docker installation](https://docs.docker.com/install/)

To run this code inside a pre-configured Docker image, you can simply run:

    docker run -it --rm --net python-dev_default -v /path/to/MECEE4520/ds_se_do:/code rhoai/python-dev:v0.1.0

### Initial Setup

Inside that container, run the following two commands:

    cd /code
    pip install -e .

## Run Examples

When inside of the running container, having installed the 'package' from the previous step,
you can run the two "data science" files:

    python ds/train.py

You'll see output similar to:

    Training model ...
    Saving vectorizer to ./demo_namespace_vectorizer
    Saving LR to ./demo_namespace_logistic_regression

Subsequently, you can run:

    python ds/predict.py

Which will produce output similar to:

    Attempting to classify text:
        Classify Me!
    ----------------------------
    Prediction: apple
    Confidence: 0.2127
    ----------------------------
