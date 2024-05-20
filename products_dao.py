from sql_connect import get_sql_connection
def get_all(connection):

    cursor = connection.cursor()

    query = ("select product.product_id, product.name, product.uom_id, product.price_perunit, uom.uom_name from product inner join uom on product.uom_id=uom.uom_id;")

    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, price_perunit, uom_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'price_perunit': price_perunit,
                'uom_name': uom_name
            }
        )

    return response


def add_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO product "
             "(name, uom_id, price_perunit)"
             "VALUES (%s, %s, %s)")
    data = (product['name'], product['uom_id'], product['price_perunit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM product where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))

    #****Add and Delete Functionality****#

    # print(delete_product(connection,15))
    # print(add_product(connection, {
    #     'name': 'Detergent',
    #     'uom_id': '1',
    #     'price_perunit': 75
    # }))
