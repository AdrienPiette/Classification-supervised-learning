# streamlit 

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Load data

df = pd.read_csv('../Data/NASA.csv')

# Title

st.title('NASA Nearest Earth Objects (1910-2024)')

# Sidebar

st.sidebar.header('Overwiew of the data')

st.sidebar.write('This dataset contains information about the Near Earth Objects (NEOs) that have been detected by NASA from 1910 to 2024. The data includes information about the size, velocity, and distance of the NEOs from Earth. The dataset also includes information about the date and time of the NEOs closest approach to Earth.')

