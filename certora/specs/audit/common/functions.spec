// use invariant totalSupplyIsSumOfBalances
// use invariant noSupplyIfNoAssets
// use invariant vaultSolvency
// use invariant noAssetsIfNoSupply
// use invariant assetsMoreThanSupply

// function safeAssumptions(env e, address receiver, address owner) {
//     require currentContract != asset();
//     requireInvariant totalSupplyIsSumOfBalances();
//     requireInvariant noSupplyIfNoAssets();
//     requireInvariant vaultSolvency(e);
//     requireInvariant noAssetsIfNoSupply(e);
//     requireInvariant assetsMoreThanSupply(e);

//     require ( (receiver != owner => balanceOf(owner) + balanceOf(receiver) <= totalSupply())  &&
//                 balanceOf(receiver) <= totalSupply() &&
//                 balanceOf(owner) <= totalSupply());
// }

/**
* @title Single reward setup
* Setup the `StaticATokenLM`'s rewards so they contain a single reward token
* which is` _DummyERC20_rewardToken`.
*/
function single_RewardToken_setup() {
    require getRewardTokensLength() == 1;
    require getRewardToken(0) == _DummyERC20_rewardToken;
    // OR // require isRegisteredRewardToken(_DummyERC20_rewardToken);
}

/**
* @title Single reward setup in RewardsController
* Sets (in `_RewardsController`) the first reward for `_AToken` as
* `_DummyERC20_rewardToken`.
*/
function rewardsController_reward_setup() {
    require _RewardsController.getAvailableRewardsCount(_AToken) > 0;
    require _RewardsController.getRewardsByAsset(_AToken, 0) == _DummyERC20_rewardToken;
}

/// @title Assumptions that should hold in any run
/// @dev Assume that RewardsController.configureAssets(RewardsDataTypes.RewardsConfigInput[] memory rewardsInput) was called
function setup(env e, address user)
{
    require getRewardTokensLength() > 0;
    require _RewardsController.getAvailableRewardsCount(_AToken)  > 0;
    require _RewardsController.getRewardsByAsset(_AToken, 0) == _DummyERC20_rewardToken;
    require currentContract != e.msg.sender;
    require currentContract != user;

    require _AToken != user;
    require _RewardsController !=  user;
    require _DummyERC20_aTokenUnderlying  != user;
    require _DummyERC20_rewardToken != user;
    require _SymbolicLendingPool != user;
    require _TransferStrategy != user;
    require _TransferStrategy != user;
}

function rewardsController_arbitrary_single_reward_setup() {
    require _RewardsController.getAvailableRewardsCount(_AToken) == 1;
    require _RewardsController.getRewardsByAsset(_AToken, 0) == _DummyERC20_rewardToken;
}

// A helper function to set the receiver
function callReceiverFunctions(method f, env e, address receiver) {
    uint256 amount;
    if (f.selector == deposit(uint256,address).selector) {
        deposit(e, amount, receiver);
    } else if (f.selector == mint(uint256,address).selector) {
        mint(e, amount, receiver);
    } else if (f.selector == withdraw(uint256,address,address).selector) {
        address owner;
        withdraw(e, amount, receiver, owner);
    } else if (f.selector == redeem(uint256,address,address).selector) {
        address owner;
        redeem(e, amount, receiver, owner);
    } else {
        calldataarg args;
        f(e, args);
    }
}

function callContributionMethods(env e, method f, uint256 assets, uint256 shares, address receiver) {
    if (f.selector == deposit(uint256,address).selector) {
        deposit(e, assets, receiver);
    }
    if (f.selector == mint(uint256,address).selector) {
        mint(e, shares, receiver);
    }
}

function callReclaimingMethods(env e, method f, uint256 assets, uint256 shares, address receiver, address owner) {
    if (f.selector == withdraw(uint256,address,address).selector) {
        withdraw(e, assets, receiver, owner);
    }
    if (f.selector == redeem(uint256,address,address).selector) {
        redeem(e, shares, receiver, owner);
    }
}
