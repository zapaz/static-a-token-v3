import "testsInit.spec"

// OK
use invariant totalSupplyIsSumOfBalances



use invariant singleAssetAccruedRewards
use invariant assetsMoreThanSupply
use invariant noAssetsIfNoSupply
use invariant noSupplyIfNoAssets
use invariant sumOfBalancePairsBounded
use invariant totalAssetsSupplyZero


use invariant vaultSolvency

use invariant zeroAssetsSupplyInvariant

use rule depositMonotonicity
use rule totalsMonotonicity
use rule underlyingCannotChange
use rule dustFavorsTheHouse
use rule redeemingAllValidity
use rule contributingProducesShares
use rule onlyContributionMethodsReduceAssets
use rule reclaimingProducesAssets
