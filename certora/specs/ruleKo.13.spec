import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"

// ???

// FALSE
rule mintRule_13a(env e) {
    uint256 shares;
    address user;

    mathint _previewAssets = previewMint(e, shares);

    mathint _balAssets = _AToken.balanceOf(e, user);
    mathint _balShares = balanceOf(user);

    mint(e, shares, user);

    mathint balAssets_ = _AToken.balanceOf(e, user);
    mathint balShares_ = balanceOf(user);

    assert balAssets_ == _balAssets + _previewAssets;
    assert balShares_ == _balShares + shares;
}

// FALSE
rule mintRule_13b(env e) {
    uint256 shares;
    address user;

    mathint _previewAssets = previewMint(e, shares);

    mathint _balAssets = _AToken.balanceOf(e, user);
    mathint _balShares = balanceOf(user);
    mint(e, shares, user);
    mathint balAssets_ = _AToken.balanceOf(e, user);
    mathint balShares_ = balanceOf(user);

    assert balShares_ >= _balShares;
    assert balShares_ <= _balShares + shares;

    assert balAssets_ >= _balAssets;
    assert balAssets_ <= _balAssets + _previewAssets;
}

// TIMEOUT
rule mintRule_13c(env e) {
    uint256 shares;
    address user;

    setupUser(e, user);

    mathint _balAssets = _AToken.balanceOf(e, user);
    mathint _balShares = balanceOf(user);

    mint(e, shares, user);

    mathint balAssets_ = _AToken.balanceOf(e, user);
    mathint balShares_ = balanceOf(user);

    assert balAssets_ >= _balAssets;
    assert balShares_ >= _balShares;
    assert balShares_ <= _balShares + shares;
}
