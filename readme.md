# Args converter 🧳  

**Converts arguments for VS Code' `launch.json` configurations like a breeze 🌬 , and copy them to clipboard 📋!**  

Are you using Raycast? See down below for use the converter as a Raycast script!

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

### Raycast script ✨

If you use Raycast, you can use the converter as a script! Just select the cloned directory as the script directory in Raycast's settings, and you're good to go! 


