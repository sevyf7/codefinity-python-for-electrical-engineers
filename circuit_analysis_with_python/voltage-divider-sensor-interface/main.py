def find_closest_e12(value):
    e12_series = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
    multipliers = [1, 10, 100, 1000, 10000, 100000, 1000000]
    candidates = []
    for base in e12_series:
        for m in multipliers:
            candidates.append(base * m)
    # pick the candidate closest to the target value
    return min(candidates, key=lambda x: abs(x - value))

def design_voltage_divider(vin, vout, preferred_r2=10000):
    # ideal R1 so that Vout = vin * (R2 / (R1 + R2))
    r2_ideal = preferred_r2
    r1_ideal = r2_ideal * (vin - vout) / vout

    # snap each to nearest E12
    r1_std = find_closest_e12(r1_ideal)
    r2_std = find_closest_e12(r2_ideal)

    # compute actual output
    vout_actual = vin * (r2_std / (r1_std + r2_std))
    return r1_std, r2_std, vout_actual

if __name__ == "__main__":
    vin = 5.0
    vout = 3.3
    r1, r2, vout_calc = design_voltage_divider(vin, vout)
    result_str = f"Closest standard resistor values: R1 = {r1} Ω, R2 = {r2} Ω. Output voltage: {vout_calc:.2f} V"
    print(result_str)
