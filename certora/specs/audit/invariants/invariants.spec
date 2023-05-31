/// @title Reward hook
/// @notice allows a single reward
//todo: allow 2 or 3 rewards
hook Sload address reward _rewardTokens[INDEX  uint256 i] STORAGE {
    require reward == _DummyERC20_rewardToken;
}

/// @title Sum of balances of StaticAToken
ghost mathint sumOfBalances {
    init_state axiom sumOfBalances == 0;
}

hook Sstore balanceOf[KEY address addy] uint256 newValue (uint256 oldValue) STORAGE {
    sumOfBalances = sumOfBalances + newValue - oldValue;
}

hook Sload uint256 val balanceOf[KEY address addy] STORAGE {
    require sumOfBalances >= val;
}

invariant totalSupplyIsSumOfBalances()
    totalSupply() == sumOfBalances


invariant totalAssetsSupplyZero(env e)
    ( userAssetsHarness(e, currentContract) == 0 => totalSupply() == 0 )
    && ( totalAssets(e) == 0 <=> ( totalSupply() == 0 ))



invariant assetsMoreThanSupply(env e1)
    totalAssets(e1) >= totalSupply()
    {
        preserved with (env e2) {
            require e2.msg.sender != currentContract;
            address any;
            safeAssumptions(e2, any , e2.msg.sender);
        }
    }

invariant noAssetsIfNoSupply(env e1)
   ( userAssetsHarness(e1, currentContract) == 0 => totalSupply() == 0 ) &&
    ( totalAssets(e1) == 0 => ( totalSupply() == 0 ))

    {
        preserved with (env e2) {
        address any;
            safeAssumptions(e2, any, e2.msg.sender);
        }
    }

definition noSupplyIfNoAssetsDef(env e) returns bool =
    ( userAssetsHarness(e, currentContract) == 0 => totalSupply() == 0 ) &&
    ( totalAssets(e) == 0 => ( totalSupply() == 0 ));

invariant noSupplyIfNoAssets()
    noSupplyIfNoAssetsDef()     // see defition in "helpers and miscellaneous" section
    {
        preserved with (env e) {
            safeAssumptions(e, _, e.msg.sender);
        }
    }


/* The following two invariants are just to show how tedious it is to prove the weaker version of totalSupplyIsSumOfBalances */
invariant sumOfBalancePairsBounded(address addy1, address addy2 )
    addy1 != addy2 => balanceOf(addy1) + balanceOf(addy2) <= totalSupply()
    {
        preserved {
            require asset() != currentContract;
            requireInvariant totalSupplyIsSumOfBalances();
        }
        preserved withdraw(uint256 assets, address receiver, address owner) with (env e2) {
            require asset() != currentContract;
            requireInvariant totalSupplyIsSumOfBalances();
            require owner == addy1 || owner == addy2 => balanceOf(addy1) + balanceOf(addy2) <= sumOfBalances;
            require owner != addy1 && owner != addy2 => balanceOf(addy1) + balanceOf(addy2) + balanceOf(owner) <= sumOfBalances;
        }
        preserved redeem(uint256 shares, address receiver, address owner) with (env e3) {
            require asset() != currentContract;
            requireInvariant totalSupplyIsSumOfBalances();
            require owner == addy1 || owner == addy2 => balanceOf(addy1) + balanceOf(addy2) <= sumOfBalances;
            require owner != addy1 && owner != addy2 => balanceOf(addy1) + balanceOf(addy2) + balanceOf(owner) <= sumOfBalances;
        }
        preserved transfer(address to, uint256 amount) with (env e4) {
            require asset() != currentContract;
            requireInvariant totalSupplyIsSumOfBalances();
            require e4.msg.sender == addy1 || e4.msg.sender == addy2 => balanceOf(addy1) + balanceOf(addy2) <= sumOfBalances;
            require e4.msg.sender != addy1 && e4.msg.sender != addy2 => balanceOf(addy1) + balanceOf(addy2) + balanceOf(e4.msg.sender) <= sumOfBalances;
        }
        preserved transferFrom(address from, address to, uint256 amount) with (env e5) {
            require asset() != currentContract;
            requireInvariant totalSupplyIsSumOfBalances();
            require from == addy1 || from == addy2 => balanceOf(addy1) + balanceOf(addy2) <= sumOfBalances;
            require from != addy1 && from != addy2 => balanceOf(addy1) + balanceOf(addy2) + balanceOf(from) <= sumOfBalances;
        }
    }

/* just to show how tedious it is to prove the weaker version of totalSupplyIsSumOfBalances */

invariant singleBalanceBounded(address addy )
    balanceOf(addy) <= totalSupply()
    {
        preserved {
            require asset() != currentContract;
            requireInvariant totalSupplyIsSumOfBalances();
        }
        preserved withdraw(uint256 assets, address receiver, address owner) with (env e2) {
            require asset() != currentContract;
            requireInvariant totalSupplyIsSumOfBalances();
            require addy == owner => balanceOf(addy)<= sumOfBalances;
            require addy != owner => balanceOf(addy) + balanceOf(owner) <= sumOfBalances;
        }
        preserved redeem(uint256 shares, address receiver, address owner) with (env e3) {
            require asset() != currentContract;
            requireInvariant totalSupplyIsSumOfBalances();
            require addy == owner => balanceOf(addy)<= sumOfBalances;
            require addy != owner => balanceOf(addy) + balanceOf(owner) <= sumOfBalances;
        }
        preserved transfer(address to, uint256 amount) with (env e4) {
            require asset() != currentContract;
            requireInvariant totalSupplyIsSumOfBalances();
            require addy == e4.msg.sender => balanceOf(addy) <= sumOfBalances;
            require addy != e4.msg.sender => balanceOf(addy) + balanceOf(e4.msg.sender) <= sumOfBalances;
        }
        preserved transferFrom(address from, address to, uint256 amount) with (env e5) {
            require asset() != currentContract;
            requireInvariant totalSupplyIsSumOfBalances();
            require addy == from => balanceOf(addy) <= sumOfBalances;
            require addy != from => balanceOf(addy) + balanceOf(from) <= sumOfBalances;
        }
    }

/// @title correct accrued value is fetched
/// @notice assume a single asset
invariant singleAssetAccruedRewards(env e0, address asset, address reward, address user)
    ((_RewardsController.getAssetListLength() == 1 && _RewardsController.getAssetByIndex(0) == asset)
        => (_RewardsController.getUserAccruedReward(asset, reward, user) == _RewardsController.getUserAccruedRewards(reward, user)))
    filtered { f -> !harnessOnlyMethods(f) }
        {
            preserved with (env e1){
                setup(e1, user);
                require asset != _RewardsController;
                require asset != _TransferStrategy;
                require reward != _StaticATokenLM;
                require reward != _AToken;
                require reward != _TransferStrategy;
            }
        }

invariant vaultSolvency(env e1)
    totalAssets(e1) >= totalSupply()  && userAssetsHarness(e1, currentContract) >= totalAssets(e1)  {
      preserved with(env e){
            requireInvariant totalSupplyIsSumOfBalances();
            require e.msg.sender != currentContract;
            require currentContract != asset();
        }
    }
