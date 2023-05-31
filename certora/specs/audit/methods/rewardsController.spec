methods {           
    _RewardsController.getRewardsIndex(address,address)returns (uint256) envfree
    _RewardsController.getAvailableRewardsCount(address) returns (uint128) envfree
    _RewardsController.getRewardsByAsset(address, uint128) returns (address) envfree
    _RewardsController.getAssetListLength() returns (uint256) envfree
    _RewardsController.getAssetByIndex(uint256) returns (address) envfree
    _RewardsController.getDistributionEnd(address, address)  returns (uint256) envfree
    _RewardsController.getUserAccruedRewards(address, address) returns (uint256) envfree
    _RewardsController.getUserAccruedReward(address, address, address) returns (uint256) envfree
    _RewardsController.getAssetDecimals(address) returns (uint8) envfree
    _RewardsController.getRewardsData(address,address) returns (uint256,uint256,uint256,uint256) envfree
    _RewardsController.getUserAssetIndex(address,address, address) returns (uint256) envfree
}