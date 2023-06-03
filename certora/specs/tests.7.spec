import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"

// UNSOUND
// often false, only rounding problem ???
//
// FALSE        for deposit, withdraw and claim

rule erc4626RatioRule_07 {
  method f; env e; calldataarg arg;
  address user;

  // setupUser(e, user);

  mathint _stataTokenBalanceOfUser = balanceOf(user);
  mathint _stataTokenTotalSupply   = totalSupply();
  mathint _aTokenBalanceOfUser     = _AToken.balanceOf(e, user);
  mathint _aTokenBalanceOfCotract  = _AToken.balanceOf(e, currentContract);
  require _stataTokenBalanceOfUser * _aTokenBalanceOfCotract  == _aTokenBalanceOfUser * _stataTokenTotalSupply;

  f@withrevert(e, arg);

  mathint stataTokenBalanceOfUser_ = balanceOf(user);
  mathint stataTokenTotalSupply_   = totalSupply();
  mathint aTokenBalanceOfUser_     = _AToken.balanceOf(e, user);
  mathint aTokenBalanceOfCotract_  = _AToken.balanceOf(e, currentContract);
  assert stataTokenBalanceOfUser_ * aTokenBalanceOfCotract_  == aTokenBalanceOfUser_ * stataTokenTotalSupply_;
}


// ERC4626 ratio invariant
// stataToken balanceOf user divided by stataToken totalSupply
// should stay equal to
// aToken balanceOf user divided by aToken balanceOf currentContract
invariant erc4626RatioInvariant_07(env e, address user)
  balanceOf(user) * _AToken.balanceOf(e, currentContract)  == _AToken.balanceOf(e, user) * totalSupply()
