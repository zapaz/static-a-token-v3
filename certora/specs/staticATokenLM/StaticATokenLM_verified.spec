import "../methods/methods_base.spec"
import "./StaticATokenLM_base.spec"
import "./metaDeposit.spec"

/////////////////// Methods ////////////////////////

////////////////// FUNCTIONS //////////////////////

///////////////// Properties ///////////////////////

use invariant singleAssetAccruedRewards
use invariant totalSupplyEqualSumAllBalances

use rule getClaimableRewardsBefore_leq_claimed_claimRewardsOnBehalf
use rule metaDepositFailsWithUnderlyingWithNoPermitRule

