methods
{
    getIncentivesController() returns (address) => CONSTANT
    getRewardsList() returns (address[]) => NONDET
    handleAction(address,uint256,uint256) => DISPATCHER(true)  //  => NONDET 
    getScaledUserBalanceAndSupply(address) returns (uint256, uint256) => NONDET   
    performTransfer(address,address,uint256) returns (bool) => NONDET

    // static aToken
    // -------------
    getCurrentRewardsIndex(address reward) returns (uint256) => CONSTANT

    // pool
    // ----
    // In RewardsDistributor.sol called by RewardsController.sol
    getAssetIndex(address, address) returns (uint256, uint256) => NONDET

    // In ScaledBalanceTokenBase.sol called by getAssetIndex
    scaledTotalSupply() returns (uint256) => NONDET

    // aToken
    // ------
    mint(address,address,uint256,uint256) returns (bool) => NONDET
    burn(address,address,uint256,uint256) returns (bool) => NONDET
    
    permit(address,address,uint256,uint256,uint8,bytes32,bytes32) => NONDET
}