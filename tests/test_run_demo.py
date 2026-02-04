# tests/test_run_demo.py
import json, subprocess, uuid, pathlib

def test_demo_run(tmp_path):
    out_dir = tmp_path / "out"
    subprocess.check_call(
        ["python", "-m", "xyraiq.cli", "examples/tier1_demo.yaml", "--out", str(out_dir)]
    )
    json_file = next(out_dir.glob("*.json"))
    data = json.loads(json_file.read_text())
    assert "hallucinations" in data["scores"]
