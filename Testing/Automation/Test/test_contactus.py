from Testing.Automation.Contactus_page.contactus_page import CountactUs
from Testing.Automation.Contactus_page.home_page import Home_page


def test_contactus(driver):
    home = Home_page(driver)
    contact =CountactUs(driver)

    home.click_contact_us()
    contact.name_value()
    contact.email_value()
    contact.phone_value()
    contact.message_value()
    contact.click_sumbit()