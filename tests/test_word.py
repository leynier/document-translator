# ruff: noqa: E402
import os
from pathlib import Path
from docx import Document
from pytest import MonkeyPatch

os.environ.setdefault("OPENAI_API_KEY", "test")

from doculingo import word


def test_segmentation(monkeypatch: MonkeyPatch, tmp_path: Path) -> None:
    doc = Document()
    texts = []
    for i in range(250):
        text = f"text {i}"
        texts.append(text)
        doc.add_paragraph(text)
    input_file = tmp_path / "input.docx"
    doc.save(str(input_file))
    output_file = tmp_path / "output.docx"

    segments: list[list[str]] = []

    def fake_translate(items: list[str], ls: str, lt: str) -> list[str]:
        segments.append(list(items))
        return list(items)

    monkeypatch.setattr(word, "get_translator", lambda _: fake_translate)

    word.main(
        input=input_file,
        output=str(output_file),
        language_source="es",
        language_target="en",
    )

    step = len(texts) // 100
    expected = [texts[i : i + step] for i in range(0, len(texts), step)]
    assert segments == expected
    assert output_file.exists()
