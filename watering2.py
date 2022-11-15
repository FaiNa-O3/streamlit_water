import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import skfuzzy as fuzz
import streamlit as st

st.title('WATERING TIME USING FUZZY LOGIC')

# input
humidity_type = ctrl.Antecedent(np.arange(1, 101, 1), 'humidity_type')
last_watering = ctrl.Antecedent(np.arange(1, 15, 1), 'last_watering')


# output
watering_time = ctrl.Consequent(np.arange(1, 120, 1), 'watering_time')

# input ==== membership value
humidity_type['dry'] = fuzz.trapmf(humidity_type.universe, [1, 1, 25, 50])
humidity_type['moist'] = fuzz.trimf(humidity_type.universe, [25, 50, 75])
humidity_type['wet'] = fuzz.trapmf(humidity_type.universe, [50, 75, 100, 100])

last_watering['short'] = fuzz.trapmf(last_watering.universe, [1, 1, 4, 7])
last_watering['medium'] = fuzz.trimf(last_watering.universe, [4, 7, 10])
last_watering['long'] = fuzz.trapmf(last_watering.universe, [7, 10, 14, 14])


# output ==== membership value
watering_time['VeryShort'] = fuzz.trapmf(
    watering_time.universe, [1, 1, 10, 20])
watering_time['Short'] = fuzz.trimf(watering_time.universe, [5, 20, 35])
watering_time['Medium'] = fuzz.trimf(watering_time.universe, [35, 50, 65])
watering_time['Long'] = fuzz.trimf(watering_time.universe, [50, 65, 80])
watering_time['VeryLong'] = fuzz.trapmf(
    watering_time.universe, [80, 95, 110, 120])

# rules

rule1 = ctrl.Rule(humidity_type['dry'] |
                  last_watering['short'], watering_time['Short'])
rule2 = ctrl.Rule(humidity_type['moist'] |
                  last_watering['short'], watering_time['VeryShort'])
rule3 = ctrl.Rule(
    humidity_type['wet'] | last_watering['short'], watering_time['VeryShort'])

rule4 = ctrl.Rule(humidity_type['dry'] |
                  last_watering['medium'], watering_time['Medium'])
rule5 = ctrl.Rule(humidity_type['moist'] |
                  last_watering['medium'], watering_time['Short'])
rule6 = ctrl.Rule(humidity_type['wet'] |
                  last_watering['medium'], watering_time['VeryShort'])

rule7 = ctrl.Rule(humidity_type['dry'] |
                  last_watering['long'], watering_time['VeryLong'])
rule8 = ctrl.Rule(humidity_type['moist'] |
                  last_watering['long'], watering_time['Long'])
rule9 = ctrl.Rule(humidity_type['wet'] |
                  last_watering['long'], watering_time['Medium'])


water_ctrl1 = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

water = ctrl.ControlSystemSimulation(water_ctrl1)


humid = st.number_input('Enter user humid', min_value=1, max_value=101)
water.input['humidity_type'] = (humid)


last_water = st.number_input(
    'Enter user last watering time', min_value=1, max_value=14)
water.input['last_watering'] = (last_water)

water.input['humidity_type'] = (humid)
water.input['last_watering'] = (last_water)


water.compute()
if st.button("watering time"):

    st.write(water.output['watering_time'])
