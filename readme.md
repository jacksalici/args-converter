# Args converter 🧳  

**Converts arguments for VS Code' `launch.json` configurations like a breeze 🌬 , and copy them to clipboard 📋!**  

## 📦 Installation

```bash
pip install -r requirements.txt
chmod +x converter.py
```



## 🚀 Usage

```bash
converter.py python3 test.py --this "/is" --a test
```

Output on `stdout` and _clipboard_:

```json
[
    "--this",
    "/is",
    "--a",
    "test"
]
```


