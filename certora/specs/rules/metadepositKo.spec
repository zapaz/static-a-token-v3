using StaticATokenLMHarness as _StaticATokenLM

methods
{
    // metaDeposit(address,address,uint256,uint16,bool,uint256,_StaticATokenLM.PermitParams,_StaticATokenLM.SignatureParams) returns uint256
    // metaDeposit(address,address,uint256,uint16,bool,uint256,(address,address,uint256,uint256,uint8,bytes32,bytes32),(uint8,bytes32,bytes32)) returns uint256
}

// Underlying metaDeposit with Permit allways fails when Underlying is not IERC20Permit
// i.e. this rule is unreachable
rule metaDepositFailsWithUnderlyingWithNoPermitRule(env e) {
    // _DummyERC20_aTokenUnderlying has no permit function, true when conf links to dummy ERC20
    require getStaticATokenUnderlying() == _DummyERC20_aTokenUnderlying;

    bool fromUnderlying;
    _StaticATokenLM.PermitParams permit;
    _StaticATokenLM.SignatureParams sigParams;

    require fromUnderlying == true;
    require permit.deadline != 0;

    metaDeposit(e, _, _, _, _, fromUnderlying, _, permit, sigParams);

    assert true;
}

rule metaDepositRule() {
    env e;
    calldataarg args;

    metaDeposit(e, args);

    assert true;
}

rule metaDepositRule2(env e) {
    bool fromUnderlying;
    _StaticATokenLM.PermitParams permit;
    _StaticATokenLM.SignatureParams sigParams;

    metaDeposit(e, _, _, _, _, fromUnderlying, _, permit, sigParams);

    assert true;
}

rule metaDepositRule3(env e) {
    _StaticATokenLM.PermitParams permit;
    _StaticATokenLM.SignatureParams sigParams;

    metaDeposit(e, _, _, _, _, false, _, permit, sigParams);

    assert true;
}

rule metaDepositRule4() {
    env e;
    calldataarg args;

    metaDeposit@withrevert(e, args);

    assert lastReverted;
}