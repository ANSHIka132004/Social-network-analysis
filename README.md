# Boyer–Moore Majority Vote Algorithm — Social Network Analysis & Big Data Assignment

This repository contains two separate implementations of the **Boyer–Moore Majority Vote Algorithm**, created for academic assignments:

- **Social Network Analysis (SNA)** — Majority detection in a small community  
- **Big Data Analysis** — Generating a large synthetic dataset and applying Boyer–Moore on thousands of samples  

Both tasks demonstrate how majority voting can be used to identify the dominant community in a network.

---

## 📌 Assignment 1 — Social Network Analysis (SNA)

### **Topic:** Identifying the Majority Community in a Small Social Network  
This assignment uses a small predefined list of community labels to understand how Boyer–Moore selects the majority.

### **Dataset Used**
```python
["A", "A", "B", "A", "A", "C", "A", "B", "A", "A"]
Goal

Determine which community appears more than 50% of the time.

Steps

Create a small list of community labels

Apply Boyer–Moore algorithm:

Select a candidate

Maintain running count

Replace candidate when count becomes zero

Verify whether the candidate actually appears more than n/2 times

Print the final majority community

# 📌 Assignment 2 — Big Data Analysis

### **Topic:** Detecting the Majority Community in a Large Synthetic Dataset Using Boyer–Moore

### **Goal**
Generate a large-scale dataset of **1000+ users** using probability-based community distribution and apply the Boyer–Moore Majority Vote Algorithm to determine the dominant community.

### **Dataset Probability Distribution**
| Community | Probability |
|----------|-------------|
| A        | 55%         |
| B        | 25%         |
| C        | 15%         |
| D        | 5%          |

### **Steps**
- Choose the number of users (e.g., 1000, 2000, 5000).  
- Assign each user a community label using the given probability distribution.  
- Store the data in a pandas DataFrame with fields:
  - `user_id`
  - `community`
- Save the dataset as:
  ```bash
  my_social_network.csv
