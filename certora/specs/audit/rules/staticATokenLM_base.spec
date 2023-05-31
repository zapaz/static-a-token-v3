/// @title The amount of rewards that was actually received by claimRewards() cannot exceed the initial amount of rewards
rule getClaimableRewardsBefore_leq_claimed_claimRewardsOnBehalf()
{
    env e;
    address onBehalfOf;
    address receiver;
    require receiver != currentContract;

    mathint balanceBefore = _DummyERC20_rewardToken.balanceOf(receiver);
    mathint claimableRewardsBefore = getClaimableRewards(e, onBehalfOf, _DummyERC20_rewardToken);
    claimSingleRewardOnBehalf(e, onBehalfOf, receiver, _DummyERC20_rewardToken);
    mathint balanceAfter = _DummyERC20_rewardToken.balanceOf(receiver);
    mathint deltaBalance = balanceAfter - balanceBefore;

    assert deltaBalance <= claimableRewardsBefore;
}
