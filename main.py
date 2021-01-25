# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver



def main():
    # Use a breakpoint in the code line below to debug your script.
    # Using Chrome to access web
    driver = webdriver.Chrome()
    # Open the website
    driver.get('https://www.reddit.com/')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # main loop
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


