def test_print_checkboxes_values(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(1000)

    # Scrolling the page
    page.mouse.wheel(50, 400)
    checkboxes = page.locator("//*[@id='post-body-1307673142697428135']/div[4]/div/label").all()

    print(f"\nTotal values are {len(checkboxes)}")
    for checkbox in checkboxes:
        text = checkbox.inner_text()
        print(text)
    page.wait_for_timeout(1500)
