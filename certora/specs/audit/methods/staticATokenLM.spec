methods {
    // ERC20
    name                                ()                              returns string      envfree
    symbol                              ()                              returns string      envfree
    decimals                            ()                              returns uint8       envfree
    totalSupply                         ()                              returns uint256     envfree
    _StaticATokenLM.balanceOf           (address)                       returns uint256     envfree
    allowance                           (address,address)               returns uint256     envfree
    approve                             (address,uint256)               returns bool
    transfer                            (address,uint256)               returns bool
    transferFrom                        (address,address,uint256)       returns bool

    // ASSETS / SHARES
    asset                               ()                              returns address     envfree
    aToken                              ()                              returns address     envfree
    aTokenUnderlying                    ()                              returns address     envfree
    totalAssets                         ()                              returns uint256
    convertToAssets                     (uint256)                       returns uint256
    convertToShares                     (uint256)                       returns uint256

    // DEPOSIT
    METADEPOSIT_TYPEHASH                ()                              returns bytes32     envfree
    maxDeposit                          (address)                       returns uint256     envfree
    previewDeposit                      (uint256)                       returns uint256     envfree
    maxDepositUnderlying                (address)                       returns uint256
    depositHarness                      (uint256,address,uint16,bool)   returns uint256
    deposit                             (uint256,address)               returns uint256
    metaDeposit                         (address,address,uint256,uint16,bool,uint256,_StaticATokenLM.SignatureParamsHarness,_StaticATokenLM.PermitParamsHarness)        returns uint256

    // WITHDRAW
    METAWITHDRAWAL_TYPEHASH             ()                              returns bytes32     envfree
    maxWithdraw                         (address)                       returns uint256
    previewWithdraw                     (uint256)                       returns uint256
    withdraw                            (uint256,address,address)       returns uint256
    metaWithdraw                        (address,address,uint256,uint256,bool,uint256,(uint8,bytes32,bytes32))   returns (uint256,uint256)

    // REDEEM
    maxRedeem                           (address)                       returns uint256     envfree
    maxRedeemUnderlying                 (address)                       returns uint256     envfree
    previewRedeem                       (uint256)                       returns uint256     envfree
    redeem                              (uint256,address,address)       returns uint256
    redeem                              (uint256,address,address,bool)  returns (uint256,uint256)

    // MINT
    previewMint                         (uint256)                       returns uint256
    maxMint                             (address)                       returns uint256     envfree
    mint                                (uint256,address)               returns uint256

    // REWARDS
    rewardTokens                        ()                              returns address[]   envfree
    getTotalClaimableRewards            (address)                       returns uint256     envfree
    getUnclaimedRewards                 (address, address)              returns uint256     envfree
    getCurrentRewardsIndex              (address)                       returns uint256     envfree
    isRegisteredRewardToken             (address)                       returns bool        envfree
    getClaimableRewards                 (address, address)              returns uint256
    collectAndUpdateRewards             (address)                       returns uint256
    refreshRewardTokens                 ()
    claimRewardsToSelf                  (address[])
    claimRewards                        (address, address[])
    claimRewardsOnBehalf                (address,address, address[])

    // OTHERS
    rate                                ()                              returns uint256
    initialize                          (address,string,string)

    // HARNESS
    getStaticATokenUnderlying           ()                              returns address     envfree
    getRewardToken                      (uint256)                       returns address     envfree
    getRewardTokensLength               ()                              returns uint256     envfree
    getRewardsIndexOnLastInteraction    (address, address)              returns uint128     envfree
    getLastUpdatedIndex                 (address)                       returns uint248
    claimSingleRewardOnBehalf           (address,address,address)
    claimDoubleRewardOnBehalfSame       (address,address,address)
    userAssetsHarness                   (address user)                  returns uint256
    metaDepositHarness                  (address,address,uint256,uint16,bool,uint256,(address,address,uint256,uint256,uint8,bytes32,bytes32), \
                                        (uint8,bytes32,bytes32))        returns uint256
 }
