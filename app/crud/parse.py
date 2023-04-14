import requests


def parse_data(id):
    response = requests.get(
        f'https://card.wb.ru/cards/detail?dest=123585705&nm={id}'
    )
    data = response.json()
    if len(data.get('data')['products']) != 0:
        product_info = data.get('data')['products'][0]
        product_data = {'colors': '', 'quantity': 0}
        product_data['nm_id'] = id
        product_data['name'] = product_info['name']
        product_data['brand'] = product_info['brand']
        product_data['brand_id'] = product_info['brandId']
        product_data['site_brand_id'] = product_info['siteBrandId']
        product_data['supplier_id'] = product_info['supplierId']
        product_data['sale'] = product_info['sale']
        product_data['price'] = int(str(product_info['priceU'])[0:-2])
        product_data['sale_price'] = int(str(product_info['salePriceU'])[0:-2])
        product_data['rating'] = product_info['rating']
        product_data['feedbacks'] = product_info['feedbacks']
        for size in product_info['sizes']:
            if len(size['stocks']) != 0:
                product_data['quantity'] += size['stocks'][0]['qty']
        if len(product_info['colors']) != 0:
            for color in product_info['colors']:
                product_data['colors'] += (f"{color['name']} ")
        return product_data
    else:
        return {'error': 'no such product'}
