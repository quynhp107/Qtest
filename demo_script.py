import pytest
from playwright.sync_api import Page,expect, sync_playwright


def check_invalid_discount_code(page:Page):
    browser = page.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://plusbase-auto.onshopbase.com/")
    #add to cart
    page.locator("//a[normalize-space()='Shop Now']").click()
    page.locator("//span[@title='(Test product) Auto-cpay1']").click()
    page.locator("//button[@class='btn w-100 btn-outline btn-add-cart shape-sharp-t-l']//span[contains(text(),'Add to cart')]").click()
    #checkout
    page.get_by_role("button", name="checkout").click()
    #apply invalid code and check error message
    page.locator("// input[ @ placeholder = 'Discount code']").fill("abcxyz")
    page.get_by_role("button", name="Apply").click()
    expect(page.locator("//p[@class='field-message field-message--error']")).to_contain_text("Unable to find a valid discount matching the code entered.")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    check_invalid_discount_code(playwright)
