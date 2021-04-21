*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  karvakasa
    Set Password  karvakasa1
    Set Password Confirmation  karvakasa1
    Submit Register Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  karvakasa1
    Set Password Confirmation  karvakasa1
    Submit Register Credentials
    Page Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Set Username  karvakasa
    Set Password  karva1
    Set Password Confirmation  karva1
    Submit Register Credentials
    Page Should Contain  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  karvakasa
    Set Password  karvakasa1
    Set Password Confirmation  karva1
    Submit Register Credentials
    Page Should Contain  Passwords do not match

Login After Successful Registration
    Set Username  karvakasa
    Set Password  karvakasa1
    Set Password Confirmation  karvakasa1
    Submit Register Credentials
    Go To Login Page
    Set Username  karvakasa
    Set Password  karvakasa1
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  karvakasa
    Set Password  karva
    Set Password Confirmation  karvakasa1
    Submit Register Credentials
    Go To Login Page
    Set Username  karvakasa
    Set Password  karva
    Submit Credentials
    Page Should Contain  Invalid username or password

*** Keywords ***
Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Submit Register Credentials
    Click Button  Register

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Login Should Succeed
    Main Page Should Be Open