FILE=main.py

run:
	python3 $(FILE)

all:
    pyinstaller -F $(FILE)

clean:
	rm -rf build
	rm -rf dist
	rm main.spec
	rm -rf __pycache__
