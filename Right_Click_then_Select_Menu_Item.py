from playwright.sync_api import Page

def test_right_click_then_select_menu_item(page):
    page.goto("https://deluxe-menu.com/popup-mode-sample.html")
    page.wait_for_timeout(1500)
    
    page.locator("//html/body/div[1]/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td[3]/p[2]/img").click(button="right")
    page.wait_for_timeout(1000)
    
    page.locator("//*[@id='dm2m1i1tdT']").hover()
    page.wait_for_timeout(1000)
    
    page.locator("//*[@id='dm2m2i1tdT']").hover()
    page.wait_for_timeout(1000)
    
    page.locator("//*[@id='dm2m3i1tdT']").hover()
    page.wait_for_timeout(200)
    
    page.locator("//*[@id='dm2m3i1tdT']").click()
    page.wait_for_timeout(3000)
