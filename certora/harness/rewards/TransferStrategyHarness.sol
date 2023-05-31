pragma solidity ^0.8.10;

import {IERC20} from "../../../lib/aave-v3-core/contracts/dependencies/openzeppelin/contracts/IERC20.sol";
import {TransferStrategyBase} from
    "../../../lib/aave-v3-periphery/contracts/rewards/transfer-strategies/TransferStrategyBase.sol";

contract TransferStrategyHarness is TransferStrategyBase {
    constructor(address incentivesController, address rewardsAdmin)
        TransferStrategyBase(incentivesController, rewardsAdmin)
    {}

    IERC20 public REWARD;

    // executes the actual transfer of the reward to the receiver
    function performTransfer(address to, address reward, uint256 amount)
        external
        override(TransferStrategyBase)
        returns (bool)
    {
        require(reward == address(REWARD));
        return REWARD.transfer(to, amount);
    }
}
