// ERC4626 : totalAssets MUST NOT revert
// totalAssets reverts with large number of assets and large rate
// this rule fails
rule totalAssetsMustNotRevert(env e) {
  require e.msg.value == 0;

  totalAssets@withrevert(e);

  assert !lastReverted , "ERC4626 : totalAssets MUST NOT revert";
}