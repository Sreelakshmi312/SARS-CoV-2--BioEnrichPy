from gprofiler import GProfiler
import pandas as pd

# === Step 1: Load gene names from Excel ===
# Make sure the Excel file exists at this location and the column name is correct
excel_file = "file_name"  # Adjust path if needed
df = pd.read_excel(excel_file)

# Replace 'column-name' with the actual column name that contains gene names in your Excel
gene_list = df['column-name'].dropna().astype(str).tolist()

# === Step 2: Run KEGG pathway enrichment using g: Profiler ===
gp = GProfiler(return_dataframe=True)
results = gp.profile(organism='hsapiens', query=gene_list)

# === Step 3: Filter only KEGG pathways ===
kegg_results = results[results['source'] == 'KEGG']

# === Step 4: Display & save results ===
if not kegg_results.empty:
    print("\nTop KEGG Pathway Enrichments:\n")
    print(kegg_results[['name', 'p_value', 'intersection_size', 'query_size', 'term_size']].head(10))
    kegg_results.to_csv("kegg_enrichment_results.csv", index=False)
    print("\n✅ KEGG results saved to 'kegg_enrichment_results.csv'")
else:
    print("⚠️ No KEGG enrichment terms found.")

# === Optional: Show available columns if debugging ===
# print("\nAvailable columns in result:\n", results.columns)
