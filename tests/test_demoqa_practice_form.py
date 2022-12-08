from selene.support.shared import browser
from selene import have, be
import os


def test_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Ksenia')
    browser.element('#lastName').type('Kapranova')
    browser.element('#userEmail').type('ksenya@mail.ru')
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').type('79778775778')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="10"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1996"]').click()
    browser.element('.react-datepicker__day--027').click()
    browser.element('#subjectsInput').set_value('Language').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').set_value(os.path.abspath('file/wpek.jpeg'))
    browser.element('#currentAddress').should(be.blank).type('Moscow')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Ksenia Kapranova',
        'ksenya@mail.ru',
        'Female',
        '79778775778',
        '27 October,1996',
        'Language',
        'Reading',
        'wpek.jpeg',
        'Moscow',
        'NCR Noida'))