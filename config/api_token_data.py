import json


def login_token():
    with open('E:\gitFile\Aqua_Playwrihgt_shop_test\config\\api_headers.json', 'r') as json_data:
        api_headers = json.load(json_data)
        return api_headers

