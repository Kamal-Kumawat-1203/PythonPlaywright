from playwright.sync_api import Page 

def test_select_datepicker_values_using_while_loop(page):
    page.goto("https://www.way2automation.com/way2auto_jquery/datepicker.php#load_box")
    page.wait_for_timeout(1000)
    frame = page.frame_locator('//*[@id="example-1-tab-1"]/div/iframe')
    frame.locator('//*[@id="datepicker"]').click()
    # prev_button = frame.locator('//*[@id="ui-datepicker-div"]/div/a[1]')
    # values = frame.locator('//*[@id="ui-datepicker-div"]/div/div')

    # Selecting Month and Year
    while True:
        month = frame.locator('//*[@id="ui-datepicker-div"]/div/div/span[1]').inner_text()
        year = frame.locator('//*[@id="ui-datepicker-div"]/div/div/span[2]').inner_text()
        if month == "March" and year == "1995":
            break
        else:
            frame.locator('//*[@id="ui-datepicker-div"]/div/a[1]').click()
            # page.wait_for_timeout(50)

    page.wait_for_timeout(1500)
    # Select the day
    frame.locator("table.ui-datepicker-calendar td a", has_text="12").click()
    page.wait_for_timeout(3000)
