*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  karvakasa  karvakasa1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  karvakasa  karvakasa1
    Input Credentials  karvakasa  karvakasa1
    Output Should Contain  User with username karvakasa already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  karvakasa1
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  karvakasa  ka1
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  karvakasa  karvakasa
    Output Should Contain  Password has invalid characters
