// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;


contract OracleTest {

    event informationRequestEvent();

    string public _information;

    constructor () {
        _information = "";
    }

    function informationRequest() public {
        emit informationRequestEvent();
    }

    function storeInformation(string memory information) public {
        _information = information;
    }

}