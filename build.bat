rm -r build dist
python setup.py sdist bdist_wheel
pip uninstall smaliemu
python setup.py install