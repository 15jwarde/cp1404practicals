# Part a
print("Electricity bill estimator")
cents_per_KWh = int(input("Enter cents per KWh: "))
daily_use = float(input("Enter daily use in KWh: "))
billing_period = int(input("Enter number of billing days: "))
bill_total = (cents_per_KWh / 100) * daily_use * billing_period
print(f"Estimated bill: ${bill_total:.2f}")

# Part b
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("\nElectricity bill estimator 2.0")
tariff = input("Which tariff? 11 or 31: ")
if tariff == "11":
    tariff_rate = TARIFF_11
else:
    tariff_rate = TARIFF_31
daily_use = float(input("Enter daily use in KWh: "))
billing_period = int(input("Enter number of billing days: "))
bill_total = tariff_rate * daily_use * billing_period
print(f"Estimated bill: ${bill_total:.2f}")
