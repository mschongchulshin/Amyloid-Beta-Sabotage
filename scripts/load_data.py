from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data"

WT = "DAEFRHDSGYEVHHQKLVFFAEDVGSNKGAIIGLMVGGVVIA"
POS = [16, 17, 18, 19, 20, 21]
COND = ["16LYS/X", "16LYS/Y", "23ASP/X", "23ASP/Y"]

COND_OF = {("16", "X"): "16LYS/X", ("16", "Y"): "16LYS/Y",
           ("23", "X"): "23ASP/X", ("23", "Y"): "23ASP/Y"}


def genome(sequence):
    return "".join(sequence[p - 1] for p in POS)


def substitutions(sequence):
    return [f"{WT[p - 1]}{p}{sequence[p - 1]}"
            for p in POS if sequence[p - 1] != WT[p - 1]]


def load_540():
    df = pd.read_csv(DATA / "dataset_540.csv")
    df.columns = [c.strip() for c in df.columns]
    dummy = df["dummy atom"].astype(str).str.extract(r"(\d+)")[0]
    axis = df["pulling axis"].astype(str).str.strip().str.upper()
    df["condition"] = [COND_OF[(d, a)] for d, a in zip(dummy, axis)]
    df["cond_idx"] = df.condition.map({c: i for i, c in enumerate(COND)})
    df["depth"] = df.sequence.map(lambda s: len(substitutions(s)))
    return df


def load_candidates():
    return pd.read_csv(DATA / "candidate_scores.csv")


def load_single_substitutions():
    return pd.read_csv(DATA / "single_substitutions.csv")


def load_smd():
    cases = pd.read_csv(DATA / "smd_cases.csv")
    endpoints = pd.read_csv(DATA / "smd_endpoints.csv")
    return cases, endpoints


if __name__ == "__main__":
    d = load_540()
    print(f"{len(d)} records, {d.sequence.nunique()} unique sequences")
    print(d.groupby("condition")[["Young's modulus (Mpa)", "UTS (Mpa)"]].median().round(1))
