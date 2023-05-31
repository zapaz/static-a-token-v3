

rule totalAssetsUnchangedRule(method f) filtered {f -> !assetsFunctions(f)}{
    env e; calldataarg args;
    
    mathint totalAssetsBefore = totalAssets(e);
    f(e, args);
    mathint totalAssetsAfter = totalAssets(e);

    assert totalAssetsAfter == totalAssetsBefore;
}


