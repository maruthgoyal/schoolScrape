from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from constants import *

driver = webdriver.Chrome()

def main():

    regno = '5858700'

    while int(regno) < MAX_ROLL_NO:

        try:
            driver.get(URL)

            student_no_login = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr[1]/td[2]/input")

            school_no_login = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr[2]/td[2]/input")


            student_no_login.send_keys(regno)
            school_no_login.send_keys(SCHOOL_CODE)

            school_no_login.send_keys(Keys.RETURN)



            assert (not(("Result Not Found" in driver.page_source)) and not(("Access denied" in driver.page_source)))



            english_name = driver.find_element_by_xpath(ENGLISH_NAME_XPATH).text

            phy_name = driver.find_element_by_xpath(PHY_NAME_XPATH).text

            chem_name = driver.find_element_by_xpath(CHEM_NAME_XPATH).text

            math_name = driver.find_element_by_xpath(MATH_NAME_XPATH).text


            if english_name == "ENGLISH CORE":

                marks = int(filter(str.isdigit, str(driver.find_element_by_xpath(ENGLISH_MARK_XPATH).text)))

                with open(ENGLISH_FILE_PATH, 'a') as f:
                    f.write(str(marks) + "\n")

            if phy_name == "PHYSICS":

                marks = int(filter(str.isdigit, str(driver.find_element_by_xpath(PHY_MARK_XPATH).text)))

                with open(PHYSICS_FILE_PATH, 'a') as f:
                    f.write(str(marks) + "\n")

            if chem_name == "CHEMISTRY":

                marks = int(filter(str.isdigit, str(driver.find_element_by_xpath(CHEM_MARK_XPATH).text)))

                with open(CHEMISTRY_FILE_PATH, 'a') as f:
                    f.write(str(marks) + "\n")

            if math_name == "MATHEMATICS":

                marks = int(filter(str.isdigit, str(driver.find_element_by_xpath(MATH_MARK_XPATH).text)))

                with open(MATH_FILE_PATH, 'a') as f:
                    f.write(str(marks) + "\n")

        except AssertionError:
            print "NO RESULT"

        regno = str(int(regno) + 1)

if __name__ == '__main__':
    main()
