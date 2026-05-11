from playwright.sync_api import Page 

def test_upload_multiple_files(page):
    page.goto("https://www.w3schools.com/jsreF/tryit.asp?filename=tryjsref_fileupload_multiple")
    page.wait_for_timeout(1000)

    # Locating the iFrame
    frame = page.frame_locator('//*[@id="iframeResult"]')

    # Selecting files
    frame.locator('//*[@id="myFile"]').set_input_files([
        "C:\\Users\\kumaw\\Pictures\\Screenshots\\Screenshot 2026-03-25 165208.png",
        "C:\\Users\\kumaw\\Pictures\\Screenshots\\Screenshot 2026-03-15 082338.png"
    ])
    page.wait_for_timeout(3000)
    
