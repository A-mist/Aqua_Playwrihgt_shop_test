from time import sleep

from playwright.sync_api import Playwright, sync_playwright


def test_run_playwright(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False, channel='chrome')
    context = browser.new_context(
        viewport={'width': 1900, 'height': 1060}
    )
    page = context.new_page()

    page.goto('https://test-toodudu.ptdplat.com/user.html')
    page.locator("xpath=//*[@id='name']").fill('李龙威')
    page.locator("xpath=//*[@id='password']").fill('a123456')
    page.locator("xpath=//*[@id='password-login']").click()
    sleep(6)
    context.storage_state(path='../config/ui_login_data.json')
    browser.close()
    context.close()


