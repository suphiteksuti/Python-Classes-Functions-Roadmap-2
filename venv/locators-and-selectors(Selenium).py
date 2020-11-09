from selenium.webdriver.common.by import By
import time


#1 UTM settings on Newsletter design page
UTM_SETTINGS = (By.ID, 'utmSettings containContentBox')
UTM_SETTINGS_CLICK = (By.CLASS_NAME, 'checkboxDefault')

#2 tags list when we select template in created journey campaign and didn’t click Use this Template button
SELECT_TAG = (By.CSS_SELECTOR, 'div.info > div > span:nth-child(1)')

#3 input warning message, for example, on Journey SMS page when we try to save empty title input
WARNING_MESSAGE = (By.CSS_SELECTOR, 'afieldset > p')

#4 on Journey do list filter input
JOURNEY_FILTER_LIST = (By.NAME'searchValue')

#5 'Test' radio button on smart recommender launch step
TEST_RADIO = (By.ID, 'Test')

#6 on Journey do list how to click exactly needed campaign’s Statistics button if there is more than 1 campaigns in the list
CLICK_STATISTICS = (By.LINK_TEXT, 'tr:nth-child(3) > td.vuetable-slot.statistics > div > div > p')

#7 on Message box design page remove variation cross icon
DELETE_VARIATION = (By.ID, 'delete')

#8 Remove/ Change element buttons on Journey canvas page
REMOVE_CHANGE_ELEMENT = (By.CLASS_NAME, 'elementOption')

#9 Alert toaster on any page of panel
ALERT = (By.CLASS_NAME, 'messageAlertBoxIcon')

#10 on Social Proof ‘Create New Personalization’
CREATE_NEW_ERS = (By.CSS_SELECTOR, 'div.personalization > div:nth-child(1) > div > a')
