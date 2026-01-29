from playwright.sync_api import Page, expect


def test_saucedemo(logged_in_page):
    logged_in_page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    logged_in_page.locator("[data-test=\"shopping-cart-link\"]").click()

    logged_in_page.locator("[data-test=\"checkout\"]").click()
    logged_in_page.locator("[data-test=\"firstName\"]").fill("nico alizda")
    logged_in_page.locator("[data-test=\"lastName\"]").fill("alz")
    logged_in_page.locator("[data-test=\"postalCode\"]").fill("02-937")
    logged_in_page.locator("[data-test='continue']").click()

    logged_in_page.locator("[data-test='finish']").click()

    # Verify the success message appears
    header = logged_in_page.locator("[data-test='complete-header']")
    expect(header).to_have_text("Thank you for your order!")
