import json
from playwright.sync_api import sync_playwright, Playwright, expect


def test_api_login(playwright: Playwright):
    """
    登录
    :return:
    """
    url = 'https://test-toodudu.ptdplat.com/login'
    # password = hashlib.md5(str('a123456').encode()).hexdigest()
    request_data = {
            "name": "李龙威",
            "password": "n+9tOj7hac6byhNAdMytB1pkuV9lLr/VhD0waUUi5IqS/yX5ST3JHHdEO7GadN/oULgAaORiSpxCsQP0m7jhwq2MPWelZHfuxsMvUi8Bjoz/L6q9M784uD6uXTh5/DwId2d5629W86/APsi3CQqYyR8oJlE/oaKkeNUC2xXQPvmYqAFUMfc0bTs6eNw0S2YgyY0i3qVOch3hao+UGuWqJyumHOvmv1BdVdOiaUyRtmLIqZvybtwcEI+Oa1axthKriV98UfFvsObgBdVJqaDkpMSiSKJb6l+H7x7vu4Z0kOUFoKUpymO2UfXIeGqOPrIlOUwsniFLD2ZfvM1IC2wDoQ==",
    }
    request_context = playwright.request.new_context()
    response = request_context.post(url=url,data=request_data)
    assert response.json()['code'] == 200, print('\n',response.json())
    print(response.url)
    print(response.headers.values())
    print(response.status_text)
    print(response.text())
    print(response.headers_array)
    with open('../config/api_headers.json', 'w') as file:
        json.dump(response.headers.get('set-cookie').split(';')[0], file)









