from playwright.sync_api import Page

def test_moving_slider_on_the_pixel_bases(page):
    page.goto("https://demo.automationtesting.in/Slider.html")
    page.wait_for_timeout(1000)
    
    # Locating the slider 
    slider = page.locator("//*[@id='slider']/a")
    slider.wait_for(state="visible")
    
    bounding_box = slider.bounding_box()
    start_x = bounding_box["x"] + bounding_box["width"] / 2
    start_y = bounding_box["y"] + bounding_box["height"] / 2
    
    # Moving the slider 
    page.mouse.move(start_x, start_y)
    page.mouse.down()
    page.mouse.move(start_x +337.65, start_y, steps=30)      # Steps are used to move the slider smoothly 
    page.mouse.up()
    page.wait_for_timeout(1500)
    
