// Underlying metaDeposit with Permit allways fails when Underlying token is not IERC20Permit
// i.e. this rule is True
rule metaDepositFailsWithUnderlyingWithNoPermitRule(env e) {
    // _DummyERC20_aTokenUnderlying has no permit function, true when conf links to dummy ERC20
    require getStaticATokenUnderlying() == _DummyERC20_aTokenUnderlying;

    bool fromUnderlying;
    _StaticATokenLM.SignatureParamsHarness sigParams;
    _StaticATokenLM.PermitParamsHarness permit;

    metaDeposit@withrevert(e, _, _, _, _, fromUnderlying, _, sigParams, permit);

    // Underlying metaDeposit with permit used always reverts  (permit used when `permit.deadline != 0`)
    assert (fromUnderlying == true) && (permit.deadline != 0) => lastReverted;
}
