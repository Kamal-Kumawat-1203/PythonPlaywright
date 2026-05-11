def test_uncheck_all_checkboxes_then_check_all(page):
    page.goto("http://www.tizag.com/htmlT/htmlcheckboxes.php")
    checkboxes = page.locator("//div[@class='display'][2]/input[@name='sports']").all()

    for checkbox in checkboxes:
        # if checkbox == check():
        checkbox.uncheck()
        page.wait_for_timeout(200)

    for checkbox in checkboxes:
        checkbox.check()
        page.wait_for_timeout(300)

        # scroll = checkbox.scrollIntoViewIfNeeded()
        page.wait_for_timeout(500)
