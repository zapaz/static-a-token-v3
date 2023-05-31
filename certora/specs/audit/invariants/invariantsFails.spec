
invariant zeroAssetsSupplyInvariant(env e)
  totalAssets(e) == 0 <=> totalSupply() == 0
