import numpy as np

from load_data import load_smd


def main():
    cases, endpoints = load_smd()
    rows = endpoints[(endpoints.record_type == "case") & endpoints.pair_reportable].copy()
    rows["n"] = rows.case.str.extract(r"(\d+)").astype(int)

    chains = cases.set_index("case").mutated_chains.to_dict()
    print(f"{'case':<6}{'condition':<11}{'chains':<12}{'YM reduction %':>18}{'UTS reduction %':>18}")
    for n in sorted(rows.n.unique()):
        g = rows[rows.n == n]
        ym = g.ym_reduction_vs_paired_wt_pct.to_numpy(float)
        ut = g.uts_reduction_vs_paired_wt_pct.to_numpy(float)
        cond = g.condition.iloc[0]
        ch = chains.get(n, "all")
        print(f"{n:<6}{cond:<11}{ch:<12}"
              f"{ym.mean():>10.1f} ± {ym.std(ddof=1):<5.1f}"
              f"{ut.mean():>11.1f} ± {ut.std(ddof=1):<5.1f}")
    print()
    print("reduction = 100 x (WT - candidate) / WT, mean ± sample SD over three seed-matched pairs")


if __name__ == "__main__":
    main()
