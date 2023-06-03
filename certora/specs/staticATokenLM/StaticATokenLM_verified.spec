import "../methods/methods_base.spec"
import "./StaticATokenLM_base.spec"

// correct accrued value is fetched assuming a single asset
use invariant singleAssetAccruedRewards

// The amount of rewards that was actually received by claimRewards()
// cannot exceed the initial amount of rewards
use rule getClaimableRewardsBefore_leq_claimed_claimRewardsOnBehalf

// stataToken total supply equal sum of all balances
invariant totalSupplyInvariant()
    totalSupply() == sumAllBalance()
    filtered { f -> !untestedFunctions(f)}


// unclaimed rewards always less than claimable rewards
rule unclaimedLessThanClaimableRule(env e) {
    address user;

    mathint _unclaimed = getUnclaimedRewards(user, _DummyERC20_rewardToken);
    mathint _claimable = getClaimableRewards(e, user, _DummyERC20_rewardToken);

    assert _unclaimed <= _claimable;
}

// unclaimed rewards unchanged by any function expect filtered
rule unclaimedUnchangedRule(method f, env e, calldataarg args) filtered {
    f -> !depositFunctions(f) && !withdrawFunctions(f)
      && !claimFunctions(f)   && !transferFunctions(f)
      && !untestedFunctions(f)
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
      && !untestedFunctions(f)
      &&  f.selector != initialize(address,string,string).selector
}{
    address user;

    single_RewardToken_setup();

    mathint _claimable = getClaimableRewards(e, user, _DummyERC20_rewardToken);
    f(e, args);
    mathint claimable_ = getClaimableRewards(e, user, _DummyERC20_rewardToken);

    assert claimable_ == _claimable;
}

// total assets unchanged by any function except deposit, withdraw and claim functions
rule totalAssetsUnchangedRule(method f) filtered {
    f -> !depositFunctions(f) && !withdrawFunctions(f) && !claimFunctions(f) && !untestedFunctions(f)
}{
    env e; calldataarg args;

    mathint _totalAssets = totalAssets(e);
    f(e, args);
    mathint totalAssets_ = totalAssets(e);

    assert totalAssets_ == _totalAssets;
}