// SPDX-License-Identifier: agpl-3.0
pragma solidity ^0.8.10;

import {StaticATokenLM, StaticATokenErrors,  IPool, IRewardsController, IERC20} from '../../src/StaticATokenLM.sol';
import {SymbolicLendingPool} from './pool/SymbolicLendingPool.sol';
import {DataTypes, ReserveConfiguration} from '../../lib/aave-v3-core/contracts/protocol/libraries/configuration/ReserveConfiguration.sol';

contract StaticATokenLMHarness is StaticATokenLM {
    struct SignatureParamsHarness {
        uint8 v;
        bytes32 r;
        bytes32 s;
    }

    struct PermitParamsHarness {
        address owner;
        address spender;
        uint256 value;
        uint256 deadline;
        uint8 v;
        bytes32 r;
        bytes32 s;
    }

    address internal _reward_A;
    address internal _reward_B;

    constructor(IPool pool, IRewardsController rewardsController) StaticATokenLM(pool, rewardsController) {}

    // returns the address of the underlying asset of the static aToken
    function getStaticATokenUnderlying() public view returns (address) {
        return _aTokenUnderlying;
    }

    // returns the address of the i-th reward token in the reward tokens list maintained by the static aToken
    function getRewardToken(uint256 i) external view returns (address) {
        return _rewardTokens[i];
    }

    // returns the length of the reward tokens list maintained by the static aToken
    function getRewardTokensLength() external view returns (uint256) {
        return _rewardTokens.length;
    }

    // returns a user's reward index on last interaction for a given reward
    function getRewardsIndexOnLastInteraction(address user, address reward) external view returns (uint128) {
        UserRewardsData memory currentUserRewardsData = _userRewardsData[user][reward];
        return currentUserRewardsData.rewardsIndexOnLastInteraction;
    }

    // returns the reward's index value on last update
    function getLastUpdatedIndex(address reward) public view returns (uint248) {
        return _startIndex[reward].lastUpdatedIndex;
    }

    // claims rewards for a user on the static aToken.
    // the method builds the rewards array with a single reward and calls the internal claim function with it
    function claimSingleRewardOnBehalf(address onBehalfOf, address receiver, address reward) external {
        require(reward == _reward_A);
        address[] memory rewards = new address[](1);
        rewards[0] = _reward_A;

        // @MM - think of the best way to get rid of this require
        require(
            msg.sender == onBehalfOf || msg.sender == INCENTIVES_CONTROLLER.getClaimer(onBehalfOf),
            StaticATokenErrors.INVALID_CLAIMER
        );
        _claimRewardsOnBehalf(onBehalfOf, receiver, rewards);
    }

    // claims rewards for a user on the static aToken.
    // the method builds the rewards array with 2 identical rewards and calls the internal claim function with it
    function claimDoubleRewardOnBehalfSame(address onBehalfOf, address receiver, address reward) external {
        require(reward == _reward_A);
        address[] memory rewards = new address[](2);
        rewards[0] = _reward_A;
        rewards[1] = _reward_A;

        require(
            msg.sender == onBehalfOf || msg.sender == INCENTIVES_CONTROLLER.getClaimer(onBehalfOf),
            StaticATokenErrors.INVALID_CLAIMER
        );
        _claimRewardsOnBehalf(onBehalfOf, receiver, rewards);
    }

    function userAssetsHarness(address user) external view returns (uint256) {
        return _aToken.balanceOf(user);
    }

    function getReserveData_AToken() public view returns (address) {
        address cachedATokenUnderlying = _aTokenUnderlying;
        // DataTypes.ReserveData memory reserveData = POOL.getReserveData(cachedATokenUnderlying);
        return POOL.getReserveData(cachedATokenUnderlying).aTokenAddress;
    }
    
    function metaDepositHarness(
        address depositor,
        address recipient,
        uint256 value,
        uint16 referralCode,
        bool fromUnderlying,
        uint256 deadline,
        PermitParams memory permit,
        SignatureParams memory sigParams
    ) external returns (uint256) {
        permit.deadline = 1;
        fromUnderlying = true;
        return this.metaDeposit(depositor, recipient, value, referralCode, fromUnderlying, deadline, permit, sigParams);
    }
}
