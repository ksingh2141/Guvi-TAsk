*** Settings ***

Resource    ../resources/keywords.robot

Test Setup       Open SauceDemo
Test Teardown    Close SauceDemo

*** Test Cases ***

Test Case 3 - Add Product To Cart

    Login    ${VALID_USER}    ${VALID_PASSWORD}

    Verify Successful Login

    Add Backpack To Cart

    Open Cart

    Verify Backpack Present


Test Case 4 - Checkout Multiple Products

    Login    ${VALID_USER}    ${VALID_PASSWORD}

    Verify Successful Login

    Add Backpack To Cart

    Add Bike Light To Cart

    Open Cart

    Verify Backpack Present

    Verify Bike Light Present

    Checkout

    Verify Checkout Page