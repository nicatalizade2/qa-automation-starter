from playwright.sync_api import Page, expect
def test_homepage_title(page: Page):
    page.goto('https://demoqa.com/')
    expect(page).to_have_title("DEMOQA")

def test_elements_menu_visible(page: Page):
    page.goto('https://demoqa.com/')
    elements_card = page.get_by_text("Elements")
    expect(elements_card).to_be_visible()

def test_textbox_submit_shows_name(page: Page):
    page.goto("https://demoqa.com/text-box")

    page.fill("#userName", "Test User")
    page.fill("#userEmail", "test@example.com")
    page.locator("#submit").click()
    result_name = page.locator("#name")
    expect(result_name).to_be_visible()
    expect(result_name).to_contain_text("Test User")


