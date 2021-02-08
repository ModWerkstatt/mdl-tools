# mdl-tools

Tool set for Transport Fever 2 mdl files

Requires Python3 to run

## recount_mesh.py

Recounts the mesh numbers and puts them in the line.

It also can replace "lod$" with the current lod number.

Requirements: _meshID = "X" must be put in the mesh and X must be any integer

Usage:
```python
python3 recount_mesh.py filename.mdl
```

## change_doorside.py

Replaces doors_left with doors_right and vice versa

Requirements: animation entries must be complete 

Usage:
```python
python3 change_doorside.py filename.mdl
```
