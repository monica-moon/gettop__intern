from behave import *

use_step_matcher ( "re" )


@given( "Open Gettop page" )
def open_Gettop_page(context):
    context.app.main_page.open_main()


@when( 'Click on "USER" icon' )
def click_on_user_icon(context):
    context.app.account_icon.page.account_icon.click()

@then( "Verify log in form opens" )
def def verify_login_form_opens(context):
    actual_result = context.driver.find_element (By.CSS_SELECTOR, "woocommerce-form woocommerce-form-login login" ).text
    assert actual_result == expected_result, f'Error {actual_result}, but expected {expected_result}'