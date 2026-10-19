# Indiana Marketplace Plans: Premium vs. Deductible

Filters Marketplace individual-market medical plans to Indiana (`State Code = IN`),
prints how many plan rows remain, and saves a scatter plot of premium (x) vs.
deductible (y) as a PNG.

- **Premium:** `Premium Adult Individual Age 40` (monthly)
- **Deductible:** `Medical Deductible - Individual - Standard`

Note: each row is one plan in one county, so the row count is larger than the
number of distinct plans. The script prints both.

## Usage

```bash
pip install -r requirements.txt
python plot_indiana_plans.py individual_market_medical.zip
```

The data file is not included in this repo (about 58 MB). Download it separately
and place it next to the script, or pass its path as the argument.

Output: `indiana_premium_vs_deductible.png`
