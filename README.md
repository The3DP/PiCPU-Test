# 🧪 Test Easily: Raspberry Pi CPU Testing Suite

Test your Raspberry Pi’s CPU straight from the terminal — quickly, simply, and effectively.

![100% Complete](https://img.shields.io/badge/Progress-100%25-darkgreen)

---

This lightweight suite lets you run various CPU performance and stability tests without the need for extra tools or complex setup.

## 🚀 Features

- ✅ Easy to use — just run from terminal  
- ⚡ Fast testing options for quick diagnostics  
- 🔧 Includes a powerful stress test (optional)  
- 🧊 Ideal for testing cooling and thermal throttling  
- 📦 No additional packages required  

---

## 🧪 Available Tests

This repository includes **4 basic test scripts** and **1 advanced stress test**:

| File           | Description                          |
|----------------|--------------------------------------|
| `Test-A.sh`    | Basic CPU load simulation            |
| `Test-B.sh`    | Arithmetic operation stress          |
| `Test-C.sh`    | Multi-core performance check         |
| `Test-D.sh`    | Logic and branch testing             |
| `Nitro-Test.sh`| 🔥 Advanced stress test (customizable) |

---

## ⚠️ Nitro-Test (Advanced)

**Warning:** This script pushes your Raspberry Pi to its limits.  
It is only recommended if your device has **adequate power supply and cooling**.

### 🛠️ Change the Test Duration

You can modify the stress duration by editing the `duration` variable inside the script:

```bash
# Inside Nitro-Test.sh
duration=30  # Default is 30 seconds
