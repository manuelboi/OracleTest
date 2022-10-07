// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;


contract OracleTest {

    event informationRequestEvent();

    string _information;

    constructor () {
        _information = "";
    }

    function getInformation() public view returns (string memory) {
        return _information;
    }

    function setInformation(string memory information) public {
        _information = information;
    }

    function informationRequest() public {
        emit informationRequestEvent();
    }

}