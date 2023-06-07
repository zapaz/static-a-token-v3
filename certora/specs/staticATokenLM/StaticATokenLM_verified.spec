import "../methods/methods_base.spec"
import "./StaticATokenLM_base.spec"

// correct accrued value is fetched assuming a single asset
use invariant singleAssetAccruedRewards

// The amount of rewards that was actually received by claimRewards()
// cannot exceed the initial amount of rewards
use rule getClaimableRewardsBefore_leq_claimed_claimRewardsOnBehalf

// stataToken total supply equal sum of all balances
invariant totalSupplyInvariant()
    totalSupply() == sumAllBalance()
    filtered { f -> !untestedFunctions(f)}


// Unclaimed rewards always less than Claimable rewards
rule unclaimedLessThanClaimableRule(env e) {
    address user;

    mathint _unclaimed = getUnclaimedRewards(user, _DummyERC20_rewardToken);
    mathint _claimable = getClaimableRewards(e, user, _DummyERC20_rewardToken);

    assert _unclaimed <= _claimable;
}

// Unclaimed rewards unchanged by any function expect those changing share balance and claims
rule unclaimedUnchangedRule(method f, env e, calldataarg args) filtered {
    f -> !depositFunctions(f) && !withdrawFunctions(f)
      && !claimFunctions(f)   && !transferFunctions(f)
      && !untestedFunctions(f)
}{
    address user;

    mathint _unclaimed = getUnclaimedRewards(user, _DummyERC20_rewardToken);
    f(e, args);
    mathint unclaimed_ = getUnclaimedRewards(user, _DummyERC20_rewardToken);

    assert unclaimed_ == _unclaimed;
}

// Claimable rewards unchanged by any function expect those changing share balance and claims
rule claimableUnchangedRule(method f, env e, calldataarg args) filtered {
    f -> !depositFunctions(f) && !withdrawFunctions(f)
      && !claimFunctions(f)   && !transferFunctions(f)
      && !untestedFunctions(f)
      &&  f.selector != initialize(address,string,string).selector
}{
    address user;

    single_RewardToken_setup();

    mathint _claimable = getClaimableRewards(e, user, _DummyERC20_rewardToken);
    f(e, args);
    mathint claimable_ = getClaimableRewards(e, user, _DummyERC20_rewardToken);

    assert claimable_ == _claimable;
}

// total assets unchanged by any function except deposit, withdraw and claim functions
rule totalAssetsUnchangedRule(method f) filtered {
    f -> !depositFunctions(f) && !withdrawFunctions(f) && !claimFunctions(f) && !untestedFunctions(f)
}{
    env e; calldataarg args;

    mathint _totalAssets = totalAssets(e);
    f(e, args);
    mathint totalAssets_ = totalAssets(e);

    assert totalAssets_ == _totalAssets;
}

// Initialize function cannot be called twice
rule initializeCannotBeCalledTwice(env e, calldataarg args) {
    initialize(e, args);
    initialize@withrevert(e, args);

    assert lastReverted, "Initialize cannot be called twice";
}

// deposit more aToken gives more stataToken
rule depositMoreRule(env e) {
    storage initial = lastStorage;

    address user;
    uint256 aTokenAmount1;
    uint256 aTokenAmount2;
    mathint stataTokenBal = balanceOf(user);
    require stataTokenBal == 0;

    deposit(e, aTokenAmount1, user) at initial;
    mathint stataTokenBal1 = balanceOf(user);

    deposit(e, aTokenAmount2, user) at initial;
    mathint stataTokenBal2 = balanceOf(user);

    assert aTokenAmount1 <= aTokenAmount2 => stataTokenBal1 <= stataTokenBal2;
}

// claimed rewards are at most claimable rewards
rule claimRewardsRule_10(env e) {
    address user = e.msg.sender;
    require user != 0;

    // setupUser(e, user);
    // single_RewardToken_setup();

    mathint _unclaimed = getUnclaimedRewards(user, _DummyERC20_rewardToken);
    mathint _claimable = getClaimableRewards(e, user, _DummyERC20_rewardToken);
    mathint _balUser   = _DummyERC20_rewardToken.balanceOf(user);
    mathint _balContract = _DummyERC20_rewardToken.balanceOf(currentContract);

    uint256 ether = 1000000000000000000;
    require _unclaimed   >= 1 * ether;
    require _claimable   >= 1 * ether;
    require _balUser     <= 1 * ether;
    require _balContract >= 1000 * ether;
    require _balContract <= 1000000000 * ether;

    address[] rewards;
    require rewards[0] == _DummyERC20_rewardToken;
    require rewards.length == 1;


    claimRewards@withrevert(e, user, rewards);

    mathint unclaimed_ = getUnclaimedRewards(user, _DummyERC20_rewardToken);
    mathint claimable_ = getClaimableRewards(e, user, _DummyERC20_rewardToken);
    mathint balUser_   = _DummyERC20_rewardToken.balanceOf(user);
    mathint balContract_ = _DummyERC20_rewardToken.balanceOf(currentContract);

    assert balUser_ >= _balUser;
    assert balUser_ <= _balUser + _claimable;

    assert balContract_ <= _balContract;
}

// redeem Token must be less than maxRedeem
rule redeemLessThanMaxRedeem(env e, calldataarg args) {
    address owner;
    address receiver;
    bool toUnderlying = true;

    uint256 _maxRedeem = maxRedeem(owner);

    uint256 redeem_;
    uint256 aToken_;
    redeem_, aToken_ = redeem(e, _maxRedeem, receiver, owner, toUnderlying);

    assert  redeem_ <= _maxRedeem;
}
