# Python Template

- setuptools
- pyproject.toml
- setup.cfg
- CLI

## Quick set up

0. `pip install -e .` in the directory of `setup.cfg` and `pyproject.toml`.
1. `python -m build`
2. `python -m twine upload --repository testpypi dist/*`
3. `python -m pip install --index-url https://test.pypi.org/simple/ --no-deps cli`

## References

- https://packaging.python.org/en/latest/tutorials/packaging-projects/
