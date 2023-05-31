definition depositFunctions(method f) returns bool =
    (   f.selector == deposit(uint256,address).selector 
    ||  f.selector == deposit(uint256,address,uint16,bool).selector 
    ||  f.selector == metaDeposit(address,address,uint256,uint16,bool,uint256,(address,address,uint256,uint256,uint8,bytes32,bytes32),(uint8,bytes32,bytes32)).selector );

definition claimFunctions(method f) returns bool =
    (   f.selector == claimRewardsToSelf(address[]).selector 
    ||  f.selector == claimRewards(address, address[]).selector 
    ||  f.selector == claimRewardsOnBehalf(address, address,address[]).selector );

definition withdrawFunctions(method f) returns bool =
    (   f.selector == redeem(uint256,address,address).selector  
    ||  f.selector == redeem(uint256,address,address,bool).selector 
    ||  f.selector == withdraw(uint256,address,address).selector 
    ||  f.selector == metaWithdraw(address,address,uint256,uint256,bool,uint256,(uint8,bytes32,bytes32)).selector );

definition assetsFunctions(method f) returns bool =
    (   f.selector == mint(uint256,address).selector ||
        depositFunctions(f) || claimFunctions(f) || withdrawFunctions(f) );

definition RAY() returns uint256 = 10^27;

definition collectAndUpdateFunction(method f) returns bool =
    f.selector == collectAndUpdateRewards(address).selector;

definition harnessOnlyMethods(method f) returns bool =
    (harnessMethodsMinusHarnessClaimMethods(f) ||
    f.selector == claimSingleRewardOnBehalf(address, address, address).selector ||
    f.selector == claimDoubleRewardOnBehalfSame(address, address, address).selector);

definition harnessMethodsMinusHarnessClaimMethods(method f) returns bool =
    (f.selector == getStaticATokenUnderlying().selector ||
    f.selector == getRewardTokensLength().selector ||
    f.selector == getRewardToken(uint256).selector ||
    f.selector == getRewardsIndexOnLastInteraction(address, address).selector ||
    f.selector == getLastUpdatedIndex(address).selector);
