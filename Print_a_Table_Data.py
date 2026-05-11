from playwright.sync_api import Page

def test_printing_the_table(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(1000)
    
    # Moving the page 
    page.mouse.wheel(1300, 1700)
    page.wait_for_timeout(2000)
    
    all_inner_text = page.locator("#HTML1 > div.widget-content > table > tbody > tr").all_inner_texts()
    print("\n")
        
    for inner_text in all_inner_text:
        print(inner_text)
        # page.wait_for_timeout(100)
