import time

from lxml.html.diff import token
from playwright.sync_api import sync_playwright,Playwright,Page,expect
from config import api_token_data


def test_search(playwright: Playwright):
    """
    查询
    :return:
    """
    url = 'https://test-tooduduitem.ptdplat.com/search?q=%E6%B6%82%E6%96%99'
    request_data = {
        'q': '涂料',
        'brandId':None,
        'catId': None,
        '_time': time.time()
    }
    token = api_token_data.login_token()
    print(token)
    headers = {
        "Authorization": f"Bearer {token}",
    }
    request_context = playwright.request.new_context()

    response = request_context.get(url=url, headers=headers)
    assert response.ok
    # assert response.json()['code'] == 200
    print(response)

