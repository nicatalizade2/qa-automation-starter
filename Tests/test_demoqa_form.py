
from playwright.sync_api import Page, expect
def test_demoqa_text_box(page: Page) -> None:
    page.goto("https://demoqa.com/text-box")
    page.get_by_placeholder("Full Name").fill("nico")
    page.get_by_placeholder("name@example.com").fill("nico@gmail.com")
    page.get_by_placeholder("Current Address").fill("baku")
    page.locator("#permanentAddress").fill("sihbasi")
    page.get_by_role("button", name="Submit").scroll_into_view_if_needed()
    page.get_by_role("button", name="Submit").click()
    # We check if the result box appears and contains the correct data
    output_name = page.locator("#name")
    expect(output_name).to_be_visible()
    expect(output_name).to_contain_text("Name:nico")

    output_email = page.locator("#email")
    expect(output_email).to_contain_text("Email:nico@gmail.com")

