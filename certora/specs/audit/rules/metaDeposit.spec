// Underlying metaDeposit with Permit allways fails when Underlying token is not IERC20Permit
// i.e. this rule is True
rule metaDepositFailsWithUnderlyingWithNoPermitRule() {
    env e; calldataarg args;

    address depositor;
    address recipient;
    uint256 value;
    uint16 referralCode;
    bool fromUnderlying;
    uint256 deadline;

    _StaticATokenLM.SignatureParamsHarness sigParams;
    _StaticATokenLM.PermitParamsHarness permit;

    // _DummyERC20_aTokenUnderlying has no permit function
    require getStaticATokenUnderlying() == _DummyERC20_aTokenUnderlying;

    metaDeposit@withrevert(e, depositor, recipient, value, referralCode, fromUnderlying, deadline, sigParams, permit);

    // Underlying metaDeposit with permit used always reverts  (permit used when `permit.daedline != 0`)
    assert (fromUnderlying == true) && (permit.deadline != 0) => lastReverted;
}
