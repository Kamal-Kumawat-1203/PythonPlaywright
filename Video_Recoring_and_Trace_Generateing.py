import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    # context = browser.new_context()

    # # If video recording is not required then comment the line below and uncomment the upper line

    context = browser.new_context(
        record_video_dir="c:/Users/kumaw/PycharmProjects/PlaywrightLearning/testcases/videos/",
        record_video_size={"width": 1920, "height": 1080})  # record_video_size={"width": 3840, "height": 2160}

    # Start tracing before creating/navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.set_viewport_size({"width": 1425, "height": 760})
    yield page
    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="c:/Users/kumaw/PycharmProjects/PlaywrightLearning/testcases/trace/trace.zip")
    page.close()
    context.close()

# ==============================================================================================================================

# Here are the Steps to open trace.zip file

# 1. Open the terminal in PyCharm (Available in the left mid-bottom)
# 2. Enter: cd .\testcases\trace
# Now we are in the trace folder 
# 3. Enter: playwright show-trace trace.zip




