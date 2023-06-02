import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"

/////////////////// Methods ////////////////////////

////////////////// FUNCTIONS //////////////////////

///////////////// Properties ///////////////////////

invariant zeroAssetsSupplyInvariant(env e)
    totalAssets(e) == 0 <=> totalSupply() == 0
    {
        preserved with (env ep) {
            setup( ep, ep.msg.sender);
        }
    }

// bug6
rule mintRule(env e) {
    uint256 shares;
    address user;

    setup(e, user);

    mathint _balAssets = _AToken.balanceOf(e, user);
    mathint _balShares = balanceOf(user);

    mint(e, shares, user);

    mathint balAssets_ = _AToken.balanceOf(e, user);
    mathint balShares_ = balanceOf(user);

    assert balAssets_ >= _balAssets;
    assert balShares_ >= _balShares;
    assert balShares_ == _balShares + shares;
}


// check rewards claimed are equal to claimable  rewards ?
// bug1
rule claimRewardsRule(env e) {
    address user;
    require user != 0;
    
    // setup(e, user);

    mathint _unclaimed = getUnclaimedRewards(user, _DummyERC20_rewardToken);
    mathint _claimable = getClaimableRewards(e, user, _DummyERC20_rewardToken);
    mathint _balUser   = _DummyERC20_rewardToken.balanceOf(user);
    mathint _balContract = _DummyERC20_rewardToken.balanceOf(user);

    uint256 ether = 1000000000000000000;
    require _unclaimed   >= 1 * ether;
    require _claimable   >= 1 * ether;
    require _balUser     <= 1 * ether;
    require _balContract >= 1000 * ether;
    require _balContract <= 1000000000 * ether;

    single_RewardToken_setup();
    address[] rewards;
    require rewards[0] == _DummyERC20_rewardToken;
    require rewards.length == 1;
    claimRewards(e, user, rewards);


    mathint unclaimed_ = getUnclaimedRewards(user, _DummyERC20_rewardToken);
    mathint claimable_ = getClaimableRewards(e, user, _DummyERC20_rewardToken);
    mathint balUser_   = _DummyERC20_rewardToken.balanceOf(user);
    mathint balContract_ = _DummyERC20_rewardToken.balanceOf(user);

    assert unclaimed_ == 0;
    assert claimable_ == 0;

    assert balUser_ >= _balUser;
    assert balContract_ >= _balContract;
    assert balUser_ == _balUser + _claimable;
    assert balUser_ == _balUser + _unclaimed;
}

