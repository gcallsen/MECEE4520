from datetime import datetime
from elasticsearch import Elasticsearch

# Establish elasticsearch connection
es = Elasticsearch("elasticsearch:9200")


def elasticsearch_demo():
    """ Example use of setting and retrieving a document in ES.

        Note: This also creates a test index if it doesn't exist
    """

    recipes = (
        {
            "_id": "sandwich_ham",
            "body": {
                "ingredients": ['wheat bread', 'cheddar', 'ham']
            }
        },
        {
            "_id": "sandwich_turkey",
            "body": {
                "ingredients": ['wheat bread', 'cheddar', 'turkey']
            }
        },
        {
            "_id": "cheese_platter_1",
            "body": {
                "ingredients": ['cheddar', 'mozzarella', 'olives']
            }
        },
        {
            "_id": "cheese_platter_2",
            "body": {
                "ingredients": ['pepper jack', 'mozzarella', 'olives']
            }
        }
    )
    for recipe in recipes:
        res = es.index(
            index="recipe-index",
            doc_type='recipe',
            id=recipe['_id'],
            body=recipe['body']
        )
        print(res['result'])

    res = es.get(index="recipe-index", doc_type='recipe', id='sandwich_ham')
    print(res['_source'])

    es.indices.refresh(index="recipe-index")

    res = es.search(index="recipe-index", body={"query": {"match_all": {}}})
    print("Got {} Hits:".format(res['hits']['total']))
    for hit in res['hits']['hits']:
        print("{}: {}".format(hit['_id'], hit["_source"]['ingredients']))


def search_example(ingredient):
    """ Basic example of searching elasticsearch for recipes w/ an ingredient
    """
    query = {
        "query": {
            "multi_match": {
                "query": ingredient,
                "fields": ["ingredients"]
            }
        }
    }
    res = es.search(index="recipe-index", body=query)
    print("Found {} recipes containing `{}`:"
          .format(res['hits']['total'], ingredient))
    for hit in res['hits']['hits']:
        print("{}: {}".format(hit['_id'], hit["_source"]['ingredients']))


if __name__ == '__main__':
    elasticsearch_demo()
