import pandas as pd

def calculate_average_income_by_education(df):
    """
    Kontrollib 'haridustase' ja 'sissetulek' veergude olemasolu DataFrame'is
    ja arvutab seejärel keskmise sissetuleku haridustasemeti.
    """
    # --- SINU LISATUD ASSERT LAUSED ---
    # 1. Kontrolli 'haridustase' veeru olemasolu
    # assert ...

    # 2. Kontrolli 'sissetulek' veeru olemasolu
    # assert ...
    # ------------------------------------

    # Kui assertid läksid läbi:
    print("Vajalikud veerud ('haridustase', 'sissetulek') leitud.") # See print on testimiseks vähem oluline

    # Arvutame keskmise sissetuleku haridustasemeti
    # Hea tava oleks ka kontrollida, et sissetulek on numbriline, aga hoiame praegu lihtsana
    avg_income = df.groupby('haridustase')['sissetulek'].mean()

    # Tagastame tulemuse
    return avg_income
