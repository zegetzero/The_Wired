# The_Wired: Input Monitoring Research Tool

**The_Wired** is a Python-based utility developed for **defensive security research**. This tool demonstrates how system-level input capture (keylogging) operates, providing a practical environment for studying digital footprints, forensic artifacts, and detection strategies in **Incident Response (IR)** and **Digital Forensics**.

---

## 🛡️ Project Intent & Educational 
The primary goal of this repository is to analyze the mechanics of unauthorized monitoring to better defend against them. 

* **Behavioral Analysis:** Understanding how Python interfaces with OS-level input hooks.
* **Forensic Artifacts:** Identifying the logs, process behaviors, and system changes created during active monitoring.
* **Detection Engineering:** Developing and testing YARA rules or EDR queries to catch similar "stealth" scripts in a production environment.

---

## 🚀 Technical Features
* **Low-Level Hooking:** Utilizes `pynput` to intercept scan codes directly from the OS input stream.
* **Structured Logging:** Outputs captured data into a machine-readable JSON format, simulating real-world security logs for easier parsing and correlation.
* **Stealth Simulation:** Designed to test how background execution and obfuscation affect detection rates by standard AV/EDR solutions.
* **Cleanup Protocol:** Includes functions to securely remove research artifacts (logs) after a testing session.

---

## 🛠️ Installation & Usage
> **Warning:** This tool is for authorized educational environments only. Ensure you have explicit permission before running this on any machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/OliverCarrillo/The_Wired.git](https://github.com/OliverCarrillo/The_Wired.git)
cd The_Wired
```
---
## 📜 Ethical Disclaimer

* IMPORTANT: This project is for Educational and Authorized Research Purposes Only. The author, zegetzero, does not condone or support the use of this software for malicious activities. Unauthorized access to computer systems is a violation of law and professional ethics. Use of this tool without explicit, written permission from the system owner is strictly prohibited.
