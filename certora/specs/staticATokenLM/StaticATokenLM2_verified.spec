import "../methods/methods_base.spec"
import "./StaticATokenLM_base.spec"

// Claimable rewards decrease on transfer
rule claimableRewardsDecreaseOnTransfer(env e, calldataarg args) {
  address from = e.msg.sender;
  address to;
  uint256 amount;

  require rate(e) == 1 || rate(e) == 2 ;
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
