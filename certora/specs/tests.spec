import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"


// Claimable rewards decrease on transfer
rule claimableRewardsDecreaseOnTransferA(env e) {
  address to;
  uint256 amount;

	single_RewardToken_setup();

  require rate(e) == 1 || rate(e) == 2 ;

  mathint _claimableRewards = getClaimableRewards(e, e.msg.sender, _DummyERC20_rewardToken);

  transfer(e, to, amount);

  mathint claimableRewards_ = getClaimableRewards(e, e.msg.sender, _DummyERC20_rewardToken);

  assert claimableRewards_ <= _claimableRewards;
}



// Claimable rewards decrease on transfer
rule claimableRewardsDecreaseOnTransferB(env e, calldataarg args) {
  address from = e.msg.sender;
  address to;
  uint256 amount;

	single_RewardToken_setup();

  mathint _claimableRewards = getClaimableRewards(e, from, _DummyERC20_rewardToken);
  mathint _balanceStataTokenFrom = balanceOf(from);
  mathint _balanceStataTokenTo = balanceOf(to);


  require(to != from);
  transfer(e, to, amount);

  mathint claimableRewards_ = getClaimableRewards(e, from, _DummyERC20_rewardToken);
  mathint balanceStataTokenFrom_ = balanceOf(from);
  mathint balanceStataTokenTo_ = balanceOf(to);

  assert claimableRewards_ <= _claimableRewards;

  assert _balanceStataTokenFrom + _balanceStataTokenTo
    ==   balanceStataTokenFrom_ + balanceStataTokenTo_;

  assert balanceStataTokenFrom_ + amount == _balanceStataTokenFrom;
}
