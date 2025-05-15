# BioEnrichPy

**BioEnrichPy** is a lightweight Python tool for automated functional enrichment analysis of human genes or proteins interacting with SARS-CoV-2 or other viral agents. It leverages the g:Profiler API to identify enriched **KEGG pathways**, **Gene Ontology (GO) biological processes**, **molecular functions**, and **cellular components**. The pipeline reads input from an Excel file and exports high-confidence pathway results in a reproducible, publication-ready format.

---

## 🔍 Features

- Simple and customizable enrichment pipeline
- Supports input from Excel (`.xlsx`) files
- Queries the g:Profiler API for:
  - KEGG pathways
  - Gene Ontology: Biological Process (BP), Molecular Function (MF), Cellular Component (CC)
- Automatically saves filtered enrichment results to a CSV file
- Built using `pandas`, `gprofiler-official`, and `openpyxl`

---

## 📁 Input Format

- Input file: Excel (`.xlsx`)
- The file must contain one column with gene symbols (e.g., HGNC names like `TP53`, `EGFR`, etc.)
- Update the script with your file name and column name:

```python
excel_file = "your_input_file.xlsx"         # Replace with your Excel file name
gene_list = df['GeneSymbol'].tolist()       # Replace 'GeneSymbol' with your actual column name
```

---

## 💻 Installation

Install the required Python packages using:

```bash
pip install gprofiler-official pandas openpyxl
```

---

## 🚀 Usage

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/BioEnrichPy.git
cd BioEnrichPy
```

2. **Edit the Script**

Open the Python file (`bioenrichpy.py`) and:
- Update the `excel_file` variable with your Excel filename.
- Update the column name to match the one containing your gene list.

3. **Run the Script**

```bash
python bioenrichpy.py
```

4. **Output**

- Top KEGG enrichment results will be printed in the terminal.
- Results will be saved to:

```text
kegg_enrichment_results.csv
```

You can modify the script to save GO-BP, GO-MF, or GO-CC results by changing the `'source'` filter to `'GO:BP'`, `'GO:MF'`, or `'GO:CC'`.

---

## 📊 Example Output

```
Top KEGG Pathway Enrichments:

                        name       p_value  intersection_size  query_size  term_size
0          Apoptosis pathway    0.000122                8           100         90
1  NF-kappa B signaling path    0.000435                6           100         80

✅ KEGG results saved to 'kegg_enrichment_results.csv'
```

---

## 📦 File Structure

```
BioEnrichPy/
├── bioenrichpy.py                # Main script
├── your_input_file.xlsx          # Input file (user-provided)
├── kegg_enrichment_results.csv   # Output file (auto-generated)
├── README.md                     # Documentation
```

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute it with attribution.

---

## 👩‍💻 Author

**Sreelakshmi K.**  
PhD Scholar, Yenepoya (Deemed to be University)  
Email: sreelakshmi@example.com *(replace with your real contact)*

---

## 📚 Citation

If you use this tool in your research, please cite:

> Sreelakshmi K., *BioEnrichPy: An Automated Python-Based Functional Enrichment Tool for Viral Interactome Analysis*, [GitHub Repository], 2025.

---

