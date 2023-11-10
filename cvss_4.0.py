def calculate_cvss_base_score(impact, exploitability):
    # Base Impact Subscore
    if impact == 'N':
        impact_subscore = 0
    elif impact == 'L':
        impact_subscore = 0.22
    elif impact == 'L':
        impact_subscore = 0.56
    else:
        impact_subscore = 0.704

    # Base Exploitability Subscore
    if exploitability == 0:
        exploitability_subscore = 0
    else:
        exploitability_subscore = 8.22 * exploitability

    # Calculate Base Score
    base_score = round(min(impact_subscore + exploitability_subscore, 10), 1)

    return base_score

def main():
    # Example values for impact and exploitability
    impact = 'H'  # High (H), Low (L), or None (N)
    exploitability = 0.22  # Range: 0.0 to 1.0

    # Calculate CVSS Base Score
    base_score = calculate_cvss_base_score(impact, exploitability)

    print(f"CVSS Base Score: {base_score}")

if __name__ == "__main__":
    main()
