# importing packages
import pulp
import pandas as pd

# formatting csv data for the parent timings into a manipulable form with pandas
parent_timings_csv = 'parents_timings.csv'
parent_timings = pd.read_csv(parent_timings_csv)
