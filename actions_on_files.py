from pathlib import Path

def return_budget_amount(path):
    try:
        with open(path, "r") as f:
            str_amount = f.read()
            return float(str_amount)
    except Exception as e:
        print(f"error! type error:{e}")
