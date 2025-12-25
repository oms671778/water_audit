PH_MIN = 6.5
PH_MAX = 8.5
CHLORIDE_MAX = 250.06
RESULTS_FILE = "water_results.txt"

def banner():
    print("\n==== Water Quality Checker ====\n")

def get_number(prompt):
    while True:
        val = input(prompt).strip()
        try:
            return float(val)
        except:
            print("Please enter a valid number.")

def check_water(ph, chloride):
    problems = []
    if ph < PH_MIN or ph > PH_MAX:
        problems.append("pH out of range")
    if chloride > CHLORIDE_MAX:
        problems.append("Chloride too high")
    return (len(problems) == 0), problems

def save_result(ph, chloride, safe, problems):
    try:
        with open(RESULTS_FILE, "a") as f:
            status = "SAFE" if safe else "NOT SAFE"
            f.write(f"pH={ph}, Cl={chloride} mg/L, {status}")
            if problems:
                f.write(", issues: " + "; ".join(problems))
            f.write("\n")
        print("Result saved to", RESULTS_FILE)
    except:
        print("Could not save result.")

def main():
    banner()
    while True:
        ph = get_number("Enter pH value: ")
        chloride = get_number("Enter Chloride (mg/L): ")
        safe, problems = check_water(ph, chloride)
        print()
        if safe:
            print("Result: Water is SAFE for drinking.")
        else:
            print("Result: Water is NOT SAFE for drinking.")
            print("Issues:")
            for p in problems:
                print(" -", p)
        if input("Save result? (y/N): ").strip().lower() == 'y':
            save_result(ph, chloride, safe, problems)
        if input("Check another sample? (Y/n): ").strip().lower() == 'n':
            break
        print()

if __name__ == "__main__":
    main()

