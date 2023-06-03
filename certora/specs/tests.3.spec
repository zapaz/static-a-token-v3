import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"

rule depositMoreRule_03(env e) {
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