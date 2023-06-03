import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"

// UNREACHABLE for claim functions... why ?
rule totalAssetsUnchangedRule_11d(method f) filtered {
    f -> claimFunctions(f)
}{
    env e; calldataarg args;

    // setup(e);
    // single_RewardToken_setup();

    mathint _totalAssets = totalAssets(e);
    f(e, args);
    mathint totalAssets_ = totalAssets(e);

    assert totalAssets_ == _totalAssets;
}