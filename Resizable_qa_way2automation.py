from playwright.sync_api import Page 

def test_qaway2automantion_web_resizable_gesture(page):
    page.goto("https://www.way2automation.com/way2auto_jquery/resizable.php#load_box")

    # Switching to the iframe
    frame = page.frame_locator("//*[@id='example-1-tab-1']/div/iframe")
    
    # Switching to the resizable as per the iframe 
    resizable = frame.locator("//*[@id='resizable']")
    # resizable.scroll_into_view_if_needed()
    page.wait_for_timeout(2000)
    resizable.wait_for(state="visible")
    # page.wait_for_timeout(1000)
    bounding_box = resizable.bounding_box()
    start_x = bounding_box["x"] + bounding_box["width"] -5
    start_y = bounding_box["y"] + bounding_box["height"] -5 
    # Resize handle zones are typically 5-10px wide around element borders in jQuery UI resizables. 
    # If we change it to +5 or remove the code will not work
    
    # Resizing the textarea
    page.mouse.move(start_x, start_y)
    page.mouse.down()
    page.mouse.move(start_x+200, start_y+200, steps=30)
    page.mouse.up()
    page.wait_for_timeout(2000)

