def generate_suggestions(flags):
    suggestions = []

    if flags[0] > 0.5:
        suggestions.append(
            "Alignment issue detected. Ensure UI elements align to a consistent grid system. "
        )

    if flags[1] > 0.5:
        suggestions.append(
            "Spacing issue detected. Improve padding and margins to reduce visual clutter."
        )

    if not suggestions:
        suggestions.append(
            "UI layout appears well-structured with good alignment and spacing."
        )

    return suggestions
