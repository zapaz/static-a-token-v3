import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"

// FALSE
// often false, only rounding problem ???
//
// FALSE        for claimRewards, withdraw, mint, redeem, deposit
// UNREACHABLE  for metaDeposit
// TIMOUT       for claimRerwardsOnBehalf

rule mintRule_01(method f, env e, calldataarg args) filtered {
    f -> !untestedFunctions(f)
}{
    mathint _aTokenBalanceContract = _AToken.balanceOf(e, currentContract);
    mathint _stataTokenBalanceContract = totalSupply();
    mathint _currentRate = rate(e);

    require _stataTokenBalanceContract == _aTokenBalanceContract * _currentRate;

    f(e, args);

    mathint aTokenBalanceContract_ = _AToken.balanceOf(e, currentContract);
    mathint stataTokenBalanceContract_ = totalSupply();
    mathint currentRate_ = rate(e);

    assert stataTokenBalanceContract_ == aTokenBalanceContract_ * currentRate_;
}
