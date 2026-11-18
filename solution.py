

def solve(value):
    return [value["items"][i:i+value["size"]] for i in range(0, len(value["items"]), value["size"])] if value["size"] > 0 else (_ for _ in ()).throw(ValueError("size must be positive"))
