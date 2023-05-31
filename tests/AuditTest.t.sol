// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.10;

import 'forge-std/Test.sol';
import {AToken} from 'aave-v3-core/contracts/protocol/tokenization/AToken.sol';
import {DataTypes, ReserveConfiguration} from 'aave-v3-core/contracts/protocol/libraries/configuration/ReserveConfiguration.sol';
import {StaticATokenLM, IERC20, IERC20Metadata, ERC20} from '../src/StaticATokenLM.sol';
import {RayMathExplicitRounding, Rounding} from '../src/RayMathExplicitRounding.sol';
import {IStaticATokenLM} from '../src/interfaces/IStaticATokenLM.sol';
import {SigUtils} from './SigUtils.sol';
import {BaseTest} from './TestBase.sol';

import {TransparentProxyFactory} from 'solidity-utils/contracts/transparent-proxy/TransparentProxyFactory.sol';
import {AaveV3Avalanche, IPool} from 'aave-address-book/AaveV3Avalanche.sol';


contract StaticATokenLMTest is BaseTest {
  using RayMathExplicitRounding for uint256;

  address public constant override UNDERLYING = 0x49D5c2BdFfac6CE2BFdB6640F4F80f226bc10bAB;
  address public constant override A_TOKEN = 0xe50fA9b3c56FfB159cB0FCA61F5c9D750e8128c8;
  address public constant EMISSION_ADMIN = 0xCba0B614f13eCdd98B8C0026fcAD11cec8Eb4343;

  IPool public override pool = IPool(AaveV3Avalanche.POOL);

  address[] rewardTokens;

  function REWARD_TOKEN() public returns (address) {
    return rewardTokens[0];
  }

  function setUp() public override {
    vm.createSelectFork(vm.rpcUrl('avalanche'), 25016463);
    rewardTokens.push(0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7);

    super.setUp();
  }

  function testAudit1() public {
  }
}
