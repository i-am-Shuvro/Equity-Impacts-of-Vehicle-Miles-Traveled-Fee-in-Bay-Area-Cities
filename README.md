Equity Impacts of a Vehicle Miles Traveled (VMT) Fee in Bay Area Cities

Project Objective
This project evaluates the equity and distributional impacts of replacing California’s state fuel tax with a Vehicle Miles Traveled (VMT) fee in selected San Francisco Bay Area cities. The analysis compares household transportation cost burdens across income groups and urban versus rural locations, and examines how results change when driving behavior responds to pricing.

Data
The analysis uses household-level data from the 2017 National Household Travel Survey (NHTS). Vehicle fuel economy is estimated using federal fuel-economy standards due to missing MPG values in the survey. Only California state fuel taxes are replaced in the VMT scenarios. Federal fuel taxes remain constant across all scenarios. 
Data Structure:
data/

├── raw_data/ # Original NHTS survey files and fuel economy standards

└── cleaned_data/ # Final analysis-ready dataset

    └── df_cleanest+mpg.csv

    
Code
All code is fully reproducible and divided into data preparation and policy analysis. 
Code Structure:
codes/

├── codes_for_data_cleaning/

│   ├── data_cleaning.ipynb

│   └── data_cleaning.py

└── codes_for_results/

    ├── bayarea_vmt_analysis.ipynb  
    └── bayarea_vmt_analysis.py
    
* Data cleaning scripts convert raw NHTS data into a single cleaned dataset.
* Analysis scripts implement the policy scenarios, estimate behavioral response, and compute equity metrics.

Policy Scenarios
Four scenarios are evaluated:
1. Fuel Tax (Baseline): Current California state fuel tax system.
2. Static VMT Fee: Fuel tax replaced with a per-mile fee, holding household driving constant.
3. Dynamic VMT Fee (Modified Elasticities): Household VMT adjusts to cost changes, but positive elasticities are removed to prevent increases in driving.
4. Dynamic VMT Fee (Raw Elasticities): Full behavioral response using estimated elasticities, allowing VMT to increase or decrease.

Equity Assessment
Equity is evaluated using the Gini Index, calculated for:
1. Urban households
2. Rural households
3. All households combined
Gini values are used to compare inequality under the fuel tax and VMT fee scenarios.

Results
Final outputs are stored in the results/ folder:
results/
├── scenario1_fuel_tax.csv
├── scenario2_static_vmt.csv
├── scenario3_dynamic_modified.csv
├── scenario4_dynamic_raw.csv
└── gini_summary.csv

Key findings include:
* Rural households face higher average burdens in all scenarios.
* Static VMT fees produce small changes relative to the fuel tax.
* Dynamic scenarios increase burdens for lower-income households due to behavioral response.
* Overall inequality (Gini Index) remains relatively stable across scenarios.

How to Reproduce:
1. Run the scripts in codes/codes_for_data_cleaning/ to generate df_cleanest+mpg.csv
2. Run the scripts in codes/codes_for_results/ to generate scenario results and Gini indices
3. All outputs will be saved automatically to the results/ folder

Limitations
* Analysis covers a limited set of Bay Area cities
* Rural households are underrepresented in the sample
* Fuel economy values are estimated
* Results are based on 2017 NHTS data

Acknowledgments
This project was completed for an academic course under the guidance of Professor Manxi Wu (UC Berkeley). ChatGPT 4.0 was used to assist with code debugging, workflow structuring, and writing clarity.

Citation
Equity Impacts of a Vehicle Miles Traveled (VMT) Fee in Bay Area Cities
