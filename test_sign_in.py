from selene import browser, be, have

def test_login_with_wrong_password():
        browser.open('https://school.qa.guru/cms/system/login')
        browser.element('.form-field-email[name=email]').type('lady.astashina@yandex.ru')
        browser.element('.form-field-password[name=password]').type('123')
        browser.element('.form-buttons.btn-success').click()
        browser.element('login-form.btn-success.btn-error').should(be.visible).should(be.hidden)



def test_login_with_valid_data():
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('.form-field-email[name=email]').type('lady.astashina@yandex.ru')
    browser.element('.form-field-password[name=password]').type('Df!3103cz')
    browser.element('.form-buttons.btn-success').click()
    browser.element('.header-view').should(have.text('Список тренингов'))