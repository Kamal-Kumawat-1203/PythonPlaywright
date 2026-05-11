from playwright.sync_api import *

def test_file_upload_handling(page):
    page.goto("https://www.way2automation.com/way2auto_jquery/registration.php#load_box")
    page.wait_for_timeout(1000)
    # 1. Filling the First Name and Last Name
    page.locator("//*[@id='register_form']/fieldset[1]/p[1]/input").fill("Kamal")
    page.wait_for_timeout(500)
    page.locator("//*[@id='register_form']/fieldset[1]/p[2]/input").fill("Kumar Kumawat")
    page.wait_for_timeout(500)

    # 2. Selecting the Gender radio button
    page.locator('//*[@id="register_form"]/fieldset[2]/div/label[2]/input').click()
    page.wait_for_timeout(500)

    # 3. Selecting hobby checkbox or all checkboxes

    # page.locator('//*[@id="register_form"]/fieldset[3]/div/label[3]').check()
    # checkboxes.check()
    # page.wait_for_timeout(100)

    checkboxes = page.locator('//*[@id="register_form"]/fieldset[3]/div/label').all()
    # below loop will select all checkboxes in sequence
    for checkbox in checkboxes:
        checkbox.check()
        page.wait_for_timeout(400)
    page.wait_for_timeout(1200)
    #
    # # 4. Selecting DOB
    # selecting Month
    page.locator('//*[@id="register_form"]/fieldset[5]/div[1]/select').click()
    page.select_option("//*[@id='register_form']/fieldset[5]/div[1]/select", value="1")
    page.wait_for_timeout(500)

    # Selecting Day
    page.locator('//*[@id="register_form"]/fieldset[5]/div[2]/select').click()
    page.select_option("//*[@id='register_form']/fieldset[5]/div[2]/select", value="1")
    page.wait_for_timeout(500)

    # Selecting Year
    page.locator('//*[@id="register_form"]/fieldset[5]/div[3]/select').click()
    page.select_option("//*[@id='register_form']/fieldset[5]/div[3]/select", value="2014")
    page.wait_for_timeout(500)

    # 5. Input Mobile Number
    page.locator('//*[@id="register_form"]/fieldset[6]/input').fill('8877665544')
    page.wait_for_timeout(500)

    page.mouse.wheel(105, 300)
    # 6. Enter User Name
    page.locator('//*[@id="register_form"]/fieldset[7]/input').fill('Kamal')
    page.wait_for_timeout(500)

    # 7. Enter E-mail
    page.locator('//*[@id="register_form"]/fieldset[8]/input').fill("testinguser@test.com")
    page.wait_for_timeout(500)

    # 8. Choosing a file
    page.locator('//*[@id="register_form"]/fieldset[9]/input').set_input_files("C:\\Users\\kumaw\\Pictures\\Screenshots\\Screenshot 2026-03-25 165208.png")
    page.wait_for_timeout(500)

    # 9. Filling about your self input area
    page.locator('//*[@id="register_form"]/fieldset[10]/textarea').fill("I am Kamal Kumar Kumawat. I am from Mukundgarh, Rajasthan. Currently, I am learning automation testing."
               "I believe this kill will help me to get new job in Testing field with batter Salary to compare Manual Testing.")
    page.wait_for_timeout(1500)
    page.mouse.wheel(300, 400)

    # 10. Enter password
    page.locator('//*[@id="register_form"]/fieldset[11]/input').fill("testuser")
    page.wait_for_timeout(500)

    # 11. Reenter password in confirm password field
    page.locator('//*[@id="register_form"]/fieldset[12]/input').fill("testuser")
    page.wait_for_timeout(1000)

    # 12. Clicking on Submit button
    page.locator('//*[@id="register_form"]/fieldset[13]/input').click()

    page.wait_for_timeout(2000)

