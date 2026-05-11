from playwright.sync_api import Page 

def test_price_based_slider_handling(page):
    page.goto("https://www.globalsqa.com/demo-site/sliders/#Range")
    page.wait_for_timeout(1500)

    # Switching to the iframe that is holding the slider
    frame = page.frame_locator('(//p/iframe)[2]')

    # Locating the slider and handles
    slider = frame.locator('//div[@id="slider-range"]')
    left_handle = frame.locator('//*[@id="slider-range"]/span[1]')               # First handle
    right_handle = frame.locator('//*[@id="slider-range"]/span[2]')              # Second handle

    slider_box = slider.bounding_box()
    border_width = 1
    slider_start_x = slider_box["x"] + border_width
    # border_width is mandatory, because, if we remove it, the actual test result will be -1 to compare the expected result
    slider_width = slider_box["width"]

    # Defining sliders' min and max range
    slider_min = 0
    slider_max = 500

    def move_handle(handle, target_value):
        # Calculate the proportional value to move handles
        proportion = (target_value - slider_min) / (slider_max - slider_min)
        target_x = slider_start_x + (proportion * slider_width)

        handle_box = handle.bounding_box()
        current_x = handle_box["x"] + handle_box["width"] / 2
        current_y = handle_box["y"] + handle_box["height"]/2

        # moving handles to the targeted value
        page.mouse.move(current_x, current_y)
        page.mouse.down()
        page.mouse.move(target_x, current_y, steps=30)
        page.mouse.up()

    # Moving handles left to right
    print("\nMoving both handle left to right")
    move_handle(left_handle, 150)
    page.wait_for_timeout(1000)
    move_handle(right_handle, 490)
    page.wait_for_timeout(1000)

    # Moving both handles right to left
    print("\n Moving both handle right to left")
    move_handle(left_handle, 100)
    page.wait_for_timeout(1000)
    move_handle(right_handle, 200)
    page.wait_for_timeout(1500)

