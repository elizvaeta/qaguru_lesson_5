import os

from selene import browser, be, have, by


def test_success_submit():
    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('Elizaveta').should(have.value('Elizaveta'))
    browser.element('#lastName').should(be.blank).type('Kazova').should(have.value('Kazova'))
    browser.element('#userEmail').should(be.blank).type('test@test.com').should(have.value('test@test.com'))
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('9997776655').should(have.value('9997776655'))

    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__month-select").click().element(by.text('September')).click()
    browser.element(".react-datepicker__year-select").click().element(by.text('1999')).click()
    browser.element('.react-datepicker__day--007').click()

    browser.element('#subjectsInput').should(be.blank).type('Maths').should(have.value('Maths')).press_enter()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../files/test.jpg'))
    browser.element('#currentAddress').should(be.blank).type('Russia').should(have.value('Russia'))
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
