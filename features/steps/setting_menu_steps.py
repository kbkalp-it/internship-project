from behave import when

@when('Click on the settings option')
def click_settings(context):
    # context.driver.implicitly_wait(3)
    context.app.settings_menu_page.click_settings()