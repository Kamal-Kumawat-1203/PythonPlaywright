from playwright.sync_api import Page

def test_frames_handling(page):
    page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit")

    frame = page.frame_locator("//*[@id='iframeResult']")
    frame.locator("//*[@id='fname']").clear()
    frame.locator("//input[@id='fname']").fill("Kamal")
    page.wait_for_timeout(500)

    frame.locator("//input[@id='lname']").clear()
    frame.locator("//input[@id='lname']").fill("Kumar Kumawat")
    page.wait_for_timeout(1000)
    frame.locator("//input[@type='submit']").click()
    page.wait_for_timeout(1500)
