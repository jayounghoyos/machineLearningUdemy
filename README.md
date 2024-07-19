# Commands to work
```bash
conda activate base
conda install jupyter
jupyter notebook
```
## Command for Reading CSV with Specific Encoding

Si encuentras errores de codificación al leer un archivo CSV, puedes especificar la codificación correcta utilizando el parámetro `encoding`. A continuación se muestra un ejemplo de cómo leer un archivo CSV utilizando la codificación `ISO-8859-1`:

```python
import pandas as pd

# Leer el archivo CSV con la codificación ISO-8859-1
df = pd.read_csv("csv/vg.csv", encoding='ISO-8859-1')
```

