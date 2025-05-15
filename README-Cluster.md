
# SARS-CoV-2 Viral-Host Interaction Cluster Analysis

This script performs **cluster detection and visualization** of SARS-CoV-2-human protein interaction networks using the **Louvain community detection algorithm**.

## 🧠 Purpose

- Identify tightly connected modules (clusters) from a viral-host interaction network.
- Visualize the **largest (top) cluster** in the network, distinguishing between viral and human proteins.

## 📂 Input

A Microsoft Excel file containing two columns (without headers):
- Column 1: Viral protein identifiers
- Column 2: Human protein identifiers

Format:
```
Viral_Protein   Human_Protein
--------------- --------------
NSP1            P12345
NSP3            Q9H1A4
...
```

## ⚙️ How It Works

1. Reads the Excel file and standardizes column names.
2. Constructs an undirected graph using NetworkX.
3. Applies **Louvain community detection** to find clusters.
4. Extracts the **largest cluster**.
5. Visualizes the cluster with:
   - Red nodes for viral proteins.
   - Skyblue nodes for human proteins.
   - Node labels and improved layout.

## 🖼️ Output

- `top_cluster.png`: High-resolution image of the top cluster (saved at 600 DPI).

## 🧪 Requirements

Install the following Python packages:

```bash
pip install pandas networkx matplotlib python-louvain openpyxl
```

## 🚀 Usage

1. Replace the file path in the script:

```python
file_path = "your_input_file.xlsx"
```

2. Run the script:

```bash
python cluster_analysis.py
```

## 📜 Citation

If you use this script in your research, please cite this GitHub repository or the associated paper (if available).

---

**Author**: [Sreelakshmi K.](https://github.com/Sreelakshmi312)  
**Project**: Part of SARS-CoV-2 BioEnrichPy Repository
