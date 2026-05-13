def analyze_circuit(R1, R2, R3, V):
    # In series
    Rs = R1 + R2
    # In parallel with R3
    Rp = 1/(1/Rs + 1/R3)
    total_resistance = Rp
    print("Total resistance (Ohms):", total_resistance)

    total_current = V / total_resistance
    print("Total current (A):", total_current)

    # Current through series branch (R1 + R2)
    current_series = V / Rs
    current_R1 = current_series
    current_R2 = current_series
    print("Current through R1 (A):", current_R1)
    print("Current through R2 (A):", current_R2)

    # Current through R3 branch
    current_R3 = V / R3
    print("Current through R3 (A):", current_R3)


# Sample values
R1 = 100
R2 = 200
R3 = 300
V = 12

analyze_circuit(R1, R2, R3, V)