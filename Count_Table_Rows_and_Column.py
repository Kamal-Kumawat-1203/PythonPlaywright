from playwright.sync_api import Page 

def test_count_tables_row_and_column(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(1000)

    # Moving the page 
    page.mouse.wheel(1300, 1700)
    page.wait_for_timeout(2000)

    # Counting the number of columns
    cols = page.locator("//div/div/table[@name='BookTable']/tbody/tr/th").count()
    print("\nTotal colums are:",cols)

    # Counting the number of rows 
    rows = page.locator("//div/div/table[@name='BookTable']/tbody/tr").count()
    print("Total rows are:",rows)

    text = page.locator("#HTML1 > div.widget-content > table > tbody > tr:nth-child(3) > td:nth-child(1)")
    
    # Applying a basic assertion 
    expect(text).to_contain_text("Learn Java")
    print(text.inner_text())
    print("assertion passed")
