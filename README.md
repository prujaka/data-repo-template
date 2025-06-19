# Repo template
This is a basic template for a data project.

## Getting started
Create the virtual environment from your preferred Python version using `pyenv virtualenv`:
```zsh
pyenv virtualenv 3.12.7 foo-env
```

Activate the new environment locally:
```zsh
pyenv local foo-env
```
Then, change the Python interpreter in Pycharm for the foo-env.

Rename `package` to your package name: the directory itself and in the `setup.py` file. The best would be to refactor the `package` name in Pycharm by clicking on it with the right muse button and selecting "Rename". 

Install `setuptools`:
```zsh
pip install setuptools
```

Populate the requirements.txt and install the package:
```zsh
pip install -e . 
```

Create the config from `config.ini.template` and save it as `config.ini`:
```zsh
cp config.ini.template config.ini
```
Then, populate it with the secrets.
