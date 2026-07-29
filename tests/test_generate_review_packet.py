from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.generate_review_packet import build_packet


class GenerateReviewPacketTest(unittest.TestCase):
    def test_build_packet_includes_counts_and_sections(self):
        packet = build_packet(
            date(2026, 7, 29),
            candidates=[
                {
                    "id": "lit-a",
                    "title": "A",
                    "state": "needs_human_review",
                    "actionability": "reading_candidate",
                }
            ],
            recommended_upgrades=[],
            recommended_rejects=[],
            review_needed=[{"id": "lit-a"}],
            benchmarks=[
                {
                    "id": "bench-a",
                    "system": "H2",
                    "observable": "total_cross_section",
                    "status": "candidate",
                    "target_phase": "Phase G",
                }
            ],
            risks=[
                {
                    "id": "risk-a",
                    "claim": "claim",
                    "evidence": "evidence",
                    "project_impact": "impact",
                }
            ],
        )

        self.assertIn("# Literature Review Packet: 2026-07-29", packet)
        self.assertIn("- New candidates: 1", packet)
        self.assertIn("## Benchmark Updates", packet)
        self.assertIn("bench-a", packet)
        self.assertIn("risk-a", packet)


if __name__ == "__main__":
    unittest.main()
