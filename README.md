# 🗺️ Geo-Data Logic: Indian States & UTs Game

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Library](https://img.shields.io/badge/Data_Handling-Pandas-150458?style=for-the-badge&logo=pandas)
![GUI](https://img.shields.io/badge/Graphics-Turtle-green?style=for-the-badge)

> **A technical implementation of coordinate-based data visualization using Python and Pandas.**

---

## 🔄 System Architecture
The core objective of Day 25 was to transition from hard-coded logic to a **Data-Driven Architecture**.Instead of defining positions within the source code, the application serves as a rendering engine for an external CSV dataset.

### 🛠️ Key Technical Features
* **Localized Data Engine**: Refactored the standard curriculum to handle 36 unique Indian administrative divisions (States and UTs) for real-world data localization.
* **Dynamic Coordinate Mapping**: Utilizes `pandas` to query and retrieve discrete $(x, y)$ coordinate pairs from a CSV file based on real-time user input.
* **State Persistence & Reporting**: Implements an automated 'Exit' trigger using **List Comprehension** to generate a `missed_administrative_div.csv` for post-session review.
* **Performance Optimization**: Managed the game loop to handle input normalization and dataset verification without degrading UI responsiveness.

---


## 🚀 Deployment
1. Ensure `map.gif` and the state data CSV are in the root directory.
2. Execute `main.py`.
3. Enter the names of Indian States and UTs. Type **'Exit'** to terminate the loop and generate the missed states report.
