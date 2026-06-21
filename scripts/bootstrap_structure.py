#!/usr/bin/env python3
"""
Bootstrap the entire project structure with empty files.
Usage:  python scripts/bootstrap_structure.py
"""
from pathlib import Path

STRUCTURE = {
    # ----- Root -----
    "": [
        "README.md", "LICENSE", "pyproject.toml",
        "docker-compose.yml", ".env.example", ".gitignore",
    ],

    # ----- apps/api -----
    "apps/api":              ["__init__.py", "main.py"],
    "apps/api/routes":       ["__init__.py", "chat.py", "voice.py", "admin.py"],
    "apps/api/middleware":   ["__init__.py", "auth.py", "consent.py", "audit.py"],

    # ----- apps/agents -----
    "apps/agents": [
        "__init__.py", "base.py", "orchestrator.py",
        "triage.py", "history.py", "scheduling.py",
        "communication.py", "escalation.py",
    ],
    "apps/agents/shared":    ["__init__.py", "config.py", "llm.py",
                              "schemas.py", "prompts.py", "tools.py"],

    # ----- apps/rag -----
    "apps/rag":              ["__init__.py", "embedder.py", "retriever.py",
                              "reranker.py", "indexer.py"],

    # ----- apps/channels -----
    "apps/channels":         ["__init__.py", "twilio_voice.py",
                              "twilio_sms.py", "asr_tts.py"],

    # ----- apps/eval -----
    "apps/eval":             ["__init__.py", "ragas_eval.py",
                              "triage_accuracy.py", "conversation_traces.py"],

    # ----- data -----
    "data/synthetic":        ["patients.json"],
    "data/knowledge":        ["triage_protocols.json"],
    "data/eval":             ["gold_cases.json"],

    # ----- infra -----
    "infra/docker":          ["Dockerfile"],

    # ----- docs -----
    "docs":                  ["business-proposal.md", "technical-framework.md",
                              "dpia.md", "api.md", "runbook.md"],

    # ----- scripts -----
    "scripts":               ["seed_kb.py", "demo.py", "bootstrap_structure.py"],

    # ----- tests -----
    "tests":                 ["__init__.py"],
    "tests/unit":            ["__init__.py", "test_agents.py", "test_rag.py"],
    "tests/integration":     ["__init__.py", "test_orchestrator.py"],
    "tests/e2e":             ["__init__.py", "test_patient_journey.py"],
}

def main():
    base = Path.cwd()
    print(f"\nCreating project structure in: {base}\n")
    print("─" * 60)

    for folder, files in STRUCTURE.items():
        dir_path = base / folder if folder else base
        dir_path.mkdir(parents=True, exist_ok=True)
        label = folder + "/" if folder else "(root)"
        print(f"\n {label}")
        for filename in files:
            (dir_path / filename).touch(exist_ok=True)
            print(f" {filename}")

    print("\n" + "─" * 60)
    print(f"\n Done. Created {sum(len(f) for f in STRUCTURE.values())} files "
          f"in {len(STRUCTURE)} folders.\n")

if __name__ == "__main__":
    main()