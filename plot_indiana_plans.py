"""
Scatter plot of premium vs. deductible for Indiana Marketplace plans.

Usage:
    python plot_indiana_plans.py individual_market_medical.zip
"""
import sys
import zipfile

import matplotlib.pyplot as plt
import pandas as pd

# --- Configuration ---------------------------------------------------------
ZIP_PATH = sys.argv[1] if len(sys.argv) > 1 else "individual_market_medical.zip"
STATE = "IN"
PREMIUM_COL = "Premium Adult Individual Age 40"
DEDUCTIBLE_COL = "Medical Deductible - Individual - Standard"
OUTPUT_PNG = "indiana_premium_vs_deductible.png"


def to_number(series: pd.Series) -> pd.Series:
    """Convert strings like '$1,500' to numbers; non-numeric text becomes NaN."""
    return pd.to_numeric(series.str.replace(r"[$,]", "", regex=True), errors="coerce")


def main() -> None:
    # Read the first sheet of the xlsx inside the zip.
    # The real column names are on the second row (header=1).
    with zipfile.ZipFile(ZIP_PATH) as zf:
        xlsx_name = next(n for n in zf.namelist() if n.endswith(".xlsx"))
        with zf.open(xlsx_name) as f:
            df = pd.read_excel(f, sheet_name=0, header=1, dtype=str)

    df.columns = [c.strip() for c in df.columns]

    # Keep only Indiana rows
    ind = df[df["State Code"] == STATE].copy()
    print(f"Plans left after filtering to {STATE}: {len(ind)}")
    print(f"Unique plan IDs: {ind['Plan ID (Standard Component)'].nunique()}")

    # Clean the numeric columns
    ind["premium"] = to_number(ind[PREMIUM_COL])
    ind["deductible"] = to_number(ind[DEDUCTIBLE_COL])
    plot_df = ind.dropna(subset=["premium", "deductible"])

    # Scatter plot
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.scatter(plot_df["premium"], plot_df["deductible"], alpha=0.35, s=18)
    ax.set_xlabel("Monthly premium, adult age 40 ($)")
    ax.set_ylabel("Individual medical deductible ($)")
    ax.set_title("Indiana Marketplace Plans: Premium vs. Deductible")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUTPUT_PNG, dpi=150)
    print(f"Saved {OUTPUT_PNG}")


if __name__ == "__main__":
    main()
