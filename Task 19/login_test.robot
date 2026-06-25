*** Settings ***
Resource    ../resources/keywords.robot

Suite Setup       Open Browser To Application
Suite Teardown    Close Browser Session

*** Test Cases ***
Verify Login Submit Sales Form And Logout
    [Documentation]    Verify user can login, submit sales form and logout successfully
    [Tags]    Smoke

    Login To Application    ${USERNAME}    ${PASSWORD}

    Verify Login Successful

    Fill Sales Form
    Submit Sales Form
    Verify Sales Form Submitted

    Logout From Application