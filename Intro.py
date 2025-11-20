

This assignment uses a manually defined set of community labels to understand how Boyer–Moore selects the majority.

Dataset Used

A small community list:

["A", "A", "B", "A", "A", "C", "A", "B", "A", "A"]

Goal

Determine which community appears more than 50% of the time.

Steps

Create a small list of community labels

Apply Boyer–Moore algorithm:

Select a candidate

Maintain running count

Replace candidate when count reaches zero

Verify if the candidate is the actual majority

Print final majority community

Output
Majority Community in Network: A


This demonstrates how the majority class can be identified without needing extra memory.

# Assignment 2 — Big Data Analysis
Topic: Majority Detection Using Boyer–Moore on a Large Synthetic Dataset

This assignment focuses on large-scale community analysis using a generated dataset of 1000+ users.

Goal

Generate a big dataset with community probabilities and identify the majority efficiently.

Dataset Generation

A synthetic dataset is created using probability distribution:

Community	Probability
A	55%
B	25%
C	15%
D	5%
Steps

Select number of users (e.g., 1000, 2000, 5000)

Assign random communities to each user following the probability distribution

Store the results in a pandas DataFrame

Save the dataset as:

my_social_network.csv


Load the CSV file

Apply Boyer–Moore Majority Vote Algorithm on the entire column

Print the detected majority community

Expected Output
Majority Community: A


This matches the dataset distribution (A = 55%).

About the Boyer–Moore Algorithm

The Boyer–Moore Majority Vote Algorithm is a powerful technique used to find majority elements in linear time:

Time Complexity: O(n)

Space Complexity: O(1)

Works best for majority detection in streams and large datasets

Ideal for Social Network Analysis, Recommendation Systems, and Big Data pipelines

Files in This Repository
File	Description
Untitled4.py	Contains both SNA and Big Data Analysis implementations
my_social_network.csv	Auto-generated dataset (generated when running the script)
