import "methods/methods_base.spec"

rule underlyingCannotChange(method f, env e, calldataarg args) filtered {
    f -> !untestedFunctions(f)
}{
    address originalAsset = asset();

    f(e, args);

    address newAsset = asset();

    assert originalAsset == newAsset,
        "the underlying asset of a contract must not change";
}
