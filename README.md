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

Assignment 2 — Big Data Analysis
Topic

Performing majority detection on a large synthetic dataset using the Boyer–Moore Algorithm.

Goal

Generate a dataset of 1000+ users and determine the majority community using an efficient linear-time algorithm.

Dataset Generation

A synthetic dataset is built using the following probability distribution:

Community	Probability
A	55%
B	25%
C	15%
D	5%

This ensures that A is expected to be the majority.

Steps

Select number of users (1000, 2000, 5000, etc.)

Assign communities using probability-based sampling

Convert to a pandas DataFrame

Save the dataset as:

my_social_network.csv


Load the CSV

Apply the Boyer–Moore algorithm on the entire dataset

Print the detected majority

Expected Output
Majority Community: A


## Assignment 2 — Big Data Analysis
Topic

Performing majority detection on a large synthetic dataset using the Boyer–Moore Algorithm.

Goal

Generate a dataset of 1000+ users and determine the majority community using an efficient linear-time algorithm.

Dataset Generation

A synthetic dataset is built using the following probability distribution:

Community	Probability
A	55%
B	25%
C	15%
D	5%

This ensures that A is expected to be the majority.

Steps

Select number of users (1000, 2000, 5000, etc.)

Assign communities using probability-based sampling

Convert to a pandas DataFrame

Save the dataset as:

my_social_network.csv


Load the CSV

Apply the Boyer–Moore algorithm on the entire dataset

Print the detected majority
This reflects the probability distribution (A = 55%).

🧠 About the Boyer–Moore Algorithm

The Boyer–Moore Majority Vote Algorithm is a classic method for identifying the majority element in a list.

Why It’s Powerful

✔ O(n) time

✔ O(1) space

✔ Ideal for big data and streaming

✔ Useful in network analysis, recommendation systems, and voting models

The algorithm works in two phases:

Candidate selection — Tracks the most likely majority

Verification — Confirms if the candidate truly occurs more than n/2 times

📂 Files in This Repository
File	Description
Untitled4.py	Contains the full implementation of Assignment 1 and Assignment 2
my_social_network.csv	Auto-generated dataset (created during runtime)
🚀 How to Run
Local Machine
pip install pandas
python Untitled4.py

Google Colab

Upload the script

Run all cells

The CSV file will automatically download

