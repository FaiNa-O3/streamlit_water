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
watering_time = ctrl.Consequent(np.arange(1, 90, 1), 'watering_time')

#===============================================================================================================================================#
# input ==== membership value
humidity_type['dry'] = fuzz.trapmf(humidity_type.universe, [0, 0, 25, 50])
humidity_type['moist'] = fuzz.trimf(humidity_type.universe, [25, 50, 75])
humidity_type['wet'] = fuzz.trapmf(humidity_type.universe, [50, 75, 100, 100])

sunshine_hour['short'] = fuzz.trapmf(sunshine_hour.universe, [0,0,2,6])
sunshine_hour['medium'] = fuzz.trimf(sunshine_hour.universe, [2,6,10])
sunshine_hour['long'] = fuzz.trapmf(sunshine_hour.universe, [6,10,12,12])

sun_radiation['light'] = fuzz.trapmf(sun_radiation.universe, [0,0,400,800])
sun_radiation['medium'] = fuzz.trimf(sun_radiation.universe, [400,800,1200])
sun_radiation['heavy'] = fuzz.trapmf(sun_radiation.universe, [800,1200,1600,1600])

delta_evaporation['small'] = fuzz.trapmf(delta_evaporation.universe, [0,0,1,3])
delta_evaporation['medium'] = fuzz.trimf(delta_evaporation.universe, [1,3,5])
delta_evaporation['large'] = fuzz.trapmf(delta_evaporation.universe, [3,5,6,6])

last_watering['short'] = fuzz.trapmf(last_watering.universe, [0, 0, 4, 7])
last_watering['medium'] = fuzz.trimf(last_watering.universe, [4, 7, 10])
last_watering['long'] = fuzz.trapmf(last_watering.universe, [7, 10, 14, 14])


# output ==== membership value
watering_time['VeryShort'] = fuzz.trapmf(watering_time.universe, [0, 0, 5, 10])
watering_time['Short'] = fuzz.trimf(watering_time.universe, [10, 20, 30])
watering_time['Medium'] = fuzz.trimf(watering_time.universe, [20, 40, 60])
watering_time['Long'] = fuzz.trimf(watering_time.universe, [50, 60, 70])
watering_time['VeryLong'] = fuzz.trapmf(watering_time.universe, [70, 80, 90, 90])

#===============================================================================================================================================#
# rules

rule1 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['small']&last_watering['short'], watering_time['VeryShort'])
rule2 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['small']&last_watering['short'], watering_time['VeryShort'])
rule3 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['small']&last_watering['short'], watering_time['VeryShort'])

rule4 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['small']&last_watering['short'], watering_time['Short'])
rule5 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['small']&last_watering['short'], watering_time['VeryShort'])
rule6 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['small']&last_watering['short'], watering_time['VeryShort'])

rule7 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['small']&last_watering['short'], watering_time['Short'])
rule8 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['small']&last_watering['short'], watering_time['VeryShort'])
rule9 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['small']&last_watering['short'], watering_time['VeryShort'])


rule10 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['medium']&last_watering['short'], watering_time['Short'])
rule11 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['medium']&last_watering['short'], watering_time['VeryShort'])
rule12 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['medium']&last_watering['short'], watering_time['VeryShort'])

rule13 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['medium']&last_watering['short'], watering_time['Short'])
rule14 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['medium']&last_watering['short'], watering_time['Short'])
rule15 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['medium']&last_watering['short'], watering_time['VeryShort'])

rule16 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['medium']&last_watering['short'], watering_time['Short'])
rule17 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['medium']&last_watering['short'], watering_time['Short'])
rule18 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['medium']&last_watering['short'], watering_time['VeryShort'])


rule19 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['large']&last_watering['short'], watering_time['Short'])
rule20 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['large']&last_watering['short'], watering_time['Short'])
rule21 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['large']&last_watering['short'], watering_time['Short'])

rule22 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['large']&last_watering['short'], watering_time['Medium'])
rule23 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['large']&last_watering['short'], watering_time['Short'])
rule24 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['large']&last_watering['short'], watering_time['Short'])

rule25 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['large']&last_watering['short'], watering_time['Medium'])
rule26 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['large']&last_watering['short'], watering_time['Short'])
rule27 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['large']&last_watering['short'], watering_time['Short'])




rule28 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['small']&last_watering['medium'], watering_time['Short'])
rule29 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['small']&last_watering['medium'], watering_time['Short'])
rule30 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['small']&last_watering['medium'], watering_time['Short'])

rule31 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['small']&last_watering['medium'], watering_time['Medium'])
rule32 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['small']&last_watering['medium'], watering_time['Short'])
rule33 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['small']&last_watering['medium'], watering_time['Short'])

rule34 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['small']&last_watering['medium'], watering_time['Medium'])
rule35 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['small']&last_watering['medium'], watering_time['Medium'])
rule36 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['small']&last_watering['medium'], watering_time['Short'])


rule37 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['medium']&last_watering['medium'], watering_time['Medium'])
rule38 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['medium']&last_watering['medium'], watering_time['Short'])
rule39 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['medium']&last_watering['medium'], watering_time['Short'])

rule40 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['medium']&last_watering['medium'], watering_time['Long'])
rule41 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['medium']&last_watering['medium'], watering_time['Medium'])
rule42 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['medium']&last_watering['medium'], watering_time['Short'])

rule43 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['medium']&last_watering['medium'], watering_time['Long'])
rule44 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['medium']&last_watering['medium'], watering_time['Medium'])
rule45 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['medium']&last_watering['medium'], watering_time['Short'])


rule46 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['large']&last_watering['medium'], watering_time['Medium'])
rule47 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['large']&last_watering['medium'], watering_time['Medium'])
rule48 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['large']&last_watering['medium'], watering_time['Short'])

rule49 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['large']&last_watering['medium'], watering_time['Long'])
rule50 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['large']&last_watering['medium'], watering_time['Long'])
rule51 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['large']&last_watering['medium'], watering_time['Medium'])

rule52 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['large']&last_watering['medium'], watering_time['Long'])
rule53 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['large']&last_watering['medium'], watering_time['Long'])
rule54 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['large']&last_watering['medium'], watering_time['Medium'])




rule55 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['small']&last_watering['long'], watering_time['Long'])
rule56 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['small']&last_watering['long'], watering_time['Medium'])
rule57 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['small']&last_watering['long'], watering_time['Short'])

rule58 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['small']&last_watering['long'], watering_time['Long'])
rule59 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['small']&last_watering['long'], watering_time['Long'])
rule60 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['small']&last_watering['long'], watering_time['Medium'])

rule61 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['small']&last_watering['long'], watering_time['VeryLong'])
rule62 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['small']&last_watering['long'], watering_time['Long'])
rule63 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['small']&last_watering['long'], watering_time['Medium'])


rule64 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['medium']&last_watering['long'], watering_time['VeryLong'])
rule65 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['medium']&last_watering['long'], watering_time['Long'])
rule66 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['medium']&last_watering['long'], watering_time['Medium'])

rule67 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['medium']&last_watering['long'], watering_time['VeryLong'])
rule68 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['medium']&last_watering['long'], watering_time['Long'])
rule69 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['medium']&last_watering['long'], watering_time['Medium'])

rule70 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['medium']&last_watering['long'], watering_time['VeryLong'])
rule71 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['medium']&last_watering['long'], watering_time['Long'])
rule72 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['medium']&last_watering['long'], watering_time['Medium'])


rule73 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['large']&last_watering['long'], watering_time['VeryLong'])
rule74 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['large']&last_watering['long'], watering_time['Long'])
rule75 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['short'] & sun_radiation ['light'] &delta_evaporation ['large']&last_watering['long'], watering_time['Long'])

rule76 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['large']&last_watering['long'], watering_time['VeryLong'])
rule77 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['large']&last_watering['long'], watering_time['Long'])
rule78 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['medium'] & sun_radiation ['medium'] &delta_evaporation ['large']&last_watering['long'], watering_time['Medium'])

rule79 = ctrl.Rule(humidity_type['dry']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['large']&last_watering['long'], watering_time['VeryLong'])
rule80 = ctrl.Rule(humidity_type['moist']    & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['large']&last_watering['long'], watering_time['VeryLong'])
rule81 = ctrl.Rule(humidity_type['wet']      & sunshine_hour ['long'] & sun_radiation ['heavy'] &delta_evaporation ['large']&last_watering['long'], watering_time['Medium'])

#===============================================================================================================================================#
water_ctrl1 = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, 
     rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
     rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, 
     rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36,
     rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45,
     rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54,
     rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63, 
     rule64, rule65, rule66, rule67, rule68, rule69, rule70, rule71, rule72, 
     rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80, rule81
])

water = ctrl.ControlSystemSimulation(water_ctrl1)
#===============================================================================================================================================#

humid = st.number_input('ENTER HUMIDITY 0-100%', min_value=0, max_value=100)
water.input['humidity_type'] = (humid)

sunshine = st.number_input('ENTER SUNSHINE HOUR 0-12 HOURS', min_value=0, max_value=12)
water.input['sunshine_hour'] = (sunshine)

radiation = st.number_input('ENTER SUN RADIATION 0-1600', min_value=0, max_value=1600)
water.input['sun_radiation'] = (radiation)

evaporation = st.number_input('ENTER DELTA EVAPORATION 0-6MM', min_value=0, max_value=6)
water.input['delta_evaporation'] = (evaporation)

last_water = st.number_input('ENTER LAST WATERING TIME 0-14 DAYS', min_value=0, max_value=14)
water.input['last_watering'] = (last_water)


#===============================================================================================================================================#

water.input['humidity_type'] = (humid)
water.input['sunshine_hour'] = (sunshine)
water.input['sun_radiation'] = (radiation)
water.input['delta_evaporation'] = (evaporation)
water.input['last_watering'] = (last_water)

#===============================================================================================================================================#
water.compute()
if st.button("calculate watering time!"):

    st.write(water.output['watering_time'])
