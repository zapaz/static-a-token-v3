import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"


// Claimable rewards decrease on transfer
rule claimableRewardsDecreaseOnTransfer(method f, env e, calldataarg args) {
  address from = e.msg.sender;

	single_RewardToken_setup();

  // require rate(e) == 1 || rate(e) == 2 ;

  mathint _claimableRewards = getClaimableRewards(e, from, _DummyERC20_rewardToken);
  mathint _balanceAToken = _AToken.balanceOf(e, from);

  f(e, args);

  mathint claimableRewards_ = getClaimableRewards(e, from, _DummyERC20_rewardToken);
  mathint balanceAToken_ = _AToken.balanceOf(e, from);

  assert _balanceAToken == balanceAToken_ => claimableRewards_ == _claimableRewards;
}
