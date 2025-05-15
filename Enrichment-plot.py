import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the KEGG enrichment results
results_file = "kegg_enrichment_results.csv"
df = pd.read_csv(results_file)

# Step 2: Clean and convert p_value column
df['p_value'] = df['p_value'].astype(str).str.strip()
df['p_value'] = pd.to_numeric(df['p_value'], errors='coerce')
df = df.dropna(subset=['p_value'])

# Step 3: Filter pathways with p_value <= 0.01
fdr_threshold = 0.01
df_filtered = df[df['p_value'] <= fdr_threshold]

# Diagnostic output
print(f"Total pathways in input file: {len(df)}")
print(f"Pathways with p_value <= {fdr_threshold}: {len(df_filtered)}")

# Step 4: Plot if results exist
if df_filtered.empty:
    print(f"No pathways found with p_value <= {fdr_threshold}.")
else:
    df_sorted = df_filtered.sort_values(by='p_value')
    num_pathways = len(df_sorted)
    fig_height = max(5, num_pathways * 0.5)
    plt.figure(figsize=(10, fig_height))

    bars = plt.barh(df_sorted['name'], -np.log10(df_sorted['p_value']), color='steelblue')

    plt.xlabel('-log10(FDR-adjusted p-value)', fontsize=12)
    plt.title(f'KEGG Pathway Enrichment (FDR ≤ {fdr_threshold})', fontsize=14)
    plt.gca().invert_yaxis()
    plt.grid(axis='x', linestyle='--', alpha=0.6)

    for bar, pval in zip(bars, df_sorted['p_value']):
        plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                 f"{pval:.1e}", va='center', fontsize=9)

    plt.tight_layout()
    plt.savefig("kegg_pathways_plot.jpeg", dpi=300, bbox_inches='tight')
    plt.show()
