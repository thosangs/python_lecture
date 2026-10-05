"""Jalankan ulang notebook supaya output tersimpan di file .ipynb.

Pakai:
    python tools/run_notebooks.py                       # jalankan notebook materi & kunci
    python tools/run_notebooks.py notebooks/xxx.ipynb   # jalankan notebook tertentu

Cell yang memakai input() diberi jawaban otomatis lewat metadata cell:
    "metadata": {"mock_input": ["Raka Pratama", "05-10-2026"]}
Jawaban dicetak seperti saat diketik di Colab, misalnya "Nama analis: Raka Pratama".

Error yang sengaja dibuat (NameError, TypeError, dst.) tetap disimpan sebagai output.
"""

import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_NOTEBOOKS = [
    ROOT / "notebooks" / "01_materi_kopi_senja.ipynb",
    ROOT / "notebooks" / "03_kunci_jawaban.ipynb",
]

SETUP_CODE = """
import builtins as __b
__mock_q = []
def __mock_input(prompt=""):
    jawaban = __mock_q.pop(0) if __mock_q else ""
    print(f"{prompt}{jawaban}")
    return jawaban
__b.input = __mock_input
get_ipython().kernel.raw_input = __mock_input   # ipykernel memasang ulang input() tiap eksekusi
"""


def run_hidden(client, code):
    # execute_cell menaruh hasilnya di nb.cells[index], jadi kembalikan cell aslinya
    saved = client.nb.cells[0]
    client.execute_cell(nbformat.v4.new_code_cell(code), 0, store_history=False)
    client.nb.cells[0] = saved


def run_notebook(path):
    nb = nbformat.read(path, as_version=4)
    client = NotebookClient(
        nb,
        timeout=120,
        kernel_name="python3",
        allow_errors=True,
        resources={"metadata": {"path": str(path.parent)}},
    )
    count = 0
    with client.setup_kernel():
        run_hidden(client, SETUP_CODE)
        for index, cell in enumerate(nb.cells):
            if cell.cell_type != "code":
                continue
            mock = cell.metadata.get("mock_input")
            if mock:
                run_hidden(client, f"__mock_q[:] = {list(mock)!r}")
            count += 1
            client.execute_cell(cell, index, execution_count=count)
    nbformat.write(nb, path)
    print(f"✔ {path.relative_to(ROOT)} ({count} code cell)")


if __name__ == "__main__":
    targets = [Path(p).resolve() for p in sys.argv[1:]] or DEFAULT_NOTEBOOKS
    for target in targets:
        run_notebook(target)
