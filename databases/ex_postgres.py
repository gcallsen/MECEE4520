from datetime import datetime
from models.models import Products, Departments, Session,\
    create_tables, drop_tables


def postgres_demo():
    """ Example use of setting and retrieving a postgres record.
    """
    drop_tables()
    create_tables()

    # Create a database session
    s = Session()

    print('*'*50)
    print('Creating departments ...')
    departments = (
        ('Produce', 'Healthy stuff!'),
        ('Bakery', 'Breads and goodies'),
        ('Deli', 'Meats, cheeses, etc')
    )
    for department in departments:
        d = Departments(
            name=department[0],
            description=department[1]
        )
        s.add(d)
        s.commit()
        print('Added: {}'.format(department[0]))

    print('*'*50)

    print('Creating products ...')
    products = (
        (1, 'Apple', 1.99, 'Delicious Apple'),
        (1, 'Banana', 3.49, 'Bunch of Bananas'),
        (2, 'Bread', 3.99, 'Loaf of whole wheat'),
        (3, 'Cheddar', 2.79, 'Sliced cheddar')
    )
    for product in products:
        p = Products(
            department_id=product[0],
            name=product[1],
            price=product[2],
            description=product[3]
        )
        s.add(p)
        s.commit()
        print('Added: {}'.format(product[1]))

    print('*'*50)
    res = s.query(Products).join(Departments).all()
    print('Result of outer join:')
    for r in res:
        print('{} | {} | {}'.format(r.name, r.department.name, r.price))


if __name__ == '__main__':
    postgres_demo()
