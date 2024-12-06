import time

from playwright.sync_api import sync_playwright,Playwright,expect


def test_playwright(playwright: Playwright)->None:
    browser =  playwright.chromium.launch(headless=False, channel='chrome')
    context = browser.new_context(
        viewport={'width': 1440, 'height': 900},
        storage_state='../../config/ui_login_data.json'
    )
    page = context.new_page()
    page.goto('https://test-toodudumember.ptdplat.com/#/ucenter/order/index')
    page.locator("xpath=//*[@id='name']").fill('a s s ')
    time.sleep(50)

    browser.close()
    context.close()

