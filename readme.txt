Work Description


1. Hi This is a api to montior old persons heart rate per 60 minute and share a response.
2. This api contains a code which will take user registration data as json format and upload to a database ( database server is in build).
3. The data (heart rate BPM) will be taken from a physical device per 60 min on a 10 sec interval ( check data.py for the example data generation and check any test_data.json for the fomat )
4. Now the collected data will be shared through a algorithm which will have 3 conditions
    1.Green Zone: Normal Heart Rate
        Description: Heart rate within the normal range.
        Average BPM Range: Typically around 60-100 BPM.
    2.Blue Zone: Resting Heart Rate
        Description: Heart rate while at rest or during periods of relaxation.
        Average BPM Range: Generally below 60 BPM.
    3.Red Zone: Elevated Heart Rate
        Description: Heart rate above the normal range, indicating increased activity or exertion.
        Average BPM Range: Typically above 100 BPM.

    this part of the api is under build

5. The final collected data per 24 hours will be formatted in json and send to the family members or concerned persons mail ID 


