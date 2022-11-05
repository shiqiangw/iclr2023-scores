# ICLR 2023 Scores from OpenReview

A simple script to extract scores of publicly available ICLR submissions from OpenReview.

Prerequisite: Install the OpenReview Python client following Step 1 in https://docs.openreview.net/getting-started/using-the-api/installing-and-instantiating-the-python-client

Run `python3 main.py` to get a spreadsheet including paper titles and scores, in CSV format. The result is saved in `output.csv`.

Open `output.csv` in a software such as MS Excel. Then you can do manual sorting according to the average score or collect other statistics.

Note: Withdrawn papers are excluded from the output.

**Recommendation:** Let's not overload the OpenReview server, so don't run this too often :)