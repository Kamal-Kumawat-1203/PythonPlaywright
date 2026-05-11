from playwright.sync_api import Page

def test_Alerts_handling(page):

    def dialog_handler(dialog):
        page.wait_for_timeout(3000)
        print(dialog.message)
        dialog.dismiss()
        # dialog.accept()

    page.on("dialog", dialog_handler)
    page.goto("https://mail.rediff.com/cgi-bin/login.cgi")
    page.locator("//button[@type='submit']").click()
