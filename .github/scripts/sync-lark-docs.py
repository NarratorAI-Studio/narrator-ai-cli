#!/usr/bin/env python3
"""
Sync GitHub docs/*.md to their mapped Lark docs.

Reads `docs/lark-sync.yml` (manifest of {file → doc_token}), determines which
markdown files changed in this commit, and pushes each via:

    lark-cli docs +update --doc <token> --markdown @<file> --mode overwrite

Env:
    FORCE_ALL=1   sync every doc in manifest (ignore git diff)

Designed to run in GitHub Actions after `actions/checkout@...` with fetch-depth: 2.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
MANIFEST = REPO_ROOT / "docs" / "lark-sync.yml"

def fail(msg, code=1):
    print(f"::error::{msg}", file=sys.stderr)
    sys.exit(code)

def load_manifest():
    if not MANIFEST.exists():
        fail(f"manifest not found: {MANIFEST}")
    data = yaml.safe_load(MANIFEST.read_text())
    docs = data.get("docs") or []
    if not docs:
        fail("manifest has no docs entries")
    return docs

def changed_files():
    """Files changed in HEAD vs HEAD~1, restricted to docs/*.md."""
    if os.environ.get("FORCE_ALL"):
        return None  # signal "all"
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", "HEAD~1", "HEAD", "--", "docs/*.md"],
            text=True,
        ).strip()
    except subprocess.CalledProcessError as e:
        # First commit on branch / shallow clone: fall back to "all"
        print(f"::warning::git diff failed ({e}); syncing all docs")
        return None
    if not out:
        return set()
    return {Path(p).name for p in out.splitlines()}

def push_doc(doc_token: str, md_path: Path):
    md_path = REPO_ROOT / "docs" / md_path
    if not md_path.exists():
        return False, f"file not found: {md_path}"
    proc = subprocess.run(
        [
            "lark-cli", "docs", "+update",
            "--doc", doc_token,
            "--markdown", md_path.read_text(),
            "--as", "bot",
            "--mode", "overwrite",
        ],
        capture_output=True, text=True
    )
    if proc.returncode != 0:
        return False, f"lark-cli exit {proc.returncode}: {proc.stderr[:400]}"
    # Try to parse response
    try:
        resp = json.loads(proc.stdout)
        if not resp.get("ok", False):
            return False, f"lark-cli reported not-ok: {proc.stdout[:300]}"
    except json.JSONDecodeError:
        pass  # tolerate text output
    return True, "ok"

def main():
    docs = load_manifest()
    changed = changed_files()
    if changed is None:
        print(f"::notice::syncing ALL {len(docs)} docs")
        targets = docs
    else:
        # Always include lark-sync.yml-only edits as a "no-op" (no markdown to push)
        targets = [d for d in docs if d["file"] in changed]
        print(f"::notice::changed markdown files: {sorted(changed)}")
        print(f"::notice::matched manifest entries: {len(targets)}")
        if not targets:
            print("::notice::nothing to sync; exiting cleanly")
            return

    failures = []
    for d in targets:
        title = d.get("title", d["file"])
        token = d["doc_token"]
        print(f"\n→ {d['file']}  →  Lark «{title}»")
        ok, info = push_doc(token, d["file"])
        if ok:
            print(f"  ✓ {info}")
        else:
            print(f"  ✗ {info}")
            failures.append((d["file"], info))

    if failures:
        print("\n::error::sync failed for:")
        for f, info in failures:
            print(f"  - {f}: {info}")
        sys.exit(1)
    print(f"\n✓ {len(targets)} doc(s) synced to Lark")

if __name__ == "__main__":
    main()
