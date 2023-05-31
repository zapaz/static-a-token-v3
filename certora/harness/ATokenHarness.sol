// SPDX-License-Identifier: BUSL-1.1
pragma solidity 0.8.10;

import {AToken} from "aave-v3-core/contracts/protocol/tokenization/AToken.sol";
import {IPool} from "aave-v3-core/contracts/interfaces/IPool.sol";

contract ATokenHarness is AToken {
    constructor(IPool pool) AToken(pool) {}
}
