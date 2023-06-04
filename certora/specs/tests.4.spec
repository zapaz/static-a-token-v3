import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"


// Claimable rewards decrease on transfer
rule claimableRewardsDecreaseOnTransferA(env e) {
  address to;
  uint256 amount;

  require rate(e) == 1 || rate(e) == 2 ;

  mathint _claimableRewards = getClaimableRewards(e, e.msg.sender, _DummyERC20_rewardToken);

  transfer(e, to, amount);

  mathint claimableRewards_ = getClaimableRewards(e, e.msg.sender, _DummyERC20_rewardToken);

  assert claimableRewards_ <= _claimableRewards;
}
