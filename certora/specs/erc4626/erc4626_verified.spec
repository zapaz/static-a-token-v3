import "erc4626_base.spec"

// The following spec implements erc4626 properties according to the official eip described here:
// https://eips.ethereum.org/EIPS/eip-4626

///////////////// Properties ///////////////////////

use rule previewWithdrawIndependentOfMaxWithdraw1
use rule previewWithdrawIndependentOfMaxWithdraw2
use rule amountConversionRoundedDown
use rule sharesConversionRoundedDown
use rule maxRedeemMustntRevert

rule conversionOfZero(env e) {
    uint256 convertZeroShares = convertToAssets(e, 0);
    uint256 convertZeroAssets = convertToShares(e, 0);

    assert convertZeroShares == 0,
        "converting zero shares must return zero assets";
    assert convertZeroAssets == 0,
        "converting zero assets must return zero shares";

}

rule zeroDepositZeroShares_04(env e)
{
    uint256 assets; address receiver;

    uint256 shares = deposit(e, assets, receiver);

    assert shares == 0 <=> assets == 0;
}

rule convertToAssetsWeakAdditivity_05 (env e) {
    uint256 sharesA; uint256 sharesB;
    require sharesA + sharesB < max_uint128
         && convertToAssets(e, sharesA) + convertToAssets(e, sharesB) < max_uint256
         && convertToAssets(e, sharesA + sharesB) < max_uint256;

    assert convertToAssets(e, sharesA) + convertToAssets(e, sharesB) <= convertToAssets(e, sharesA + sharesB),
        "converting sharesA and sharesB to assets then summing them must yield a smaller or equal result to summing them then converting";
}

rule conversionWeakIntegrity(env e) {
    uint256 sharesOrAssets;

    assert convertToShares(e, convertToAssets(e, sharesOrAssets)) <= sharesOrAssets,
        "converting shares to assets then back to shares must return shares less than or equal to the original amount";
    assert convertToAssets(e, convertToShares(e, sharesOrAssets)) <= sharesOrAssets,
        "converting assets to shares then back to assets must return assets less than or equal to the original amount";
}

rule convertToCorrectness(env e)
{
    uint256 amount; uint256 shares;

    assert amount >= convertToAssets(e, convertToShares(e, amount));
    assert shares >= convertToShares(e, convertToAssets(e, shares));
}

rule convertToSharesWeakAdditivity(env e) {
    uint256 assetsA; uint256 assetsB;
    require assetsA + assetsB < max_uint128
         && convertToAssets(e, assetsA) + convertToAssets(e, assetsB) < max_uint256
         && convertToAssets(e, assetsA + assetsB) < max_uint256;

    assert convertToAssets(e, assetsA) + convertToAssets(e, assetsB) <= convertToAssets(e, assetsA + assetsB),
        "converting assetsA and assetsB to shares then summing them must yield a smaller or equal result to summing them then converting";
}

rule conversionWeakMonotonicity(env e) {
    uint256 smallerShares; uint256 largerShares;
    uint256 smallerAssets; uint256 largerAssets;

    assert smallerShares < largerShares => convertToAssets(e, smallerShares) <= convertToAssets(e, largerShares),
        "converting more shares must yield equal or greater assets";
    assert smallerAssets < largerAssets => convertToShares(e, smallerAssets) <= convertToShares(e, largerAssets),
        "converting more assets must yield equal or greater shares";
}
