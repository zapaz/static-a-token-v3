import "../methods/methods_base.spec"
import "./StaticATokenLM_base.spec"

use invariant singleAssetAccruedRewards
use rule getClaimableRewardsBefore_leq_claimed_claimRewardsOnBehalf

invariant totalSupplyInvariant()
    totalSupply() == sumAllBalance()
    filtered { f -> !harnessFunctions(f) && !metaDepositFunction(f)}

rule totalAssetsUnchangedRule(method f) filtered {
    f -> !assetsFunctions(f) && !harnessFunctions(f)
}{
    env e; calldataarg args;

    mathint _totalAssets = totalAssets(e);
    f(e, args);
    mathint totalAssets_ = totalAssets(e);

    assert totalAssets_ == _totalAssets;
}

rule rewardsUnclaimedLessThanClaimableRule(env e) {
    address user;

    mathint _unclaimed = getUnclaimedRewards(user, _DummyERC20_rewardToken);
    mathint _claimable = getClaimableRewards(e, user, _DummyERC20_rewardToken);

    assert _unclaimed <= _claimable;
}

rule claimableLessThanUnclaimedRule2(method f, env e, calldataarg  args) filtered {
    f -> !harnessFunctions(f)
}{
    address user;
    // setup(e, user);

    mathint _unclaimed = getUnclaimedRewards(user, _DummyERC20_rewardToken);
    mathint _claimable = getClaimableRewards(e, user, _DummyERC20_rewardToken);
    require _unclaimed <= _claimable;

    f(e, args);

    mathint unclaimed_ = getUnclaimedRewards(user, _DummyERC20_rewardToken);
    mathint claimable_ = getClaimableRewards(e, user, _DummyERC20_rewardToken);
    assert unclaimed_ <= claimable_;
}

rule unclaimedUnchangedRule(method f, env e, calldataarg args) filtered {
    f -> !depositFunctions(f) && !withdrawFunctions(f)
      && !claimFunctions(f)   && !transferFunctions(f)
      && !harnessFunctions(f)
}{
    address user;

    mathint _unclaimed = getUnclaimedRewards(user, _DummyERC20_rewardToken);
    f(e, args);
    mathint unclaimed_ = getUnclaimedRewards(user, _DummyERC20_rewardToken);

    assert unclaimed_ == _unclaimed;
}

rule claimableUnchangedRule(method f, env e, calldataarg args) filtered {
    f -> !depositFunctions(f) && !withdrawFunctions(f)
      && !claimFunctions(f)   && !transferFunctions(f)
      && !harnessFunctions(f)
}{
    address user;

    mathint _claimable = getClaimableRewards(e, user, _DummyERC20_rewardToken);
    f(e, args);
    mathint claimable_ = getClaimableRewards(e, user, _DummyERC20_rewardToken);

    assert claimable_ == _claimable;
}
