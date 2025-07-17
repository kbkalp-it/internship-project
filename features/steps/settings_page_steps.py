from behave import when, then

@when('Change Language to Russian')
def select_language(context):
    context.app.language_setting_page.select_language()

@then('Verify Language is modified')
def verify_language_modified(context):
    context.app.language_setting_page.verify_selected_language()