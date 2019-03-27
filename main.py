from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as selEc
from selenium.webdriver.common.by import By as selBy
from selenium.webdriver.support.ui import WebDriverWait
import json, time, threading, random, sys
from modules.spotify import Links as links, XPaths as xpaths


def run(username, password, _url, _headless):

    # Open Chrome and head to playlist link
    options = Options()
    options.headless = _headless
    browser = Chrome(executable_path='drivers/chromedriver.exe', options=options)
    wait = WebDriverWait(browser, 10)
    browser.get(_url) if _url else browser.get(links.default)

    # Login with given credentials
    login_btn = wait.until(selEc.element_to_be_clickable((selBy.XPATH, xpaths.login_btn)))
    login_btn.click()
    user_form = wait.until(selEc.element_to_be_clickable((selBy.XPATH, xpaths.user_form)))
    user_form.send_keys(username)
    pass_form = wait.until(selEc.element_to_be_clickable((selBy.XPATH, xpaths.pass_form)))
    pass_form.send_keys(password)
    cookie_check = wait.until(selEc.element_to_be_clickable((selBy.XPATH, xpaths.cookie_check)))
    cookie_check.click()
    submit_btn = wait.until(selEc.element_to_be_clickable((selBy.XPATH, xpaths.submit_btn)))
    submit_btn.click()

    # Configure shuffle and repeat settings
    shuffle_btn = wait.until(selEc.element_to_be_clickable((selBy.XPATH, xpaths.shuffle_btn)))
    repeat_btn = wait.until(selEc.element_to_be_clickable((selBy.XPATH, xpaths.repeat_btn)))

    # Activate shuffle if disabled
    if "control-button--active" not in shuffle_btn.get_attribute("class"):
        time.sleep(1)
        shuffle_btn.click()

    # Set repeat mode to "playlist"
    if "spoticon-repeat-16 control-button--active" in repeat_btn.get_attribute("class"):
        pass
    elif "spoticon-repeatonce-16 control-button--active" in repeat_btn.get_attribute("class"):
        time.sleep(1)
        repeat_btn.click()
        time.sleep(1)
        repeat_btn.click()
    else:
        time.sleep(1)
        repeat_btn.click()

    # Start playing
    play_btn = wait.until(selEc.element_to_be_clickable((selBy.XPATH, xpaths.play_btn)))
    play_btn.click()
    while True:
        time.sleep(random.randint(55, 70))
        song_name = wait.until(selEc.presence_of_element_located((selBy.XPATH, xpaths.song_name))).text
        time_track = wait.until(selEc.presence_of_element_located((selBy.XPATH, xpaths.time_track))).text
        print(" * Played {0} for {1}".format(song_name, time_track))
        skip_btn = wait.until(selEc.element_to_be_clickable((selBy.XPATH, xpaths.skip_btn)))
        skip_btn.click()


def init():
    print(r"""
      _____             _   _ _____       ____        _     __   ___  
     / ____|           | | (_)  __ \     |  _ \      | |   /_ | / _ \ 
    | (___  _ __   ___ | |_ _| |__) |   _| |_) | ___ | |_   | || | | |
     \___ \| '_ \ / _ \| __| |  ___/ | | |  _ < / _ \| __|  | || | | |
     ____) | |_) | (_) | |_| | |   | |_| | |_) | (_) | |_   | || |_| |
    |_____/| .__/ \___/ \__|_|_|    \__, |____/ \___/ \__|  |_(_)___/ 
           | |                       __/ |                            
           |_|                      |___/""")

    print("\n * Bot started.")
    selUrl = input(" * Insert Spotify playlist url (empty for default): ")
    headless = "--headless" in sys.argv
    with open('data/profiles.json', 'r') as f:
        credentials = json.load(f)
        print(" * Opening browsers...")
        for data in credentials['credentials']:
            threading.Thread(target=run, args=[data['username'], data['password'], selUrl, headless]).start()
            time.sleep(1)
        f.close()


if __name__ == '__main__':
    init()
