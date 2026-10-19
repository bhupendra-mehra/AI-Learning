def clean_text(value: str) -> str:
    """Remove leading and trailing whitespace and normalize internal spaces."""
    return " ".join(value.split())


def slugify(value: str) -> str:
    """Convert a string into a simple lowercase hyphen-separated slug."""
    return "-".join(value.lower().split())