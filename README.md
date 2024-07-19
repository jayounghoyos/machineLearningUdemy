# Commands to work
```bash
conda activate base
conda install jupyter
jupyter notebook
```
## Command for Reading CSV with Specific Encoding
If you encounter encoding errors when reading a CSV file, you can specify the correct `encoding` using the encoding parameter. Below is an example of how to read a CSV file using the `ISO-8859-1` encoding:

```python
import pandas as pd

# Leer el archivo CSV con la codificación ISO-8859-1
df = pd.read_csv("csv/vg.csv", encoding='ISO-8859-1')
```

