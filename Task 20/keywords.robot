*** Settings ***
Library    SeleniumLibrary

Resource    variables.robot
Resource    locators.robot

*** Keywords ***

Open SauceDemo
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    10s

Close SauceDemo
    Close Browser

Login
    [Arguments]    ${user}    ${pass}

    Wait Until Element Is Visible    ${TXT_USERNAME}

    Input Text        ${TXT_USERNAME}    ${user}
    Input Password    ${TXT_PASSWORD}    ${pass}

    Click Button      ${BTN_LOGIN}

Verify Successful Login
    Wait Until Element Is Visible    ${LBL_PRODUCTS}

Verify Login Error
    Wait Until Element Is Visible    ${LBL_ERROR}
    Element Should Contain    ${LBL_ERROR}    Epic sadface

Add Backpack To Cart
    Wait Until Element Is Visible    ${BTN_BACKPACK}
    Click Button    ${BTN_BACKPACK}

Add Bike Light To Cart
    Wait Until Element Is Visible    ${BTN_BIKELIGHT}
    Click Button    ${BTN_BIKELIGHT}

Open Cart
    Wait Until Element Is Visible    ${LNK_CART}
    Click Element    ${LNK_CART}

    Wait Until Element Is Visible    ${BTN_CHECKOUT}

Verify Backpack Present
    Page Should Contain    Sauce Labs Backpack

Verify Bike Light Present
    Page Should Contain    Sauce Labs Bike Light

Checkout

    Click Button    ${BTN_CHECKOUT}

    Wait Until Element Is Visible    ${TXT_FIRSTNAME}

    Input Text    ${TXT_FIRSTNAME}    ${FIRST_NAME}
    Input Text    ${TXT_LASTNAME}     ${LAST_NAME}
    Input Text    ${TXT_POSTAL}       ${ZIP_CODE}

    Click Button    ${BTN_CONTINUE}

Verify Checkout Page
    Wait Until Element Is Visible    ${LBL_SUMMARY}