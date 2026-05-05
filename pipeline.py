# Wheeler Wilkinson Project - Data Pipeline

import pandas as pd
import matplotlib.pyplot as plt
import hashlib

def verify_data_integrity(data_string, expected_hash):
    """Verifies that the data matches the expected SHA-256 hash."""
    actual_hash = hashlib.sha256(data_string.encode('utf-8')).hexdigest()
    
    if actual_hash == expected_hash:
        print("Hash match: Data is verified and untouched!")
    else:
        print("Hash mismatch! The data has been altered.")
        print(f"Expected: {expected_hash}")
        print(f"Actual:   {actual_hash}")

print("==========================================")
print(" Downloading datasets... (This may take 6-8 minutes)")
print("==========================================")

# Load Chicago Data
chicago_url = 'https://data.cityofchicago.org/api/views/qzdf-xmn8/rows.csv?accessType=DOWNLOAD'
chicago = pd.read_csv(chicago_url)
print(f"Chicago dataset loaded. Shape: {chicago.shape}")

# Load LA Data
la_url = 'https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD'
LA = pd.read_csv(la_url)
print(f"LA dataset loaded. Shape: {LA.shape}")

print("\n--- Cleaning & Formatting ---")

# Clean LA Date
LA['DATE OCC'] = pd.to_datetime(LA['DATE OCC'])
LA = LA[LA['DATE OCC'].dt.year == 2020]
LA['DATE OCC'] = LA['DATE OCC'].dt.strftime('%m/%d/%Y %I:%M:%S %p')

# Unified Crime Mapping Dictionary (Generated via Gemini)
unified_mapping = {
    'HOMICIDE': ['HOMICIDE', 'CRIMINAL HOMICIDE', 'MANSLAUGHTER, NEGLIGENT'],
    'ASSAULT & BATTERY': [
        'BATTERY', 'ASSAULT', 'INTIMIDATION', 'STALKING',
        'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT', 'INTIMATE PARTNER - SIMPLE ASSAULT',
        'BATTERY - SIMPLE ASSAULT', 'CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT',
        'CRIMINAL THREATS - NO WEAPON DISPLAYED', 'BATTERY WITH SEXUAL CONTACT',
        'INTIMATE PARTNER - AGGRAVATED ASSAULT', 'BATTERY POLICE (SIMPLE)', 'OTHER ASSAULT',
        'ASSAULT WITH DEADLY WEAPON ON POLICE OFFICER', 'CHILD ABUSE (PHYSICAL) - AGGRAVATED ASSAULT',
        'BATTERY ON A FIREFIGHTER', 'THREATENING PHONE CALLS/LETTERS'
    ],
    'SEX OFFENSES': [
        'SEX OFFENSE', 'CRIMINAL SEXUAL ASSAULT', 'CRIM SEXUAL ASSAULT', 'PROSTITUTION',
        'OBSCENITY', 'PUBLIC INDECENCY', 'LEWD/LASCIVIOUS ACTS WITH CHILD', 'RAPE, ATTEMPTED', 
        'SODOMY/SEXUAL CONTACT B/W PENIS OF ONE PERS TO ANUS OTH', 'RAPE, FORCIBLE', 
        'SEX OFFENDER REGISTRANT OUT OF COMPLIANCE', 'SEX,UNLAWFUL(INC MUTUAL CONSENT, PENETRATION W/ FRGN OBJ',
        'ORAL COPULATION', 'SEXUAL PENETRATION W/FOREIGN OBJECT', 'LEWD CONDUCT', 'INDECENT EXPOSURE',
        'CHILD PORNOGRAPHY', 'PANDERING', 'PIMPING', 'BEASTIALITY, CRIME AGAINST NATURE SEXUAL ASSLT WITH ANIM',
        'INCEST (SEXUAL ACTS BETWEEN BLOOD RELATIVES)', 'LETTERS, LEWD - TELEPHONE CALLS, LEWD'
    ],
    'CRIMES AGAINST CHILDREN': [
        'OFFENSE INVOLVING CHILDREN', 'CRM AGNST CHLD (13 OR UNDER) (14-15 & SUSP 10 YRS OLDER)', 
        'CHILD NEGLECT (SEE 300 W.I.C.)', 'CONTRIBUTING', 'CHILD ANNOYING (17YRS & UNDER)', 'CHILD ABANDONMENT'
    ],
    'ROBBERY': ['ROBBERY', 'ATTEMPTED ROBBERY', 'PURSE SNATCHING', 'PURSE SNATCHING - ATTEMPT'],
    'BURGLARY': ['BURGLARY', 'BURGLARY FROM VEHICLE', 'BURGLARY, ATTEMPTED', 'BURGLARY FROM VEHICLE, ATTEMPTED'],
    'THEFT / LARCENY': [
        'THEFT', 'THEFT OF IDENTITY', 'THEFT PLAIN - PETTY ($950 & UNDER)', 
        'THEFT-GRAND ($950.01 & OVER)EXCPT,GUNS,FOWL,LIVESTK,PROD', 'THEFT, PERSON', 
        'SHOPLIFTING - PETTY THEFT ($950 & UNDER)', 'SHOPLIFTING-GRAND THEFT ($950.01 & OVER)',
        'PICKPOCKET', 'THEFT PLAIN - ATTEMPT', 'SHOPLIFTING - ATTEMPT', 'THEFT, COIN MACHINE - PETTY ($950 & UNDER)',
        'THEFT FROM PERSON - ATTEMPT', 'THEFT, COIN MACHINE - ATTEMPT', 'PETTY THEFT - AUTO REPAIR',
        'GRAND THEFT / AUTO REPAIR', 'THEFT, COIN MACHINE - GRAND ($950.01 & OVER)', 'TILL TAP - PETTY ($950 & UNDER)',
        'PICKPOCKET, ATTEMPT', 'TILL TAP - GRAND THEFT ($950.01 & OVER)', 'DEFRAUDING INNKEEPER/THEFT OF SERVICES, $950 & UNDER',
        'DEFRAUDING INNKEEPER/THEFT OF SERVICES, OVER $950.01', 'THEFT FROM MOTOR VEHICLE - GRAND ($950.01 AND OVER)',
        'THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)', 'THEFT FROM MOTOR VEHICLE - ATTEMPT'
    ],
    'MOTOR VEHICLE THEFT': [
        'MOTOR VEHICLE THEFT', 'VEHICLE - STOLEN', 'VEHICLE - ATTEMPT STOLEN', 'BIKE - STOLEN', 
        'VEHICLE, STOLEN - OTHER (MOTORIZED SCOOTERS, BIKES, ETC)', 'DRIVING WITHOUT OWNER CONSENT (DWOC)', 
        'BOAT - STOLEN', 'BIKE - ATTEMPTED STOLEN'
    ],
    'DRUGS & NARCOTICS': ['NARCOTICS', 'OTHER NARCOTIC VIOLATION', 'DRUGS, TO A MINOR'],
    'WEAPONS OFFENSES': [
        'WEAPONS VIOLATION', 'CONCEALED CARRY LICENSE VIOLATION', 'FIREARMS RESTRAINING ORDER (FIREARMS RO)', 
        'BRANDISH WEAPON', 'DISCHARGE FIREARMS/SHOTS FIRED', 'SHOTS FIRED AT MOVING VEHICLE, TRAIN OR AIRCRAFT', 
        'SHOTS FIRED AT INHABITED DWELLING', 'REPLICA FIREARMS(SALE,DISPLAY,MANUFACTURE OR DISTRIBUTE)', 
        'WEAPONS POSSESSION/BOMBING', 'FIREARMS EMERGENCY PROTECTIVE ORDER (FIREARMS EPO)'
    ],
    'FRAUD & WHITE COLLAR': [
        'DECEPTIVE PRACTICE', 'EMBEZZLEMENT, GRAND THEFT ($950.01 & OVER)', 'BUNCO, ATTEMPT', 
        'DOCUMENT FORGERY / STOLEN FELONY', 'BUNCO, GRAND THEFT', 'BUNCO, PETTY THEFT', 'DISHONEST EMPLOYEE - PETTY THEFT', 
        'EMBEZZLEMENT, PETTY THEFT ($950 & UNDER)', 'CREDIT CARDS, FRAUD USE ($950 & UNDER', 'DOCUMENT WORTHLESS ($200 & UNDER)', 
        'CREDIT CARDS, FRAUD USE ($950.01 & OVER)', 'COUNTERFEIT', 'DISHONEST EMPLOYEE - GRAND THEFT', 
        'DOCUMENT WORTHLESS ($200.01 & OVER)', 'GRAND THEFT / INSURANCE FRAUD', 'DISHONEST EMPLOYEE ATTEMPTED THEFT', 
        'BRIBERY', 'EXTORTION', 'UNAUTHORIZED COMPUTER ACCESS'
    ],
    'VANDALISM & PROPERTY DAMAGE': [
        'CRIMINAL DAMAGE', 'ARSON', 'VANDALISM - MISDEAMEANOR ($399 OR UNDER)', 
        'VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS)', 'THROWING OBJECT AT MOVING VEHICLE', 
        'TELEPHONE PROPERTY - DAMAGE', 'ILLEGAL DUMPING'
    ],
    'PUBLIC ORDER & TRESPASS': [
        'CRIMINAL TRESPASS', 'PUBLIC PEACE VIOLATION', 'LIQUOR LAW VIOLATION', 'INTERFERENCE WITH PUBLIC OFFICER',
        'VIOLATION OF COURT ORDER', 'VIOLATION OF RESTRAINING ORDER', 'CONTEMPT OF COURT', 'TRESPASSING', 'FAILURE TO YIELD',
        'RESISTING ARREST', 'VIOLATION OF TEMPORARY RESTRAINING ORDER', 'DISTURBING THE PEACE', 'RECKLESS DRIVING',
        'PROWLER', 'DISRUPT SCHOOL', 'FAILURE TO DISPERSE', 'BLOCKING DOOR INDUCTION CENTER', 'INCITING A RIOT',
        'FALSE POLICE REPORT', 'PEEPING TOM', 'BOMB SCARE'
    ],
    'KIDNAPPING & TRAFFICKING': [
        'KIDNAPPING', 'HUMAN TRAFFICKING', 'CHILD STEALING', 'HUMAN TRAFFICKING - COMMERCIAL SEX ACTS', 
        'KIDNAPPING - GRAND ATTEMPT', 'FALSE IMPRISONMENT', 'HUMAN TRAFFICKING - INVOLUNTARY SERVITUDE'
    ],
    'OTHER / MISCELLANEOUS': [
        'OTHER OFFENSE', 'GAMBLING', 'RITUALISM', 'NON-CRIMINAL', 'OTHER MISCELLANEOUS CRIME', 'LYNCHING', 
        'CRUELTY TO ANIMALS', 'CONSPIRACY', 'DRUNK ROLL', 'LYNCHING - ATTEMPTED', 'BIGAMY', 'TRAIN WRECKING', 
        'DRUNK ROLL - ATTEMPT'
    ]
}

# Reverse the dictionary
flat_mapping = {}
for new_category, old_values in unified_mapping.items():
    for old_val in old_values:
        flat_mapping[old_val.strip()] = new_category

# Apply mapping
chicago['Unified_Crime_Type'] = chicago['Primary Type'].str.strip().map(flat_mapping).fillna('UNMAPPED')
LA['Unified_Crime_Type'] = LA['Crm Cd Desc'].str.strip().map(flat_mapping).fillna('UNMAPPED')

print("\n--- Verifying Data Integrity (SHA-256) ---")
EXPECTED_CHICAGO_HASH = "3d3c2dcd46ab8316cc87f1d4f35ffcf4282fb008970febce7e17e4a239080018"
chicago_types_string = str(chicago['Unified_Crime_Type'].unique())
verify_data_integrity(chicago_types_string, EXPECTED_CHICAGO_HASH)

# Formatting columns
chicago = chicago[['Date', 'Latitude', 'Longitude', 'Unified_Crime_Type']]
chicago['City'] = 'CHICAGO'
chicago = chicago.rename(columns={'Date': 'Date', 'Latitude': 'Latitude', 'Longitude': 'Longitude'})

LA = LA[['DATE OCC', 'LAT', 'LON', 'Unified_Crime_Type']]
LA['City'] = 'LA'
LA = LA.rename(columns={'DATE OCC': 'Date', 'LAT': 'Latitude', 'LON': 'Longitude'})

# Combine and Export CSVs
print("\n--- Saving Cleaned CSVs ---")
combined_crime = pd.concat([chicago, LA], ignore_index=True)

chicago.to_csv('Chicago_Crime_Cleaned.csv', index=False)
LA.to_csv('LA_Crime_Cleaned.csv', index=False)
combined_crime.to_csv('Combined_Crime_Cleaned.csv', index=False)
print("CSVs saved successfully.")

print("\n--- Processing Temporal Data ---")
combined_crime['Date'] = pd.to_datetime(combined_crime['Date'])
combined_crime = combined_crime.sort_values(by='Date', ascending=True).reset_index(drop=True)
combined_crime['Date'] = combined_crime['Date'].dt.normalize()

# Filter by month
months_dfs = [combined_crime[combined_crime['Date'].dt.month == i] for i in range(1, 13)]
jan_2020, feb_2020, mar_2020, apr_2020, may_2020, jun_2020, jul_2020, aug_2020, sep_2020, oct_2020, nov_2020, dec_2020 = months_dfs
months_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
crime_counts = [len(df) for df in months_dfs]

print("\n--- Generating and Saving Charts ---")

# 1. Jan 2020 Crime Types Bar Chart
jan_2020['Unified_Crime_Type'].value_counts().plot(kind='bar', figsize=(10, 6))
plt.title('Crime Types in January 2020')
plt.xlabel('Unified Crime Type')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('chart_1_Jan2020_CrimeTypes.png')
plt.close()

# 2. Total Monthly Crimes Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(months_labels, crime_counts, color='skyblue')
plt.title('Total Number of Crimes Committed Each Month in 2020')
plt.xlabel('Month')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('chart_2_TotalMonthlyCrimes.png')
plt.close()

# Helper function to generate specific crime type charts
def plot_crime_type(crime_type_str, file_name):
    counts = [len(df[df['Unified_Crime_Type'] == crime_type_str]) for df in months_dfs]
    plt.figure(figsize=(10, 6))
    plt.bar(months_labels, counts, color='skyblue')
    plt.title(f'{crime_type_str} Counts Each Month in 2020')
    plt.xlabel('Month')
    plt.ylabel(f'Number of {crime_type_str} Crimes')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(file_name)
    plt.close()

# Generate the rest of the charts using the helper function
plot_crime_type('THEFT / LARCENY', 'chart_3_Theft.png')
plot_crime_type('SEX OFFENSES', 'chart_4_SexOffenses.png')
plot_crime_type('VANDALISM & PROPERTY DAMAGE', 'chart_5_Vandalism.png')
plot_crime_type('BURGLARY', 'chart_6_Burglary.png')
plot_crime_type('DRUGS & NARCOTICS', 'chart_7_Drugs.png')
plot_crime_type('HOMICIDE', 'chart_8_Homicide.png')

print("All charts have been generated and saved as PNG files!")
print("Pipeline complete.")
