from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.validate_registry import validate


def write_registry(root: Path, candidates: str, core: str, benchmarks: str, risks: str):
    registry = root / "registry"
    registry.mkdir()
    (registry / "candidates.yaml").write_text(candidates, encoding="utf-8")
    (registry / "core.yaml").write_text(core, encoding="utf-8")
    (registry / "benchmarks.yaml").write_text(benchmarks, encoding="utf-8")
    (registry / "risks.yaml").write_text(risks, encoding="utf-8")
    return registry


class ValidateRegistryTest(unittest.TestCase):
    def test_empty_registries_are_valid(self):
        with TemporaryDirectory() as tmp:
            registry = write_registry(
                Path(tmp),
                "items: []\n",
                "items: []\n",
                "benchmarks: []\n",
                "risks: []\n",
            )

            self.assertEqual(validate(registry), [])

    def test_missing_required_literature_field_is_reported(self):
        with TemporaryDirectory() as tmp:
            registry = write_registry(
                Path(tmp),
                """
items:
  - id: "lit-example"
    title: "Example"
    authors: ["A"]
    year: 2026
    source_type: "paper"
    state: "discovered"
    review_status: "unreviewed"
    relevance: "medium"
    role: ["frontier"]
    confidence: "metadata_only"
""",
                "items: []\n",
                "benchmarks: []\n",
                "risks: []\n",
            )

            errors = validate(registry)

            self.assertTrue(any("actionability" in error for error in errors))

    def test_invalid_enum_is_reported(self):
        with TemporaryDirectory() as tmp:
            registry = write_registry(
                Path(tmp),
                """
items:
  - id: "lit-example"
    title: "Example"
    authors: ["A"]
    year: 2026
    source_type: "blog"
    state: "discovered"
    review_status: "unreviewed"
    relevance: "medium"
    role: ["frontier"]
    confidence: "metadata_only"
    actionability: "reading_candidate"
""",
                "items: []\n",
                "benchmarks: []\n",
                "risks: []\n",
            )

            errors = validate(registry)

            self.assertTrue(any("invalid source_type" in error for error in errors))

    def test_duplicate_ids_are_reported_across_registries(self):
        with TemporaryDirectory() as tmp:
            registry = write_registry(
                Path(tmp),
                """
items:
  - id: "shared-id"
    title: "Example"
    authors: ["A"]
    year: 2026
    source_type: "paper"
    state: "discovered"
    review_status: "unreviewed"
    relevance: "medium"
    role: ["frontier"]
    confidence: "metadata_only"
    actionability: "reading_candidate"
""",
                "items: []\n",
                """
benchmarks:
  - id: "shared-id"
    literature_id: "lit-example"
    system: "H2"
    observable: "total_cross_section"
    data_availability: "figure_digitizable"
    source_location: "figure 2"
    target_phase: "Phase G"
    status: "candidate"
""",
                "risks: []\n",
            )

            errors = validate(registry)

            self.assertTrue(any("duplicate id: shared-id" in error for error in errors))

    def test_duplicate_doi_is_reported(self):
        with TemporaryDirectory() as tmp:
            literature = """
items:
  - id: "lit-one"
    title: "Example One"
    authors: ["A"]
    year: 2026
    source_type: "paper"
    doi: "10.1234/example"
    state: "discovered"
    review_status: "unreviewed"
    relevance: "medium"
    role: ["frontier"]
    confidence: "metadata_only"
    actionability: "reading_candidate"
  - id: "lit-two"
    title: "Example Two"
    authors: ["B"]
    year: 2026
    source_type: "paper"
    doi: "10.1234/example"
    state: "discovered"
    review_status: "unreviewed"
    relevance: "medium"
    role: ["frontier"]
    confidence: "metadata_only"
    actionability: "reading_candidate"
"""
            registry = write_registry(
                Path(tmp),
                literature,
                "items: []\n",
                "benchmarks: []\n",
                "risks: []\n",
            )

            errors = validate(registry)

            self.assertTrue(any("duplicate doi" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
