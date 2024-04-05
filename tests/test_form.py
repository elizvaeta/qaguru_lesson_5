import os

from selene import browser, have, by


def test_success_submit():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Elizaveta')
    browser.element('#lastName').type('Kazova')
    browser.element('#userEmail').type('test@test.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('9997776655')

    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__month-select").click().element(by.text('September')).click()
    browser.element(".react-datepicker__year-select").click().element(by.text('1999')).click()
    browser.element('.react-datepicker__day--007').click()

    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../files/test.jpg'))
    browser.element('#currentAddress').type('Russia')
    browser.element('#state').click().element(by.text('Haryana')).click()
    browser.element('#city').click().element(by.text('Karnal')).click()

    browser.element('#submit').click()

    browser.element('.modal-header').should(have.text("Thanks for submitting the form"))
    browser.element('.table').all('td').even.should(have.exact_texts(
        'Elizaveta Kazova',
        'test@test.com',
        'Female',
        '9997776655',
        '07 September,1999',
        'Maths',
        'Music',
        'test.jpg',
        'Russia',
        'Haryana Karnal'
    )
    )
