import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"


// Claimable rewards decrease on transfer
rule claimsRule(method f, env e, calldataarg args) filtered {
    f -> claimFunctions(f)
}{
    address user = e.msg.sender;

    setupUser(e, user);
	single_RewardToken_setup();

	// require rate(e) == 1 || rate(e) == 2 ;

    mathint _claimableRewards = getClaimableRewards(e, user, _DummyERC20_rewardToken);
    mathint _unclaimedRewards = getUnclaimedRewards(user, _DummyERC20_rewardToken);
  	mathint _balanceRewards = _DummyERC20_rewardToken.balanceOf(user);

    address[] rewards;
    require rewards[0] == _DummyERC20_rewardToken;
    require rewards.length == 1;

    claimRewardsToSelf(e, rewards);

    mathint claimableRewards_ = getClaimableRewards(e, user, _DummyERC20_rewardToken);
    mathint unclaimedRewards_ = getUnclaimedRewards(user, _DummyERC20_rewardToken);
  	mathint balanceRewards_ = _DummyERC20_rewardToken.balanceOf(user);

	assert balanceRewards_ + unclaimedRewards_ == _balanceRewards + _claimableRewards;
	// assert balanceRewards_ <= _balanceRewards + _claimableRewards;

	assert unclaimedRewards_ == claimableRewards_;
    assert claimableRewards_ <= _claimableRewards;
}