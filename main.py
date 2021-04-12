from time import sleep
from typing import Callable

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from qes_report import QesReportTableNames, QesReport

landing_page_url = "https://www.jpmorganindices.com/indices/landing"


def get_qes_report_elements(browser: WebDriver):
    """
    Gets the list of Position Report Elements such as:
    09 Apr 2021 Position Report.html.
    :param browser:
    :return: list of elements
    """
    go_from_landing_page_to_qes_reports_page(browser)

    position_report_elements = browser.find_elements_by_partial_link_text("Position Report")
    return position_report_elements


def go_from_landing_page_to_qes_reports_page(browser: WebDriver):
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
        ec.presence_of_element_located((By.LINK_TEXT, "Indices"))
    )
    indices_btn.click()

    def click_qes_checkbox():
        qes_checkbox = browser.find_element_by_xpath("//label[@for='family_QES']")
        qes_checkbox.click()

    attempt_func_num_times(click_qes_checkbox, 5)

    jpmorgan_us_qes_momentum_series_2_link = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.LINK_TEXT, "J.P. Morgan US QES Momentum Series 2"))
    )
    jpmorgan_us_qes_momentum_series_2_link.click()

    # jpmc US QES momentum series 2 html page

    def click_reports_btn():
        reports_btn = browser.find_element_by_xpath('//li[text()="Reports"]')
        reports_btn.click()

    attempt_func_num_times(click_reports_btn, 5)

    sleep(0.5)


def attempt_func_num_times(the_func: Callable, max_attempts: int):
    """
    attempts to call the_func once successfully.
    Keeps trying up to max_attempts. Otherwise raises exception.
    :param the_func:
    :param max_attempts:
    :return:
    """
    for attempt_num in range(max_attempts):
        try:
            sleep(2)

            the_func()
        except Exception as ex:
            if attempt_num == max_attempts:
                raise ex

        break


def get_info_from_positon_report(browser: WebDriver, position_elem: WebElement):
    """
    will click into the position_elem, and get the desired info.
    :param browser:
    :param position_elem: Position report element. This will have
    text like "09 Apr 2021 Position Report.html"
    :return: QesReport
    """
    position_elem.click()

    sleep(1)

    browser.switch_to.window(browser.window_handles[-1])
    print("tab title:", browser.title)

    main_div = browser.find_element_by_css_selector(".starter-template")
    children_elems = main_div.find_elements_by_css_selector("*")

    qes_report = QesReport()

    next_table_name = None
    for element in children_elems:
        # print(element.tag_name, ":", element.text)

        if QesReportTableNames.daily_performance.value in element.text:
            next_table_name = QesReportTableNames.daily_performance
        elif QesReportTableNames.strategy_detail.value in element.text:
            next_table_name = QesReportTableNames.strategy_detail
        elif QesReportTableNames.indicative_next_day.value in element.text:
            next_table_name = QesReportTableNames.indicative_next_day

        # parse table
        if element.tag_name == "table":
            table_array = parse_table(element)

            if next_table_name == QesReportTableNames.daily_performance:
                qes_report.daily_performance_table = table_array
            elif next_table_name == QesReportTableNames.strategy_detail:
                qes_report.strategy_detail_table = table_array
            elif next_table_name == QesReportTableNames.indicative_next_day:
                qes_report.indicative_next_day_table = table_array

            next_table_name = None  # parse one section only once

    return qes_report


def parse_table(element: WebElement):
    """
    reads a table WebElement and crams it into a 2d array.
    :param element:
    :return: 2d array of a table. 0th row is the header. The rest are data rows.
    """

    table_data = []

    # parse header columns
    header = []
    header_columns = element.find_elements_by_css_selector("thead tr th")
    for column in header_columns:
        header.append(column.text)

    table_data.append(header)

    # parse data
    data_rows_elems = element.find_elements_by_css_selector("tbody tr")
    for data_row_elem in data_rows_elems:
        data_row = []

        children_elems = data_row_elem.find_elements_by_css_selector("*")

        for child_elem in children_elems:
            data_row.append(child_elem.text)

        table_data.append(data_row)

    return table_data


if __name__ == "__main__":
    the_browser = webdriver.Chrome()

    reports_elements = get_qes_report_elements(the_browser)

    # lists all of the dd MMM yyy Position Report.html
    for reports_element in reports_elements:
        print(reports_element.text)

    latest_report_elem = reports_elements[0]
    the_qes_report = get_info_from_positon_report(the_browser, latest_report_elem)

    print(the_qes_report)

    the_browser.close()
