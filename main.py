from random import choice
from threading import Thread
from time import sleep

import browsers

from chrome import Chrome
from common import VIDEO_TITLE_AND_TIME, CHANNEL_NAME, RANDOM_VIDEO_TIME
from enums import BrowserEnum, SearchEnum
from firefox import Firefox
from msedge import Edge


def open_browser(browser_type: BrowserEnum):
    """
    This function is responsible for opening the browser.
    """
    browser_mapping = {
        BrowserEnum.CHROME: Chrome,
        BrowserEnum.FIREFOX: Firefox,
        BrowserEnum.EDGE: Edge
    }

    if browser_type in browser_mapping:
        return browser_mapping[browser_type]()
    else:
        print(f"Unsupported browser type: {browser_type}")
        return None


def get_selected():
    """
    This function is responsible for selecting the title.
    """
    return choice(VIDEO_TITLE_AND_TIME)


def main(
        browser_type: BrowserEnum = BrowserEnum.CHROME
):
    """
    This function is responsible for the main program.
    """
    opened_browser = open_browser(browser_type)

    print("====================================================")
    print("====================================================")
    print("====================================================")
    print("                                                    ")
    print(f"Opened --->>> {browser_type.value}")
    print("                                                    ")
    print("====================================================")
    print("====================================================")
    print("====================================================")

    if opened_browser is None:
        return

    title, time_text = get_selected()

    sleep(5)
    opened_browser.close_other_tabs()
    sleep(2)
    opened_browser.get("https://youtube.com")
    sleep(3)
    opened_browser.search(title)
    sleep(5)
    opened_browser.play_searched_video(time_text, CHANNEL_NAME)
    # opened_browser.searched_video(
    #     " ", choice(CHANNEL_NAMES), SearchEnum.RELATED)
    # sleep(30)
    # opened_browser.mini_player()
    # sleep(5)
    # opened_browser.home()
    # sleep(5)
    # opened_browser.play_searched_video(
    #     RANDOM_VIDEO_TIME, CHANNEL_NAME, SearchEnum.HOME)
    sleep(10)


if __name__ == "__main__":
    browsers_list = list(browsers.browsers())
    skip_browsers = ["msie", "safari", 'chromium']

    for browser in browsers_list:
        if browser["browser_type"] in skip_browsers:
            continue
        Thread(target=main, args=(BrowserEnum(
            browser["browser_type"]),)).start()
        sleep(5)
