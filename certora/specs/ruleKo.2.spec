import "methods/methods_base.spec"
// import "staticATokenLM/StaticATokenLM_base.spec"

// function safeAssumptions(env e, address receiver, address owner) {
//     require currentContract != asset();
//     // requireInvariant totalSupplyIsSumOfBalances();
//     // requireInvariant noSupplyIfNoAssets();
//     // requireInvariant vaultSolvency(e);
//     // requireInvariant noAssetsIfNoSupply(e);
//     // requireInvariant assetsMoreThanSupply(e);

//     require ( (receiver != owner => balanceOf(owner) + balanceOf(receiver) <= totalSupply())  &&
//                 balanceOf(receiver) <= totalSupply() &&
//                 balanceOf(owner) <= totalSupply());
// }


// definition noSupplyIfNoAssetsDef(env e) returns bool =
//     ( _AToken.balanceOf(e, currentContract) == 0 => totalSupply() == 0 ) &&
//     ( totalAssets(e) == 0 => ( totalSupply() == 0 ));

// invariant noSupplyIfNoAssets()
//     noSupplyIfNoAssetsDef()     // see defition in "helpers and miscellaneous" section
//     // {
//     //     preserved with (env e) {
//     //         safeAssumptions(e, _, e.msg.sender);
//     //     }
//     // }


// invariant noSupplyIfNoAssets(env e)
//     ( _AToken.balanceOf(e, currentContract) == 0 => totalSupply() == 0 ) &&
//     ( totalAssets(e) == 0 => ( totalSupply() == 0 ))

rule noSupplyIfNoAssetsRule() filtered {
    f -> !untestedFunctions(f)
}{
    require _AToken.balanceOf(e, currentContract) == 0 => totalSupply() == 0;
	f(e, args);
    assert _AToken.balanceOf(e, currentContract) == 0 => totalSupply() == 0;
}

// invariant balancesLessThanSupplyInvariant(address user1, address user2)
//     user1 != user2 => balanceOf(user1) + balanceOf(user2) <= totalSupply()
