# Generate Structure

**ID:** 6  
**Difficulty:** B

## Descriere

Creați un script care primește de la linia de comandă un path către un director și un fișier JSON. În fișierul JSON se află un dicționar în care se află o structură de directoare și fișiere astfel: fiecare cheie care are ca valoare un dicționar este un director iar dicționarul conținutul, iar fiecare cheie care are ca valoare un string reprezintă un fișier iar string-ul respectiv este conținutul fișierului. Scriptul va crea în folderul dat ca argument directoarele și fișierele conform dicționarului din JSON.

## INPUT

```
generate_structure.py root_folder_path structure_json_file_path
```

**Exemplu de dicționar:**

```json
{
  "dir1": {
    "dir2": { "file1": "continut1", "file2": "continut2" },
    "file3": "continut3"
  },
  "file4": "continut4"
}
```

## OUTPUT

```
root_folder
---dir1
------dir2
---------file1: continut1
---------file2: continut2
------file3: continut3
---file4: continut4
```
