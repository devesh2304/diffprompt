import difflib

def compute_diff(output_a: str, output_b: str) -> str:
    """Return a human-readable line-by-line diff of two LLM outputs."""
    lines_a = output_a.splitlines(keepends=True)
    lines_b = output_b.splitlines(keepends=True)

    diff = difflib.unified_diff(
        lines_a,
        lines_b,
        fromfile="Prompt A output",
        tofile="Prompt B output",
        lineterm=""
    )
    return "\n".join(diff)

def compute_similarity(output_a: str, output_b: str) -> float:
    """Return a similarity ratio between 0.0 and 1.0."""
    return difflib.SequenceMatcher(None, output_a, output_b).ratio()