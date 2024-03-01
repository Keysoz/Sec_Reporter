#! env/bin/python3

from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time
from datetime import date
import subprocess
from src import banner
from src.banner import Colors
color = Colors()

def get_by_keyword(keyword):
    os.environ['MOZ_HEADLESS'] = '1' # make the Browser runs in the background
    options = webdriver.FirefoxOptions() # Initialize WebDriver
    driver = webdriver.Firefox(options=options)
    scroll_pause_time = 2  # Pause between each scroll
    screen_height = driver.execute_script("return window.screen.height;")  # Browser window height
    i = 1
    count = 1
    # Open the URL of the webpage
    URL = f"https://infosecwriteups.com/tagged/{keyword}"
    driver.get(URL)

    while True:
        # Fetch the data using BeautifulSoup after all data is loaded
        soup = BeautifulSoup(driver.page_source, "html.parser")
        page = soup.find("div", {"class": "js-tagStream"})
        stories = page.find_all("div", {"class": "streamItem streamItem--postPreview js-streamItem"})

        for story in stories:
            name = story.find("div", {"class": "section-inner sectionLayout--insetColumn"}).text
            link = story.find("a", {"class": "button button--smaller button--chromeless u-baseColor--buttonNormal"}).get(
                "href").split("?")
            link = link[0]
            topic_date = story.find("time").get("datetime").split("T")
            topic_date = topic_date[0]
            author = story.find("div", {    
                "class": "postMetaInline postMetaInline-authorLockup ui-captionStrong u-flex1 u-noWrapWithEllipsis"}).text.split(
                "in")
            author = author[0]
            # if topic_date == date.today():
            # if topic_date == "2024-02-14":
            with open("Files/infosec.txt", "a") as infosec_file:
                print(f"{count}", file=infosec_file)
                print(f"Name -> {name}", file=infosec_file)
                print(f"Read More -> {link}", file=infosec_file)
                print(f"Published at -> {topic_date}", file=infosec_file)
                print(f"Written By -> {author}", file=infosec_file)
                print(f"<------------------------------------------->", file=infosec_file)
                infosec_file.close()
                count += 1

        # Scroll down
        driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
        i += 1
        time.sleep(scroll_pause_time/4)

        # Check if reaching the end of the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        if screen_height * i > scroll_height:
            break

    # Close the WebDriver
    driver.quit()
    print(f"\n\n--> ({color.CGREEN2}{count - 1} Write-Ups Was Found{color.ENDC}) <--")
    
def get_by_date():
    os.environ['MOZ_HEADLESS'] = '1' # make the Browser runs in the background
    options = webdriver.FirefoxOptions() # Initialize WebDriver
    driver = webdriver.Firefox(options=options)
    scroll_pause_time = 2  # Pause between each scroll
    screen_height = driver.execute_script("return window.screen.height;")  # Browser window height
    i = 1
    URL = "https://infosecwriteups.com/"
    driver.get(URL)

    while True:
        # Fetch the data using BeautifulSoup after all data is loaded
        soup = BeautifulSoup(driver.page_source, "html.parser")
        page = soup.find("div", class_="u-marginBottom40 js-collectionStream")
        section = page.find("div", {"class":"streamItem streamItem--section js-streamItem"})
        stories = section.find_all("div", class_="row u-marginTop30 u-marginLeftNegative12 u-marginRightNegative12")
        for story in stories:
            name = story.find("div", {"class":"u-letterSpacingTight u-lineHeightTighter u-breakWord u-textOverflowEllipsis u-lineClamp4 u-fontSize30 u-size12of12 u-xs-size12of12 u-xs-fontSize24"}).text
            link = story.find("a", {"class": ""}).get("href").split("?")
            link = link[0]
            topic_date = story.find("time").get("datetime").split("T")
            topic_date = topic_date[0]
            author = story.find("div", {"class": "postMetaInline postMetaInline-authorLockup ui-captionStrong u-flex1 u-noWrapWithEllipsis"})
            author = author.find('a').contents[0]
            if topic_date == str(date.today()):
                with open("Files/infosec.txt", "w") as infosec_file:
                    print(f"Name -> {name}", file=infosec_file)
                    print(f"Read More -> {link}", file=infosec_file)
                    print(f"Published at -> {topic_date}", file=infosec_file)
                    print(f"Written By -> {author}", file=infosec_file)
                    print(f"<------------------------------------------->", file=infosec_file)
                infosec_file.close()
            else:
                with open("Files/infosec.txt", "w") as infosec_file:
                    print(f"{color.CRED2}	No Write-Ups For Today{color.ENDC}", file=infosec_file)
                infosec_file.close()

        # Scroll down
        driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
        i += 1
        time.sleep(scroll_pause_time / 4)

        # Check if reaching the end of the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        if screen_height * i > scroll_height:
            break

    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    banner.main()
    option = int(input(f"    {color.CBLUE2}>{color.ENDC}  "))
    if option == 1:
        get_by_date()
        print(f"\n\n    ----------> ({color.CGREEN2}Done{color.ENDC}) <----------")
    elif option == 2:
        subprocess.run('clear')
        with open("Files/infosec.txt", "w") as writeFile:
            writeFile.close()
        keyword = input(f"  {color.CPURPLE2}>{color.ENDC} Enter The Topic name {color.CPURPLE2}:{color.ENDC} ")
        get_by_keyword(keyword)
    elif option == 3:
        raise SystemExit
    subprocess.run(['cat', 'Files/infosec.txt'])
