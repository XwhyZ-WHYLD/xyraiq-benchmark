![Stress Signature badge](https://img.shields.io/badge/Stress--Signature-silver-75%2F100-informational)

# Xyraiq™ – Cognitive Resilience Benchmark for LLMs

> **Stress‑test any language model for memory, logic, ethics, and spiritual reasoning – get a cryptographically signed ****Stress Signature™**** in under 5 minutes.**

---

## Why Xyraiq?

| Gap in today’s evals                   | How Xyraiq closes it                                            |
| -------------------------------------- | --------------------------------------------------------------- |
| Single‑shot prompts only               | Multi‑turn **Session Orchestrator** runs 50‑100 rounds          |
| No fatigue / memory decay metrics      | Detector Array tracks drift & contradiction over time           |
| Lacks ethical & spiritual logic probes | Tier‑3 prompt packs inject metaphors, scripture, paradox        |
| Hard to verify results                 | Hash‑based **Stress Signature™** makes every run tamper‑evident |

---

## Quick Start (CLI)

```bash
pip install xyraiq
xyraiq run examples/tier1_demo.yaml --model gpt-4o --out ./results
```

Outputs a JSON scorecard & signed badge ready for your README.

---

## System Architecture

1. **Prompt Injector** – loads persona & tier packs.
2. **Session Orchestrator** – drives the dialogue.
3. **Detector Array** – hallucination, contradiction, tone drift, guardrails.
4. **Scoring Engine** – weighted aggregation → 0‑100.
5. **Export Pipeline** – JSON, PDF, badge, Stress Signature hash.

---

## Stress Tiers

| Tier                  | Turns  | Complexity             | Symbolic Load             |
| --------------------- | ------ | ---------------------- | ------------------------- |
| **T1 – Basic**        | 10     | Single‑domain          | None                      |
| **T2 – Intermediate** | 30     | Multi‑domain           | Light metaphor            |
| **T3 – Elite**        | 50‑100 | Multi‑domain + fatigue | Heavy spiritual & paradox |

---

## Sample Scorecard

```json
{
  "session_id": "123e4567",
  "model": "gpt-4o",
  "tier": 3,
  "scores": {
    "hallucinations": 2,
    "contradictions": 1,
    "tone_drift": 0,
    "aggregate": 92,
    "badge": "Platinum"
  },
  "stress_signature": "a1b2c3d4..."
}
```

---

## Roadmap

* **v0.1‑alpha** – Open spec, Tier‑1 prompt pack, CLI runner
* **v0.2** – Detector plugins (tone, ethics), Tier‑2 packs
* **v0.3** – Tier‑3 packs, dashboard UI, multilingual support
* **v1.0** – Certification portal & SaaS badging

---

## License

* Core spec & CLI: **Apache‑2.0**
* Premium prompt packs & scoring weights: **Commercial license, patent pending**

---

## Citation

If you use Xyraiq in academic work, please cite:

```bibtex
@misc{xyraiq2026,
  title  = {Xyraiq: A Cognitive Resilience Benchmark for Large Language Models},
  author = {George N. and contributors},
  year   = {2026},
  howpublished = {GitHub},
  url    = {https://github.com/xwhyz/xyraiq-benchmark}
}
```

---

## Contributing

1. Fork repo & create feature branch.
2. Write tests for your change.
3. Open PR linked to an open issue.

We operate under a Contributor License Agreement (CLA) – see *CONTRIBUTING.md* for details.

---
