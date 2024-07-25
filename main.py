import pandas as pd
import matplotlib.pyplot as plt
from DigiPythonTools import DataUtility
# Function to plot tag data
def plot_tag_data(df, tag_name, month_name):
    plt.figure(figsize=(14, 7))
    plt.plot(df['TagDateTime'], df['TagValue'], label=tag_name)
    plt.xlabel('DateTime')
    plt.ylabel('Value')
    plt.title(f'{tag_name} values for {month_name}')
    plt.legend()
    plt.show()

min_sql = DataUtility()

# query = 'SELECT MIN(TagDateTime) AS mintime, MAX(TagDateTime) AS maxtime  FROM DigiProcessInfo.tblLpFmRtFceTrendData '
query_march = """SELECT *
FROM DigiProcessInfo.tblLpFmRtFceTrendData
WHERE CONVERT(VARCHAR(10), TagDateTime, 120) LIKE '2024-03-%';
"""

query_december = """SELECT *
FROM DigiProcessInfo.tblLpFmRtFceTrendData
WHERE CONVERT(VARCHAR(10), TagDateTime, 120) LIKE '2023-12-%';
"""

query_november = """SELECT *
FROM DigiProcessInfo.tblLpFmRtFceTrendData
WHERE CONVERT(VARCHAR(10), TagDateTime, 120) LIKE '2023-11-%';
"""

# Load data for each month
march_df = min_sql.min_query(query_march)
december_df = min_sql.min_query(query_december)
november_df = min_sql.min_query(query_november)

# List of tags
tags = [
'RTFCE1_Zone1AirGasRatio'
'RTFCE1_Zone1TempDer'
'RTFCE1_Zone1AirValveGain'
'RTFCE1_Zone1GasValveDer'
'RTFCE1_Zone1RationSP'
'RTFCE1_Zone1AirValveSP'
'RTFCE1_Zone1GasFlow'
'RTFCE1_Zone1GasValveOut'
'RTFCE1_Zone1GasValvePos'
'RTFCE1_Zone1TempGain'
'RTFCE1_Zone1AirValveOut'
'RTFCE1_Zone1TempOutput'
'RTFCE1_Zone1GasValveGain'
'RTFCE1_Zone1TempInt'
'RTFCE1_Zone1AirFlowSCFH'
'RTFCE1_Zone1TempSP'
'RTFCE1_Zone1AirValveInt'
'RTFCE1_Zone1AirValvePos'
'RTFCE1_Zone1O2SensorFDBK'
'RTFCE1_Zone1GasValveInt'
'RTFCE1_Zone1GasFlowSCFH'
'RTFCE1_Zone1GasValveSP'
'RTFCE1_Zone1AirFlow'
'RTFCE1_Zone1TempFDBK'
'RTFCE1_Zone1AirValveDer'
]

# # Plot data for each tag
# for tag in tags:
#     plot_tag_data(march_df, tag, 'March')
#     plot_tag_data(november_df, tag, 'November')

march_df['index'] = march_df.groupby('TagDateTime').cumcount()
pivot_df = march_df.pivot( columns='TagName', values='TagValue')

pivot_df.reset_index(inplace=True)

print(pivot_df.head())
print(march_df.tail())