#!/bin/sh

cp certora/specs/tests.$1.spec certora/specs/tests.spec
certoraRun certora/conf/tests.conf --msg test_$1
