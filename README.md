# GvahimServer

## How to run it (on Linux)
1. Install [Poetry](https://python-poetry.org/):
```sh
curl -sSL https://install.python-poetry.org | python -
```
2. Install [ashf](https://github.com/AmitDIRTYC0W/ashf), my HTTP framework:
	1. Download the source code
	```sh
	git clone https://github.com/AmitDIRTYC0W/ashf.git
	```
	2. Build
	```sh
	cd ashf
	poetry build
	```
	3. Install
	```sh
	cd dist
	pip install ashf-*.whl
	```
3. Download this server's sources:
```sh
git clone https://github.com/AmitDIRTYC0W/GvahimServer.git
```
4. Cross your fingers and... run it!
```sh
cd GvahimServer
python app.py
```
