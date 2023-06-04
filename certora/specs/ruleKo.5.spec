
import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"

function safeAssumptions(env e, address receiver, address owner) {
    require currentContract != asset();
    // requireInvariant totalSupplyIsSumOfBalances();
    // requireInvariant noSupplyIfNoAssets();
    // requireInvariant vaultSolvency(e);
    requireInvariant noAssetsIfNoSupply(e);
    // requireInvariant assetsMoreThanSupply(e);

    require ( (receiver != owner => balanceOf(owner) + balanceOf(receiver) <= totalSupply())  &&
                balanceOf(receiver) <= totalSupply() &&
                balanceOf(owner) <= totalSupply());
}


invariant noAssetsIfNoSupply(env e1)
  ( _AToken.balanceOf(e1, currentContract) == 0 => totalSupply() == 0 ) &&
  ( totalAssets(e1) == 0 => ( totalSupply() == 0 ))
  {
      preserved with (env e2) {
      address any;
          safeAssumptions(e2, any, e2.msg.sender);
      }
  }
