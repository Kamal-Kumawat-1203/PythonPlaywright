from playwright.sync_api import Page 

def test_datepicker_default_function(page):
    page.goto("https://www.way2automation.com/way2auto_jquery/datepicker.php#load_box")
    frame = page.frame_locator('//*[@id="example-1-tab-1"]/div/iframe')
    # frame.locator('//*[@id="datepicker"]').click()
    
    # Clicking on the datepicker textarea 
    datepicker = frame.locator('//*[@id="datepicker"]').click()
    page.wait_for_timeout(2000)
    
    # Inputting the date 
    frame.locator('//*[@id="datepicker"]').fill("12/03/1995")
    page.wait_for_timeout(2000)
