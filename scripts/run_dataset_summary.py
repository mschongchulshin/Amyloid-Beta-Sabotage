import numpy as np

from load_data import COND, load_540


def main():
    df = load_540()
    print(f"records            {len(df)}")
    print(f"unique sequences   {df.sequence.nunique()}")
    print(f"loading conditions {df.condition.nunique()}")
    print()

    depth = df.drop_duplicates("sequence").depth.value_counts().sort_index()
    print("substitutions per sequence")
    for k, v in depth.items():
        print(f"  {k}  {v:>4}")
    print()

    for col, name in (("Young's modulus (Mpa)", "YM (MPa)"), ("UTS (Mpa)", "UTS (MPa)")):
        print(name)
        for c in COND:
            v = df[df.condition == c][col].to_numpy(float)
            print(f"  {c:9s} median {np.median(v):9.1f}   range {v.min():8.1f} - {v.max():8.1f}")
        print()


if __name__ == "__main__":
    main()
