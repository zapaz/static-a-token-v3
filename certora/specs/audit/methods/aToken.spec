methods {
    // ERC20
    _AToken.name            ()                          returns string  envfree
    _AToken.symbol          ()                          returns string  envfree
    _AToken.decimals        ()                          returns uint8   envfree
    _AToken.totalSupply     ()                          returns uint256
    _AToken.balanceOf       (address)                   returns uint256
    _AToken.allowance       (address,address)           returns uint256 envfree
    _AToken.approve         (address,uint256)           returns bool
    _AToken.transfer        (address,uint256)           returns bool
    _AToken.transferFrom    (address,address,uint256)   returns bool

    // ERC20 with PERMIT
    _AToken.DOMAIN_SEPARATOR            ()              returns bytes32 envfree
    _AToken.permit                      (address,address,uint256,uint256,uint8,bytes32,bytes32)

    // aTOKEN
    _AToken.UNDERLYING_ASSET_ADDRESS    ()              returns (address) envfree
    _AToken.scaledTotalSupply           ()              returns (uint256) envfree
    _AToken.scaledBalanceOf             (address)       returns (uint256) envfree
}
