from aisupport import FastPathMatcher, HITLSilenceTracker, DebounceBuffer, StyleSanitizer
import time

def test_fast_path():
    matcher = FastPathMatcher()
    assert matcher.match("ta ok") is not None
    assert matcher.match("valeu!!") is not None
    assert matcher.match("bom dia") is not None
    assert matcher.match("meu pix nao caiu no app") is None

def test_hitl_silence():
    tracker = HITLSilenceTracker(cooldown_hours=0.001) # ~3.6s
    assert not tracker.is_muted(123)
    tracker.record_human_intervention(123)
    assert tracker.is_muted(123)

def test_debounce():
    db = DebounceBuffer(debounce_seconds=0.1)
    db.append(1, "Ola")
    db.append(1, "preciso de ajuda")
    time.sleep(0.15)
    assert db.should_flush(1)
    assert db.flush(1) == "Ola\npreciso de ajuda"

def test_sanitizer():
    raw = "Sou o assistente virtual da NetHub. Seu plano expira amanha."
    cleaned = StyleSanitizer.clean(raw)
    assert "Sou o assistente" not in cleaned
    assert "Seu plano expira amanha." in cleaned
