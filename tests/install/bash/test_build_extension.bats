#!/usr/bin/env bats

setup() {
    TEST_TMPDIR=$(mktemp -d)
    export TAVRO_HOME="$TEST_TMPDIR/.tavro"
    mkdir -p "$TAVRO_HOME/.state"
    mkdir -p "$TAVRO_HOME/src/rust/crates/tavro-python"
    touch "$TAVRO_HOME/src/rust/crates/tavro-python/Cargo.toml"
    export UV_STUB_LOG="$TEST_TMPDIR/uv.log"
    : > "$UV_STUB_LOG"
    export PATH="$BATS_TEST_DIRNAME/stubs:$PATH"
    export SCRIPT="$BATS_TEST_DIRNAME/../../../scripts/install/build-extension.sh"
}

teardown() {
    [[ -n "${TEST_TMPDIR:-}" ]] && rm -rf "$TEST_TMPDIR"
}

@test "writes extension-built marker on success" {
    UV_STUB_EXIT=0 run bash "$SCRIPT"
    [ "$status" -eq 0 ]
    [ -f "$TAVRO_HOME/.state/extension-built" ]
}

@test "writes extension-failed marker on failure" {
    UV_STUB_EXIT=1 run bash "$SCRIPT"
    [ "$status" -ne 0 ]
    [ -f "$TAVRO_HOME/.state/extension-failed" ]
    [ -s "$TAVRO_HOME/.state/extension-failed" ]
}

@test "removes prior failed marker on success" {
    touch "$TAVRO_HOME/.state/extension-failed"
    UV_STUB_EXIT=0 run bash "$SCRIPT"
    [ ! -f "$TAVRO_HOME/.state/extension-failed" ]
    [ -f "$TAVRO_HOME/.state/extension-built" ]
}

@test "calls uv run maturin develop with the right manifest" {
    UV_STUB_EXIT=0 run bash "$SCRIPT"
    grep -q "run maturin develop -m" "$UV_STUB_LOG"
    grep -q "rust/crates/tavro-python/Cargo.toml" "$UV_STUB_LOG"
}

@test "atomic rename — no .tmp file left behind" {
    UV_STUB_EXIT=0 run bash "$SCRIPT"
    leftover=$(find "$TAVRO_HOME/.state" -name "*.tmp" 2>/dev/null | wc -l)
    [ "$leftover" -eq 0 ]
}
