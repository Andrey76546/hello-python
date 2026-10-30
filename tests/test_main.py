import sys

from main import main


def test_main_output(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["hello-python", "demo"])

    assert main() == 0
    output = capsys.readouterr().out
    assert "hello-python version 1.0.0" in output
    assert "Hello, GitHub!" in output
    assert "Sum 1..10 = 55" in output
    assert "1: demo" in output
