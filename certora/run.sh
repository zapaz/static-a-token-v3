#!/bin/sh

certoraRun certora/conf/tests.conf
certoraRun certora/conf/testsOK.conf
certoraRun certora/conf/testsKO.conf