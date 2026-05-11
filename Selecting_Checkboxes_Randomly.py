def test_selecting_random_checkboxes(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(1000)
    page.mouse.wheel(400, 700)
    page.wait_for_timeout(1000)
    checkboxes = page.locator("//div[@class]/input[@type='checkbox']").all()
    num_to_select = len(checkboxes)//2
    checkboxes_to_select = random.sample(checkboxes, num_to_select)

    for checkbox in checkboxes_to_select:
        checkbox.check()
        page.wait_for_timeout(200)
    page.wait_for_timeout(1200)
