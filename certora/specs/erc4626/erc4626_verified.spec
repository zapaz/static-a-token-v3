import "erc4626_base.spec"

// The following spec implements erc4626 properties according to the official eip described here:
// https://eips.ethereum.org/EIPS/eip-4626

///////////////// Properties ///////////////////////

use rule previewWithdrawIndependentOfMaxWithdraw1
use rule previewWithdrawIndependentOfMaxWithdraw2
use rule amountConversionRoundedDown
use rule sharesConversionRoundedDown
use rule maxRedeemMustntRevert
