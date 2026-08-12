*** Settings ***

Resource    ../resources/keywords.robot

Test Setup       Open SauceDemo
Test Teardown    Close SauceDemo

*** Test Cases ***

Test Case 1 - Valid Login

    Login    ${VALID_USER}    ${VALID_PASSWORD}

    Verify Successful Login

Test Case 2 - Invalid Login

    Login    ${INVALID_USER}    ${INVALID_PASSWORD}

    Verify Login Error