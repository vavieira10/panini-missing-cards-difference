import sys
from json import load
from panini_cards_intersection import cards_intersection

def validate_dict(input_dict: dict):
    if input_dict.get("missing") is None:
        raise Exception("Invalid input. missing attribute is missing in input json.")
    
    if input_dict.get("repeated") is None:
        raise Exception("Invalid input. repeated attribute is missing in input json.")


def parse_json_file(file_name:str) -> dict:
    with open(file_name, "r") as fp:
        return load(fp)


def main():
    if len(sys.argv) != 2:
        raise Exception(f"Invalid input. One argument must be passed.")
    
    input_file_name = sys.argv[1]

    input_dict = parse_json_file(input_file_name)
    validate_dict(input_dict)

    print(
        cards_intersection(
            input_dict["missing"],
            input_dict["repeated"]),
            input_dict.get("separator", ", ")
    )

if __name__ == "__main__":
    main()