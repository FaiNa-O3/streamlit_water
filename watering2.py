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

#===============================================================================================================================================#
# input
humidity_type = ctrl.Antecedent(np.arange(0, 100, 1), 'humidity_type')
sunshine_hour = ctrl.Antecedent(np.arange(0, 12, 1), 'sunshine_hour')
sun_radiation = ctrl.Antecedent(np.arange(0, 1600, 1), 'sun_radiation')
delta_evaporation = ctrl.Antecedent(np.arange(0, 6, 1), 'delta_evaporation')
last_watering = ctrl.Antecedent(np.arange(0, 14, 1), 'last_watering')


# output
watering_time = ctrl.Consequent(np.arange(1, 20, 1), 'watering_time')

#===============================================================================================================================================#
# input ==== membership value
humidity_type['dry'] = fuzz.trapmf(humidity_type.universe, [1, 1, 25, 50])
humidity_type['moist'] = fuzz.trimf(humidity_type.universe, [25, 50, 75])
humidity_type['wet'] = fuzz.trapmf(humidity_type.universe, [50, 75, 100, 100])

sunshine_hour['short'] = fuzz.trapmf(sunshine_hour.universe, [1,1,2,6])
sunshine_hour['medium'] = fuzz.trimf(sunshine_hour.universe, [2,6,10])
sunshine_hour['long'] = fuzz.trapmf(sunshine_hour.universe, [6,10,12,12])

sun_radiation['light'] = fuzz.trapmf(sun_radiation.universe, [1,1,400,800])
sun_radiation['medium'] = fuzz.trimf(sun_radiation.universe, [400,800,1200])
sun_radiation['heavy'] = fuzz.trapmf(sun_radiation.universe, [800,1200,1600,1600])

delta_evaporation['small'] = fuzz.trapmf(delta_evaporation.universe, [1,1,1,3])
delta_evaporation['medium'] = fuzz.trimf(delta_evaporation.universe, [1,3,5])
delta_evaporation['large'] = fuzz.trapmf(delta_evaporation.universe, [3,5,6,6])

last_watering['short'] = fuzz.trapmf(last_watering.universe, [1, 1, 4, 7])
last_watering['medium'] = fuzz.trimf(last_watering.universe, [4, 7, 10])
last_watering['long'] = fuzz.trapmf(last_watering.universe, [7, 10, 14, 14])


# output ==== membership value
watering_time['VeryShort'] = fuzz.trapmf(watering_time.universe, [1, 1, 5, 10])
watering_time['Short'] = fuzz.trimf(watering_time.universe, [10, 20, 30])
watering_time['Medium'] = fuzz.trimf(watering_time.universe, [30, 40, 50])
watering_time['Long'] = fuzz.trimf(watering_time.universe, [50, 60, 70])
watering_time['VeryLong'] = fuzz.trapmf(watering_time.universe, [70, 80, 90, 120])

#===============================================================================================================================================#
# rules

rule1 = ctrl.Rule(humidity_type['dry']      | sunshine_hour ['short'] | sun_radiation ['light'] |delta_evaporation ['small']|last_watering['short'], watering_time['Short'])
rule2 = ctrl.Rule(humidity_type['moist']    | sunshine_hour ['short'] | sun_radiation ['light'] |delta_evaporation ['small']|last_watering['short'], watering_time['Short'])
rule3 = ctrl.Rule(humidity_type['wet']      | sunshine_hour ['short'] | sun_radiation ['light'] |delta_evaporation ['small']|last_watering['short'], watering_time['Short'])

rule4 = ctrl.Rule(humidity_type['dry']      | sunshine_hour ['medium'] | sun_radiation ['medium'] |delta_evaporation ['small']|last_watering['short'], watering_time['Short'])
rule5 = ctrl.Rule(humidity_type['moist']    | sunshine_hour ['medium'] | sun_radiation ['medium'] |delta_evaporation ['small']|last_watering['short'], watering_time['Short'])
rule6 = ctrl.Rule(humidity_type['wet']      | sunshine_hour ['medium'] | sun_radiation ['medium'] |delta_evaporation ['small']|last_watering['short'], watering_time['Short'])

rule7 = ctrl.Rule(humidity_type['dry']      | sunshine_hour ['long'] | sun_radiation ['heavy'] |delta_evaporation ['small']|last_watering['short'], watering_time['Short'])
rule8 = ctrl.Rule(humidity_type['moist']    | sunshine_hour ['long'] | sun_radiation ['heavy'] |delta_evaporation ['small']|last_watering['short'], watering_time['Short'])
rule9 = ctrl.Rule(humidity_type['wet']      | sunshine_hour ['long'] | sun_radiation ['heavy'] |delta_evaporation ['small']|last_watering['short'], watering_time['Short'])


rule10 = ctrl.Rule(humidity_type['dry']      | sunshine_hour ['short'] | sun_radiation ['light'] |delta_evaporation ['medium']|last_watering['short'], watering_time['Short'])
rule11 = ctrl.Rule(humidity_type['moist']    | sunshine_hour ['short'] | sun_radiation ['light'] |delta_evaporation ['medium']|last_watering['short'], watering_time['Short'])
rule12 = ctrl.Rule(humidity_type['wet']      | sunshine_hour ['short'] | sun_radiation ['light'] |delta_evaporation ['medium']|last_watering['short'], watering_time['Short'])

rule13 = ctrl.Rule(humidity_type['dry']      | sunshine_hour ['medium'] | sun_radiation ['medium'] |delta_evaporation ['medium']|last_watering['short'], watering_time['Short'])
rule14 = ctrl.Rule(humidity_type['moist']    | sunshine_hour ['medium'] | sun_radiation ['medium'] |delta_evaporation ['medium']|last_watering['short'], watering_time['Short'])
rule15 = ctrl.Rule(humidity_type['wet']      | sunshine_hour ['medium'] | sun_radiation ['medium'] |delta_evaporation ['medium']|last_watering['short'], watering_time['Short'])

rule16 = ctrl.Rule(humidity_type['dry']      | sunshine_hour ['long'] | sun_radiation ['heavy'] |delta_evaporation ['medium']|last_watering['short'], watering_time['Short'])
rule17 = ctrl.Rule(humidity_type['moist']    | sunshine_hour ['long'] | sun_radiation ['heavy'] |delta_evaporation ['medium']|last_watering['short'], watering_time['Short'])
rule18 = ctrl.Rule(humidity_type['wet']      | sunshine_hour ['long'] | sun_radiation ['heavy'] |delta_evaporation ['medium']|last_watering['short'], watering_time['Short'])


rule19 = ctrl.Rule(humidity_type['dry']      | sunshine_hour ['short'] | sun_radiation ['light'] |delta_evaporation ['large']|last_watering['short'], watering_time['Short'])
rule20 = ctrl.Rule(humidity_type['moist']    | sunshine_hour ['short'] | sun_radiation ['light'] |delta_evaporation ['large']|last_watering['short'], watering_time['Short'])
rule21 = ctrl.Rule(humidity_type['wet']      | sunshine_hour ['short'] | sun_radiation ['light'] |delta_evaporation ['large']|last_watering['short'], watering_time['Short'])

rule22 = ctrl.Rule(humidity_type['dry']      | sunshine_hour ['medium'] | sun_radiation ['medium'] |delta_evaporation ['large']|last_watering['short'], watering_time['Medium'])
rule23 = ctrl.Rule(humidity_type['moist']    | sunshine_hour ['medium'] | sun_radiation ['medium'] |delta_evaporation ['large']|last_watering['short'], watering_time['Short'])
rule24 = ctrl.Rule(humidity_type['wet']      | sunshine_hour ['medium'] | sun_radiation ['medium'] |delta_evaporation ['large']|last_watering['short'], watering_time['Short'])

rule25 = ctrl.Rule(humidity_type['dry']      | sunshine_hour ['long'] | sun_radiation ['heavy'] |delta_evaporation ['large']|last_watering['short'], watering_time['Medium'])
rule26 = ctrl.Rule(humidity_type['moist']    | sunshine_hour ['long'] | sun_radiation ['heavy'] |delta_evaporation ['large']|last_watering['short'], watering_time['Medium'])
rule27 = ctrl.Rule(humidity_type['wet']      | sunshine_hour ['long'] | sun_radiation ['heavy'] |delta_evaporation ['large']|last_watering['short'], watering_time['Short'])

#===============================================================================================================================================#
water_ctrl1 = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
    rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, 
    #rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, 
    #rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50, rule51, rule52, 
    #rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69, 
    #rule70, rule71, rule72, rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80, rule81
])

water = ctrl.ControlSystemSimulation(water_ctrl1)
#===============================================================================================================================================#

humid = st.number_input('ENTER HUMIDITY', min_value=1, max_value=100)
water.input['humidity_type'] = (humid)

sunshine = st.number_input('ENTER SUNSHINE HOUR', min_value=1, max_value=12)
water.input['sunshine_hour'] = (sunshine)

radiation = st.number_input('ENTER SUN RADIATION', min_value=1, max_value=1600)
water.input['sun_radiation'] = (radiation)

evaporation = st.number_input('ENTER DELTA EVAPORATION', min_value=1, max_value=6)
water.input['delta_evaporation'] = (evaporation)

last_water = st.number_input('ENTER LAST WATERING TIME', min_value=1, max_value=14)
water.input['last_watering'] = (last_water)


#===============================================================================================================================================#

water.input['humidity_type'] = (humid)
water.input['sunshine_hour'] = (sunshine)
water.input['sun_radiation'] = (radiation)
water.input['delta_evaporation'] = (evaporation)
water.input['last_watering'] = (last_water)

#===============================================================================================================================================#
water.compute()
if st.button("watering time"):

    st.write(water.output['watering_time'])
