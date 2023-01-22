from selene.support.shared import browser
from selene import be, have, command
import os

picture_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'photo', 'wepk.jpeg'))

def test_filling_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Ksenia')
    browser.element('#lastName').type('Kapranova')
    browser.element('#userEmail').type('ksenya14039@mail.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type(9973655228)
    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="9"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1997"]').click()
    browser.element('.react-datepicker__day--009').click()
    browser.element('#subjectsInput').should(be.blank).type('English').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()

    browser.element('#uploadPicture').send_keys(picture_path)

    browser.element('#currentAddress').type('Moscow')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').press_enter()

    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Ksenia Kapranova',
        'ksenya14039@mail.ru',
        'Female',
        '9973655228',
        '9 October,1997',
        'English',
        'Reading',
        'wepk.jpeg',
        'Moscow',
        'NCR Noida'
    ))