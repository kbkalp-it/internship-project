from behave import when

@when('Login to the page')
def login(context):
    context.app.sign_in_page.input_username()
    context.app.sign_in_page.input_password()
    context.app.sign_in_page.click_continue()