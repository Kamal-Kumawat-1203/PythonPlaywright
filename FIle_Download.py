import os.path

from playwright.sync_api import Page

def test_file_downloader(page):
    page.goto("https://www.selenium.dev/downloads/")
    page.wait_for_timeout(1500)
    page.mouse.wheel(550, 650)
    page.wait_for_timeout(2000)

    # with page.expect_download() as download_info:
    #     page.locator('/html/body/div[1]/main/div[4]/div[2]/div/div/p[1]/a').click()

    with page.expect_download() as download_info:
        # Use text-based locator instead of a brittle XPath
        page.locator("a[href*='selenium-server']").first.click()

    download = download_info.value

    # project_directory = os.path.join(os.path.dirname(os.getcwd()), "downloads")

    # # If we run the test with the upper line, the downloads folder will be created outside the working directory (PlaywrightLearning) folder
    # # OS is a library
    # # getcwd is the current working directory

                                                # or

    # If I run the test with the below code line, it will create the folder just above the working directory
    project_directory = os.path.join(os.getcwd(), "downloads")

    os.makedirs(project_directory, exist_ok=True)

    # Save file with original suggested name
    file_path = os.path.join(project_directory, download.suggested_filename)

                # or

    # file_path = os.path.join(project_directory, "selenium.jar")

    # # Upper code is the file path
    # # In the upper code line, we are setting the filename forcefully

    download.save_as(file_path)

    print(f"file downloaded successfully: {file_path}")


