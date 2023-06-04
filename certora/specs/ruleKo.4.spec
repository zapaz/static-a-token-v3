import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"

// stataToken total supply equal sum of all balances
// invariant totalSupplyInvariant()
//     totalSupply() == sumAllBalance()
//     filtered { f -> !untestedFunctions(f)}

// invariant vaultSolvency(env e1)
//     totalAssets(e1) >= totalSupply()  && _AToken.balanceOf(e1, currentContract) >= totalAssets(e1)  {
//       preserved with(env e){
//             requireInvariant totalSupplyInvariant();
//             require e.msg.sender != currentContract;
//             require currentContract != asset();
//         }
//     }

invariant vaultSolvencyA(env e)
    totalAssets(e) >= totalSupply()

invariant vaultSolvencyB(env e)
    _AToken.balanceOf(e, currentContract) >= totalAssets(e)
