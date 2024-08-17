from selene import browser, be, have

def test_login_with_wrong_password():
        browser.open('https://school.qa.guru/cms/system/login')
        browser.element('.form-field-email[name=email]').type('lady.astashina@yandex.ru')
        browser.element('.form-field-password[name=password]').type('wrongpassword')
        browser.element('#xdget33092_1').click()
        browser.element('login-form.btn-success.btn-error').should(be.visible)
        browser.element('login-form.btn-success.btn-error').with_(timeout=6).should(be.hidden)
