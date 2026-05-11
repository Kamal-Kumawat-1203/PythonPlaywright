from playwright.sync_api import Page

def test_way2automation_links_handling(page):
    page.goto("https://www.way2automation.com")
    
    # Locating all links and printing the total number of links 
    links = page.locator("a").all()
    print(f"Total links are: {len(links)}")
    
    # Printing the list of links with available text 
    i=1
    for link in links:
        text = link.inner_text().strip()
        url = link.get_attribute("href")
        print(f"{i}: {text} == {url}")
        i +=1

    page.wait_for_timeout(1000)
