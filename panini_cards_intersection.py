
def cards_intersection(missing: str, third_party_repeated: str, separator:str = ", ") -> list[str]:
    repeated_dict = assemble_repeated_dict(third_party_repeated.strip().split(separator))

    missing_in_third_party_repeated = [
        m
        for m in missing.strip().split(separator)
        if repeated_dict.get(m.replace(" ", "")) is not None
    ]

    return missing_in_third_party_repeated


def assemble_repeated_dict(repeated_list: list[str]) -> dict:
    return { r.replace(" ", "") : True for r in repeated_list if r.strip() != ""}
