from playwright.sync_api import Page

def test_shadow_dom_using_pierce_selector(page: Page):
    page.goto("https://selectorshub.com/xpath-practice-page/")
    page.wait_for_timeout(2000)

    # ── Playwright uses >>> to pierce Shadow DOM ──
    # Syntax: shadow_host_selector >>> element_inside_shadow
    
    # input_box = page.locator("#userName >>> #kils")
    # input_box.wait_for(state="visible")
    
    input_box1 = page.locator("#pizza")
    input_box1.wait_for(state="visible")
    input_box1.fill("Playwright Shadow DOM Testing")
    
    # input_x = page.get_by_placeholder("Enter pizza name")
    # input_x.wait_for(state="visible")
    # Type text inside Shadow DOM element
    # input_box1.fill("Playwright Shadow DOM")
    
    page.wait_for_timeout(1500)
