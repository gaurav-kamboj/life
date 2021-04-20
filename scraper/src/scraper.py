from collections import namedtuple
import requests
import os
import json
from state_data import state_data

STATES = [state["state"] for state in state_data["states"]]

District = namedtuple("District", ["name", "state"])
API_KEY = os.environ["AIRTABLE_API_KEY"]

headers = {"Authorization": f"Bearer {API_KEY}"}


def get_records(url: str) -> list:
    records = []
    offset = ""
    while True:
        response = requests.get(url, headers=headers, params=[("offset", offset)])
        records.extend(response.json()["records"])
        if "offset" in response.json():
            offset = response.json()["offset"]
        else:
            break
    return records


def get_district_data():
    records = get_records("https://api.airtable.com/v0/appIVYBhHiWvtSV1h/Districts")
    districts = {}
    for district in records:
        districts[district["id"]] = District(district["fields"]["Name"], district["fields"]["Name (from State)"][0])
    return districts


def get_states_data():
    records = get_records("https://api.airtable.com/v0/appIVYBhHiWvtSV1h/State")
    states = {}
    for state in records:
        states[state["fields"]["Name"]] = [districts[district].name for district in state["fields"]["Districts"]]
    return states


def dump_data(filename: str, data: dict):
    with open(f"data/{filename}", "w") as states_json:
        states_json.write(json.dumps(data, indent=4, sort_keys=True))


districts = get_district_data()


def sanitize_state(state: str) -> str:
    for internal_state in STATES:
        if state.lower().strip() in internal_state.lower():
            return internal_state
    return None


def get_oxygen_data():
    url = "https://api.airtable.com/v0/appIVYBhHiWvtSV1h/Oxygen"
    oxygen_data = {"data": []}
    raw_data = get_records(url)
    for record in raw_data:
        try:
            district = districts[record["fields"]["Districts"][0]]
        except Exception:
            continue
        oxygen_data["data"].append(
            {
                "id": record["id"],
                "state": district.state,
                "district": district.name,
                "city": record["fields"].get("District"),
                "name": record["fields"].get("Person name"),
                "description": record["fields"].get("Description"),
                "phone1": record["fields"].get("Phone 1"),
                "phone2": record["fields"].get("Phone 2"),
                "sourceLink": record["fields"].get("Source link"),
                "createdTime": record["createdTime"],
                "sourceBame": record["fields"].get("Source Name"),
                "companyName": record["fields"].get("Company name"),
                "verifiedStatus": record["fields"].get("Verified status").strip()
                if "Verified status" in record["fields"]
                else None,
                "comments": record["fields"].get("Comments"),
            }
        )
    return oxygen_data


def get_plasma_data():
    url = "https://api.airtable.com/v0/appIVYBhHiWvtSV1h/Plasma"
    plasma_data = {"data": []}
    raw_data = get_records(url)
    for record in raw_data:
        try:
            district = districts[record["fields"]["Districts"][0]]
        except Exception:
            continue
        plasma_data["data"].append(
            {
                "id": record["id"],
                "state": district.state,
                "district": district.name,
                "city": record["fields"].get("City"),
                "name": record["fields"].get("Name"),
                "description": record["fields"].get("Description"),
                "phone1": record["fields"].get("Phone 1"),
                "sourceLink": record["fields"].get("Source link"),
                "createdTime": record["createdTime"],
            }
        )
    return plasma_data


def get_hospital_bed_icu():
    url = "https://api.airtable.com/v0/appIVYBhHiWvtSV1h/Hospitals%2C%20Bed%2C%20ICU"
    hospital_bed_icu = {"data": []}
    raw_data = get_records(url)
    for record in raw_data:
        try:
            district = districts[record["fields"]["Districts"][0]]
        except Exception:
            continue
        hospital_bed_icu["data"].append(
            {
                "id": record["id"],
                "name": record["fields"].get("Name"),
                "state": district.state,
                "district": district.name,
                "pointOfContact": record["fields"].get("pointOfContact"),
                "phone1": record["fields"].get("phone1"),
                "phone2": record["fields"].get("phone2"),
                "sourceUrl": record["fields"].get("sourceUrl"),
                "source": record["fields"].get("source"),
                "verificationStatus": record["fields"].get("Verification Status"),
                "verifiedBy": record["fields"].get("Verified by"),
                "verifiedBy2": record["fields"].get("Verified By 2"),
                "createdTime": record["createdTime"],
            }
        )
    return hospital_bed_icu


def get_helpline_data():
    url = "https://api.airtable.com/v0/appIVYBhHiWvtSV1h/Helpline"
    helpline_data = {"data": []}
    raw_data = get_records(url)
    for record in raw_data:
        try:
            district = districts[record["fields"]["Districts"][0]]
        except Exception:
            continue
        helpline_data["data"].append(
            {
                "id": record["id"],
                "name": record["fields"].get("Name"),
                "category": record["fields"].get("category"),
                "subCategory": record["fields"].get("subCategory"),
                "state": district.state,
                "district": district.name,
                "phone1": record["fields"].get("phone1"),
                "phone2": record["fields"].get("phone2"),
                "sourceUrl": record["fields"].get("sourceUrl"),
                "source": record["fields"].get("source"),
                "description": record["fields"].get("description"),
                "zonalVerificationStatus": record["fields"].get("Zonal Verification Status"),
                "verifiedBy": record["fields"].get("Verified by"),
                "createdTime": record["createdTime"],
            }
        )
    return helpline_data


def get_medicine_data():
    url = "https://api.airtable.com/v0/appIVYBhHiWvtSV1h/Medicine%2C%20Injection"
    medicine_data = {"data": []}
    raw_data = get_records(url)
    for record in raw_data:
        try:
            district = districts[record["fields"]["Districts"][0]]
        except Exception:
            continue
        medicine_data["data"].append(
            {
                "id": record["id"],
                "name": record["fields"].get("Name"),
                "city": record["fields"].get("City"),
                "description": record["fields"].get("Description"),
                "distributorName": record["fields"].get("Distributor Name"),
                "address": record["fields"].get("Address"),
                "emailId": record["fields"].get("Email ID"),
                "state": district.state,
                "district": district.name,
                "phone1": record["fields"].get("Phone 1"),
                "Verified": record["fields"].get("Verified"),
                "commentsLatestupdate": record["fields"].get("Comments/Latest update"),
                "source": record["fields"].get("Source"),
                "contactName": record["fields"].get("Contact name"),
                "updateDateAndTime": record["fields"].get("Update date & time"),
                "verifiedBy": record["fields"].get("Verified by"),
                "createdTime": record["createdTime"],
            }
        )
    return medicine_data


def get_ambulance_data():
    url = "https://api.airtable.com/v0/appIVYBhHiWvtSV1h/Medicine%2C%20Injection"
    ambulance_data = {"data": []}
    raw_data = get_records(url)
    for record in raw_data:
        try:
            district = districts[record["fields"]["Districts"][0]]
        except Exception:
            continue
        ambulance_data["data"].append(
            {
                "id": record["id"],
                "name": record["fields"].get("Name"),
                "area": record["fields"].get("Area"),
                "state": district.state,
                "district": district.name,
                "phone1": record["fields"].get("Phone 1"),
                "phone2": record["fields"].get("Phone 2"),
                "source": record["fields"].get("Source"),
                "createdTime": record["createdTime"],
            }
        )
    return ambulance_data


hospital_data = get_hospital_bed_icu()
dump_data("hospital_bed_icu.json", hospital_data)
oxygen_data = get_oxygen_data()
dump_data("oxygen.json", oxygen_data)
plasmadata = get_plasma_data()
dump_data("plasma.json", plasmadata)
helpline_data = get_helpline_data()
dump_data("helpline.json", helpline_data)
medicine_data = get_medicine_data()
dump_data("medicine.json", medicine_data)
ambulance_data = get_ambulance_data()
dump_data("ambulance.json", ambulance_data)
