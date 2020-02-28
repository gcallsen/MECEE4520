from datetime import datetime
import redis

# Establish redis connection
r = redis.Redis(host='redis', port=6379, db=0)


def redis_demo():
    """ Example use of setting and retrieving a key in redis
    """
    recipes = (
        (
            "sandwich_ham",
            "ingredients: ['wheat bread', 'cheddar', 'ham']"
        ),
        (
            "sandwich_turkey",
            "ingredients: ['wheat bread', 'cheddar', 'turkey']"
        ),
        (
            "cheese_platter_1",
            "ingredients: ['cheddar', 'mozzarella', 'olives']"
        ),
        (
            "cheese_platter_2",
            "ingredients: ['pepper jack', 'mozzarella', 'olives']"
        )
    )
    for recipe in recipes:
        r.set(recipe[0], recipe[1])

    keys = r.keys("*")
    for key in keys:
        val = r.get(key).decode('utf-8')
        print("{}: {}".format(key.decode('utf-8'), val))
    # print("{}\nMy Ham Sandwich Recipe:\n{}\n{}".format("*"*50, my_key, "*"*50))


if __name__ == '__main__':
    redis_demo()
