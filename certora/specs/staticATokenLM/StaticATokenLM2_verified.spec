import "../methods/methods_base.spec"
import "./StaticATokenLM_base.spec"
import "./StaticATokenLM_common.spec"


rule unclaimedUnchangedRule2(method f, env e, calldataarg args) filtered {
    f -> f.selector == mint(uint256,address).selector
}{
    address user;

    mathint _unclaimed = getUnclaimedRewards(user, _DummyERC20_rewardToken);
    f(e, args);
    mathint unclaimed_ = getUnclaimedRewards(user, _DummyERC20_rewardToken);

    assert unclaimed_ == _unclaimed;
}


rule claimableUnchangedRule2(method f, env e, calldataarg args) filtered {
    f ->  f.selector == mint(uint256,address).selector
      &&  f.selector == initialize(address,string,string).selector
}{
    address user;

    mathint _claimable = getClaimableRewards(e, user, _DummyERC20_rewardToken);
    f(e, args);
    mathint claimable_ = getClaimableRewards(e, user, _DummyERC20_rewardToken);

    assert claimable_ == _claimable;
}
