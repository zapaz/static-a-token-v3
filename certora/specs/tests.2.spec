import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"


// Claimable rewards decrease on transfer
rule claimsRule(method f, env e, calldataarg args) filtered {
    f -> claimFunctions(f)
}{
  address from = e.msg.sender;

	single_RewardToken_setup();

  // require rate(e) == 1 || rate(e) == 2 ;

  mathint _claimableRewards = getClaimableRewards(e, from, _DummyERC20_rewardToken);
  mathint _unclaimedRewards = getUnclaimedRewards(from, _DummyERC20_rewardToken);

  f(e, args);

  mathint claimableRewards_ = getClaimableRewards(e, from, _DummyERC20_rewardToken);
  mathint unclaimedRewards_ = getUnclaimedRewards(from, _DummyERC20_rewardToken);

  assert claimableRewards_ == unclaimedRewards_;
  assert claimableRewards_ <= _claimableRewards;
}
