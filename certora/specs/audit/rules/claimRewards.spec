
// check rewards claimed are equal to claimable  rewards ?
// bug1
rule claimRewardsRule(env e) {

  address user;

  mathint _unclaimed = getUnclaimedRewards(user, _DummyERC20_rewardToken);
  mathint _claimable = getClaimableRewards(e, user, _DummyERC20_rewardToken);
  mathint _balUser   = _DummyERC20_rewardToken.balanceOf(user);
  mathint _balContract = _DummyERC20_rewardToken.balanceOf(user);

  address[] rewards;
  require rewards[0] == _DummyERC20_rewardToken;
  require rewards.length == 1;

  claimRewards(e, user, rewards);

  mathint unclaimed_ = getUnclaimedRewards(user, _DummyERC20_rewardToken);
  mathint claimable_ = getClaimableRewards(e, user, _DummyERC20_rewardToken);
  mathint balUser_   = _DummyERC20_rewardToken.balanceOf(user);
  mathint balContract_ = _DummyERC20_rewardToken.balanceOf(user);

  assert unclaimed_ == 0;
  assert claimable_ == 0;

  assert balUser_ >= _balUser;
  assert balContract_ >= _balContract;
  assert balUser_ == _balUser + _claimable;
  assert balUser_ == _balUser + _unclaimed;
}

// bug6
rule mintRule(env e) {
  uint256 shares;
  address user;

  mathint _balAssets = userAssetsHarness(e, user);
  mathint _balShares = balanceOf(user);

  mint(e, shares, user);

  mathint balAssets_ = userAssetsHarness(e, user);
  mathint balShares_ = balanceOf(user);

  assert balAssets_ >= _balAssets;
  assert balShares_ >= _balShares;
  assert balShares_ == _balShares + shares;
}
