methods {
    // ERC20
    _ATokenUnderlying.name            ()                          returns string  envfree         
    _ATokenUnderlying.symbol          ()                          returns string  envfree         
    _ATokenUnderlying.decimals        ()                          returns uint8   envfree        
    _ATokenUnderlying.totalSupply     ()                          returns uint256 envfree 
    _ATokenUnderlying.balanceOf       (address)                   returns uint256 envfree 
    _ATokenUnderlying.allowance       (address,address)           returns uint256 envfree 
    _ATokenUnderlying.approve         (address,uint256)           returns bool            
    _ATokenUnderlying.transfer        (address,uint256)           returns bool            
    _ATokenUnderlying.transferFrom    (address,address,uint256)   returns bool        

    // ERC20 with PERMIT
    // _ATokenUnderlying.DOMAIN_SEPARATOR    ()                                                      returns bytes32 envfree
    // _ATokenUnderlying.permit              (address,address,uint256,uint256,uint8,bytes32,bytes32)
}

