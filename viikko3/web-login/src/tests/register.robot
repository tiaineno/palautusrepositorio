*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  samikzn
    Set Password  sami1234
    Set Password Confirmation  sami1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  sa
    Set Password  sami1234
    Set Password Confirmation  sami1234
    Submit Credentials
    Register Should Fail With Message  Username must be atleast 3 characters long

Register With Valid Username And Too Short Password
    Set Username  samikzn
    Set Password  sami123
    Set Password Confirmation  sami123
    Submit Credentials
    Register Should Fail With Message  Password must be atleast 8 characters long

Register With Valid Username And Invalid Password
    Set Username  samikzn
    Set Password  samisami
    Set Password Confirmation  samisami
    Submit Credentials
    Register Should Fail With Message  Password must contain at least one number or special character

Register With Nonmatching Password And Password Confirmation
    Set Username  samikzn
    Set Password  sami1234
    Set Password Confirmation  sami12345
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  User with username kalle already exists

Login After Successful Registration
    Set Username  samikzn
    Set Password  sami1234
    Set Password Confirmation  sami1234
    Submit Credentials
    Register Should Succeed
    Go To Ohtu Page
    Click Button  Logout
    Login With Correct Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  samikzn
    Set Password  sami1
    Set Password Confirmation  sami1
    Submit Credentials
    Register Should Fail With Message  Password must be atleast 8 characters long
    Go To Login Page
    Login With Correct Credentials
    Login Should Fail With Message  Invalid username or password
    

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Login With Correct Credentials
    Set Username  samikzn
    Set Password  sami1234
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
