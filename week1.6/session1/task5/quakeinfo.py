# Week 1.6, Session 1: Task 5
from dataset import QuakeDataset,QuakeFeed
q= QuakeDataset(QuakeFeed("all","hour"))
q.read_feed()
print(q.strongest_quake())

# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

# See README.md for full details of what is required and what
# program output should look like
