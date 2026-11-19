"""Smoke test that the tmp_tavro_home fixture works."""

from __future__ import annotations

from pathlib import Path

from tavro.core import config as config_mod


def test_fixture_redirects_default_config_dir(tmp_tavro_home: Path) -> None:
    assert config_mod.DEFAULT_CONFIG_DIR == tmp_tavro_home
    assert tmp_tavro_home.exists()
    assert (tmp_tavro_home / ".state").exists()
    assert (tmp_tavro_home / ".state" / "models").exists()


def test_fixture_redirects_config_path(tmp_tavro_home: Path) -> None:
    assert config_mod.DEFAULT_CONFIG_PATH == tmp_tavro_home / "config.toml"
