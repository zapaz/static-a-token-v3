import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"

// FAILS ROUNDING ?

// check rewards claimed are equal to claimable  rewards ?
// bug1
rule claimRewardsRule_10(env e) {
    address user;
    require user != 0;

    setupUser(e, user);
    single_RewardToken_setup();

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
    mathint balContract_ = _DummyERC20_rewardToken.balanceOf(user);

    assert balUser_ >= _balUser;
    assert balUser_ <= _balUser + _claimable;
    assert balUser_ <= _balUser + _unclaimed;

    assert balContract_ <= _balContract;
}