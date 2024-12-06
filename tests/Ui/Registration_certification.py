from time import sleep
import random
from playwright.sync_api   import sync_playwright, expect, Playwright


def test_Sign_in(playwright: Playwright)->None:
    browser = playwright.chromium.launch(channel='chrome', headless=False)
    context = browser.new_context(viewport={'width': 1440, 'height': 900}, storage_state={})
    page = context.new_page()
    page.goto('https://test-toodudu.ptdplat.com/user.html')

    page.locator("xpath=/html/body/div/div[3]/div/div[2]/div[4]/a[2]").click()
    page.locator("xpath=//input[@class='msn']").fill(f'Ilikechrome')
    page.locator("xpath=//input[@class='user_contacts']").fill('李龙威')
    page.locator("xpath=//input[@placeholder='请输入部门名称']").fill('技术部')
    page.locator("xpath=//input[@readonly='readonly']").click()
    page.locator("xpath=/html/body/div[3]/div[1]/div[1]/ul/li[2]/span").click()
    page.locator("xpath=//input[@class='pwd']").fill('a123456')
    page.locator("xpath=//input[@class='repwd']").fill('a123456')
    page.locator("xpath=//*[@id='phone']").fill(f'185{random.randint(10000000, 100000000)}')
    # input_phone = page.locator("xpath=//*[@id='phone']")
    # PHONE = input_phone.first.input_value()
    page.locator("xpath=//*[@id='pcode']").fill('000000')
    page.locator("xpath=//*[@id='register_agreement']").click()
    sleep(1)
    page.locator("xpath=//*[@id='ureg']").click()
    sleep(1)
    browser.close()
    context.close()

def test_authentication(playwright: Playwright)->None:
    browser = playwright.chromium.launch(channel='chrome', headless=False)
    context = browser.new_context(
        viewport={'width': 1440, 'height': 900},
        storage_state='../../config/ui_login_data.json'
        )
    page = context.new_page()
    page.goto('https://test-toodudumember.ptdplat.com/#/ucenter')
    sleep(3)
