## Bug
1/ `metaDeposit` fails when `aTokenUnderlying` has no `permit`function
=> bug proof rule : `metaDepositFailsWithUnderlyingWithNoPermitRule`
=> use `_PermitERC20_aTokenUnderlying` instead of `_DummyERC20_aTokenUnderlying` for all other tests
   (another option would be to fix the bug, but testing with permit add more testing coverage)

## Remarks
a/ `totalAssets()` is declared envfree  in `methods_base.spec` but is dependant on `block.timestamp`
is it considered as a bug or not, in this audit contest ?
(fixed by Certora team during contest with new commit on certora* branch)

b/ `DummyERC20Impl` decimals should be uint8 not uint256
