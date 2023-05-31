
// with totalAssets envfree this rule fails
// as totalAssets depends on block.timestamp
// rule totalAssetsBugRule(env e) {
//   mathint totalAssetsFirst = totalAssets(e);
//   mathint totalAssetsSecond = totalAssets(e);

//   assert totalAssetsFirst == totalAssetsSecond;
//  }

rule totalAssetsOkRule(env e) {
  mathint totalAssetsFirst = totalAssets(e);
  mathint totalAssetsSecond = totalAssets(e);

  assert totalAssetsFirst == totalAssetsSecond;
}