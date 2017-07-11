python setup.py sdist bdist_wheel
pip uninstall smaliemu
python setup.py install
rm -r build dist smaliemu.egg-info
