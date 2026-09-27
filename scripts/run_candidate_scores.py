import numpy as np

from load_data import COND, load_candidates, load_single_substitutions


def main():
    cand = load_candidates()
    print(f"evaluated candidates {len(cand):,}")
    print()

    for endpoint in ("YM", "UTS"):
        print(f"{endpoint} rank score")
        for c in COND:
            v = cand[f"{endpoint}_{c}"].to_numpy(float)
            print(f"  {c:9s} median {np.median(v):.3f}   min {v.min():.3f}   max {v.max():.3f}")
        print()

    print("joint rank score, condition-specific objective")
    for c in COND:
        v = cand[f"obj_{c}"].to_numpy(float)
        print(f"  {c:9s} median {np.median(v):.3f}   min {v.min():.3f}")
    v = cand["obj_shared"].to_numpy(float)
    print(f"  {'shared':9s} median {np.median(v):.3f}   min {v.min():.3f}")
    print()

    single = load_single_substitutions()
    print(f"single substitutions {len(single)}")
    for c in COND:
        v = single[f"obj_{c}"].to_numpy(float)
        print(f"  {c:9s} median {np.median(v):.3f}   min {v.min():.3f}")


if __name__ == "__main__":
    main()
