import "methods/methods_base.spec"
import "staticATokenLM/StaticATokenLM_base.spec"

// FALSE
// try more loose rule... existing one ?

invariant zeroAssetsSupplyInvariant_08(env e)
    totalAssets(e) == 0 <=> totalSupply() == 0
    {
        preserved with (env ep) {
            setupUser( ep, ep.msg.sender);
        }
    }
