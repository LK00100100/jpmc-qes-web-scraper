from time import sleep
from typing import Callable

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

landing_page_url = "https://www.jpmorganindices.com/indices/landing"


def get_qes_report_elements(browser: webdriver):
    """
    Gets the list of Position Report Elements such as:
    09 Apr 2021 Position Report.html.
    :param browser:
    :return: list of elements
    """
    go_from_landing_page_to_qes_reports_page(browser)

    position_report_elements = browser.find_elements_by_partial_link_text("Position Report")
    return position_report_elements


def go_from_landing_page_to_qes_reports_page(browser: webdriver):
    """
    will click its way through from the landing page to the QES report page.
    :param browser:
    :return:
    """
    browser.get(landing_page_url)

    select_location_btn = browser.find_element_by_link_text("Select Location")
    select_location_btn.click()

    sleep(0.5)

    non_us_btn = browser.find_element_by_class_name("nonus")
    non_us_btn.click()

    sleep(0.5)

    select_profile_btn = browser.find_element_by_link_text("Select Profile")
    select_profile_btn.click()

    sleep(0.5)

    professional_investor_btn = browser.find_element_by_link_text("Professional Investor")
    professional_investor_btn.click()

    sleep(0.5)

    accept_btn = browser.find_element_by_xpath("//input[@aria-label='Accept']")
    accept_btn.click()

    # next html page
    indices_btn = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Indices"))
    )
    indices_btn.click()

    def click_qes_checkbox():
        qes_checkbox = browser.find_element_by_xpath("//label[@for='family_QES']")
        qes_checkbox.click()

    attempt_func_num_times(click_qes_checkbox, 5)

    jpmorgan_us_qes_momentum_series_2_link = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "J.P. Morgan US QES Momentum Series 2"))
    )
    jpmorgan_us_qes_momentum_series_2_link.click()

    # jpmc US QES momentum series 2 html page

    def click_reports_btn():
        reports_btn = browser.find_element_by_xpath('//li[text()="Reports"]')
        reports_btn.click()

    attempt_func_num_times(click_reports_btn, 5)

    sleep(0.5)


def attempt_func_num_times(the_func: Callable, max_attempts: int):
    for attempt_num in range(max_attempts):
        try:
            sleep(1)

            the_func()
        except Exception as ex:
            if attempt_num == max_attempts:
                raise ex

        break


if __name__ == "__main__":
    the_browser = webdriver.Chrome()

    reports_elements = get_qes_report_elements(the_browser)

    # lists all of the dd MMM yyy Position Report.html
    for reports_element in reports_elements:
        print(reports_element.text)

    the_browser.close()
