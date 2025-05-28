
# QuickTXT

This tool makes TextEdit a lot mroe like Windows Notepad because TextEdit really just sucks.


## How it Works

1. Creates a `.txt` file in the dedicated MacOS temporary directory.
2. Opens it in TextEdit automatically.
3. Upon saving, prompts the user for a directory to save the file.
4. Deletes the temporary file and copies it to the chosen directory.
5. Reopens the file that has been moved for further editing.

## Building the App Yourself

Unfortunately, the prebuilt `.app` is unsigned (I have no money, Apple has a trillion dollars but wants more), so macOS will block it. But good news: you can build your own version realy quickly.

1. Install everything in `requirements.txt`.
2. Pop open terminal and go to where the script and icon is.
3. Use this super cool bash copypasta (with your own environment obviously):
```bash
path/to/.env/python -m PyInstaller \
  --windowed \
  --name "QuickTXT" \
  --icon=icon.icns \
  --onefile \
  main.py
```
