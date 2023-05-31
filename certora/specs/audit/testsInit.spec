import "common/definitions.spec"
import "common/functions.spec"

import "methods/methods_base.spec"

import "methods/staticATokenLM.spec"
import "methods/aToken.spec"
import "methods/aTokenUnderlying.spec"
import "methods/symbolicLendingPool.spec"
import "methods/transferStrategy.spec"
import "methods/rewardsController.spec"
import "methods/rewardToken.spec"

import "rules/claimRewards.spec"
import "rules/staticATokenLM_base.spec"
import "rules/erc4626_base.spec"
import "rules/erc4626.spec"
import "rules/totalAssets.spec"
import "rules/metaDeposit.spec"
import "rules/totalAssetsFails.spec"

import "invariants/invariants.spec"
import "invariants/invariantsFails.spec"

using ATokenHarness as _AToken
using StaticATokenLMHarness as _StaticATokenLM
using SymbolicLendingPool as _SymbolicLendingPool
using RewardsControllerHarness as _RewardsController
using TransferStrategyHarness as _TransferStrategy
using DummyERC20_rewardToken as _DummyERC20_rewardToken
using DummyERC20_aTokenUnderlying as _DummyERC20_aTokenUnderlying

using PermitERC20_aTokenUnderlying as _PermitERC20_aTokenUnderlying

use invariant totalSupplyIsSumOfBalances
