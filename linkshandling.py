from playwright.sync_api import Page, expect

def test_automationexercise_link_handling(page):
    page.goto("https://www.automationexercise.com/")
    links = page.locator("a")
    total = links.count()
    print(f"Total links are {total}")
    for i in range(total):
        link = links.nth(i)
        try:
            text = link.inner_text()
            url = link.get_attribute("href")
            print(f"{text.strip()} ---- {url}")
        except:
            print(f"Error reading link at index {i}")
    page.wait_for_timeout(8000)

<!-- COde to find and print links on amazon.in -->

def test_amazon_links_handling(page):
    page.goto("https://www.amazon.in/")
    # Applying timeout wait so that Timeout error not accured
    page.wait_for_timeout(5000)
    links = page.locator("a")
    totallinks = links.count()
    # Printing total links number
    print(f"Total links are {totallinks}")
    for i in range(totallinks):
        link = links.nth(i)
        try:
            text = link.inner_text()
            url = link.get_attribute("href")
            print(f"{text.strip()}  -----   {url}")
        except:
            print(f"Facing issue to read URL at index {i}")

    page.wait_for_timeout(3000)
