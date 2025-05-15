
# KEGG Pathway Enrichment using g:Profiler

This script performs KEGG pathway enrichment analysis on a list of human gene names using the g:Profiler Python API. It reads gene names from an Excel file, queries g:Profiler, filters for KEGG terms, and saves the results to a CSV file.

## 📦 Requirements

- Python 3.x
- pandas
- gprofiler-official

Install the required packages using:

```bash
pip install pandas gprofiler-official
```

## 📂 Input

An Excel file containing a list of gene names.

- Replace `"file_name"` with the actual path to your Excel file.
- Replace `'column-name'` with the actual column name in your Excel file that contains gene names.

## ▶️ How to Run

Run the script using Python:

```bash
python kegg_enrichment.py
```

## 💾 Output

- `kegg_enrichment_results.csv`: Contains the enriched KEGG pathways including p-values and gene counts.

## 📊 Output Columns

- `name`: Name of the KEGG pathway
- `p_value`: Raw p-value
- `intersection_size`: Number of query genes in the term
- `query_size`: Total number of input genes
- `term_size`: Total number of genes in the KEGG term

## ⚠️ Notes

- The script filters results to show only KEGG-related enrichments (`source == 'KEGG'`).
- Ensure the input Excel file is properly formatted.

## 📁 Example File Structure

```
your-folder/
├── kegg_enrichment.py
├── your_input_file.xlsx
├── kegg_enrichment_results.csv
└── README.md
```
