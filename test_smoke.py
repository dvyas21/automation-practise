import re
from playwright.sync_api import Playwright, sync_playwright, expect


#other - help - submit
#change my address - save - resume - submit
#any or none - delete - delete & restart

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://stage-col-myaccount.hubsmartcoverage.ca/")
    page.get_by_role("textbox", name="Email Address").click()
    page.get_by_role("textbox", name="Email Address").fill("csgwebapps.qa+dwija-test@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("testing")
    page.get_by_test_id("submit").click()
    page.locator("div").filter(has_text=re.compile(r"^Policy detailsPink Slip$")).get_by_test_id("driver-policy--0").click()
    page.get_by_role("link", name="HUB SmartCoverage Masthead").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Download pink slip").click()
    page1 = page1_info.value
    page1.close()
    page.locator("div").filter(has_text=re.compile(r"^User IconLAURA P CIVICHINOPolicy number: A97176903PLAPolicy details$")).get_by_test_id("driver-policy--0").click()
    page.get_by_role("link", name="HUB SmartCoverage Masthead").click()
    page.get_by_test_id("hab-policy--0").click()
    page.get_by_role("link", name="HUB SmartCoverage Masthead").click()
    page.get_by_test_id("nav").click()
    page.get_by_text("Make a Request Arrow Icon").click()
    page.get_by_test_id("get-a-quote").click()
    page.locator("label").filter(has_text="Other").click()
    page.get_by_test_id("start-request").click()
    page.get_by_role("textbox", name="How can we help you today?").click()
    page.get_by_role("textbox", name="How can we help you today?").fill("abc")
    page.get_by_test_id("manage").click()
    page.get_by_test_id("Save").click()
    page.get_by_role("link", name="Resume").click()
    page.get_by_test_id("submit").click()
    page.get_by_role("link", name="Account Summary").click()
    page.get_by_test_id("nav").click()
    page.get_by_text("Make a Request Arrow Icon").click()
    page.get_by_test_id("make-a-change").click()
    page.get_by_role("button", name="Continue").click()
    page.locator("label").filter(has_text="Cancel my Policy").click()
    page.get_by_test_id("start-request").click()
    page.get_by_test_id("continue").click()
    page.locator("label").filter(has_text="LAURA P CIVICHINO").click()
    page.get_by_test_id("23").click()
    page.get_by_test_id("manage").click()
    page.get_by_role("button", name="Delete and restart").click()
    page.get_by_role("button", name="Cancel").click()
    page.get_by_test_id("continue").click()
    page.get_by_test_id("manage").click()
    page.get_by_role("button", name="Delete and restart").click()
    page.get_by_role("button", name="Restart", exact=True).click()
    page.get_by_test_id("ask-a-question").click()
    page.get_by_role("button", name="Continue").click()
    page.locator("label").filter(has_text="General Question").click()
    page.get_by_test_id("start-request").click()
    page.get_by_text("TOYOTA RAV4 LE 4DR AWD").click()
    page.get_by_text("P27840998HAB").click()
    page.get_by_role("textbox", name="How can we help you today?").click()
    page.get_by_role("textbox", name="How can we help you today?").fill("xyz")
    page.get_by_test_id("continue").click()
    page.locator("label").filter(has_text="Phone Call").click()
    page.get_by_role("textbox", name="Phone Number").click()
    page.get_by_role("textbox", name="Phone Number").fill("3456789090")
    page.get_by_test_id("submit").click()
    page.get_by_test_id("make-request").click()
    with page.expect_popup() as page2_info:
        page.get_by_test_id("view-other-offers").click()
    page2 = page2_info.value
    page2.close()
    page.get_by_text("HUB SmartCoverageMastheadFRMake a Requestmenu").click()
    page.get_by_test_id("nav").click()
    page.get_by_test_id("profile").click()
    page.get_by_test_id("nav").click()
    page.get_by_test_id("claims").click()
    page.get_by_test_id("nav").click()
    page.get_by_test_id("help").click()
    page.get_by_role("link", name="My policy information is").click()
    page.get_by_test_id("nav").click()
    page.get_by_test_id("contact").click()
    page.get_by_test_id("nav").click()
    page.get_by_test_id("disclosures").click()
    with page.expect_popup() as page3_info:
        page.get_by_text("Information IconPrivacy Policy").click()
    page3 = page3_info.value
    page3.close()
    page.get_by_role("button", name="FR").click()
    page.get_by_test_id("nav").click()
    page.get_by_test_id("logout").click()
    page.get_by_role("link", name="Aller à l’accueil").click()
    page.get_by_role("button", name="EN", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
