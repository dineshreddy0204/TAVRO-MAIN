"""Tests for speech configuration."""

from tavro.core.config import TavroConfig, SpeechConfig


def test_speech_config_defaults():
    cfg = SpeechConfig()
    assert cfg.backend == "auto"
    assert cfg.model == "base"
    assert cfg.language == ""
    assert cfg.device == "auto"
    assert cfg.compute_type == "float16"


def test_tavro_config_has_speech():
    cfg = TavroConfig()
    assert hasattr(cfg, "speech")
    assert isinstance(cfg.speech, SpeechConfig)
    assert cfg.speech.backend == "auto"


def test_tavro_system_has_speech_backend():
    """TavroSystem has a speech_backend attribute."""
    from tavro.system import TavroSystem

    assert "speech_backend" in TavroSystem.__dataclass_fields__
