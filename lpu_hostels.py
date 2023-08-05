import winwifi
from playwright.sync_api import sync_playwright
import webbrowser
import time

Id="Your_UMS_ID"
pwd="Your_UMS_Password"

def connect_to_wifi():
    try:
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=False, slow_mo=50)
            page=browser.new_page()
            page.goto('https://internet.lpu.in/24online/webpages/client.jsp')
            page.click('input#agreepolicy')
            page.fill('input[type=text]', Id)
            page.fill('input[type=password]', pwd)
            page.click('button[type=submit]')

            print("successfully connected to LPU Hostels!")

            time.sleep(1)

            # You can also use the below command for the same.

            # webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open_new("10.10.10.1")


    except Exception as e:
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=False, slow_mo=50)
            page=browser.new_page()
            page.goto('https://internet.lpu.in/24online/webpages/client.jsp')
            page.click('input[type=submit]')

            print("wifi already connected!\ndis-connecting previous connection...")
            print("successfully dis-connected...")

            page.click('input#agreepolicy')
            page.fill('input[type=text]', Id)
            page.fill('input[type=password]', pwd)
            page.click('button[type=submit]')

            print("\nsuccessfully re-connected to LPU Hostels!\n")

            time.sleep(1)



try:
    winwifi.WinWiFi.connect("LPU Hostels")
    connect_to_wifi()

except Exception as e:
    print(f'\nError message: {e}')
    print("\nThe site is not responding.\n")
    print("Waiting for the site to load...\n")

    for i in range(30, 0, -1):
        print(i, end=" ")
        time.sleep(1)

    connect_to_wifi()

