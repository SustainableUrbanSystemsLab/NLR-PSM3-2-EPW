year = ""
year_str = str(year).strip()
year_is_valid = True
year_warning = ""

if not year_str:
    year_is_valid = False
    year_warning = "A year or TMY identifier is required."
elif year_str.isdigit():
    pass
else:
    if not year_str.lower().startswith(("tmy", "tgy", "tdy")):
        year_is_valid = False
        year_warning = "Year must be a numeric year (>=1998) or a TMY name like tmy or tmy-2024."

print(f"year_is_valid: {year_is_valid}, year_warning: {year_warning}")
