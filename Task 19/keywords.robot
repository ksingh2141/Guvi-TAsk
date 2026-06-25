*** Settings ***
Library    SeleniumLibrary
Variables  ../variables/variables.py

*** Keywords ***

Open Browser To Application
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Set Selenium Timeout    10s

Login To Application
    [Arguments]    ${username}    ${password}

    Input Text      id:username    ${username}
    Input Password  id:password    ${password}
    Click Button    xpath://button[@type='submit']

Verify Login Successful
    Wait Until Element Is Visible
    ...    id:firstname
    ...    10s

Fill Sales Form
    Input Text      id:firstname      John
    Input Text      id:lastname       Smith

    Select From List By Value
    ...    id:salestarget
    ...    50000

    Input Text      id:salesresult    60000

Submit Sales Form
    Click Button
    ...    xpath://button[contains(text(),'Submit')]

Verify Sales Form Submitted
    Wait Until Page Contains
    ...    Home
    ...    10s

Logout From Application
    Click Button
    ...    xpath://button[contains(.,'Log out')]

Close Browser Session
    Close Browser