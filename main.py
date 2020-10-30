from classification import CanClass
from nearby_places import GetNearbyHospitals
from remedy_sugg import RemedySugg

can_model = CanClass()

print("For Proof-Of-Concept Purposes")
print("")
print("")

ben_pred = can_model.predict_class()
print("Actual Class : Non-Melanomic Cancer")
print("Predicted Class :", ben_pred)
print("")

mal_pred = can_model.predict_class()
print("Actual Class : Melanomic Cancer")
print("Predicted Class :", mal_pred)
print("")

non_canc_pred = can_model.predict_class()
print("Actual Class : Non-Cancerous")
print("Predicted Class :", non_canc_pred)
print("")

non_canc_pred_real = can_model.predict_class()
print("Actual Class : Non-Cancerous")
print("Predicted Class :", non_canc_pred_real)
print("")


nearby_hosp = GetNearbyHospitals(13.016327, 77.548578)
nearby_hosp.get_hospital_one()
nearby_hosp.get_hospital_two()
nearby_hosp.get_hospital_three()
nearby_hosp.get_hospital_four()
nearby_hosp.get_hospital_five()

print("")

print("For Proof-Of-Concept Purposes, We Will Open The Website For Test Image 4")
sugg = RemedySugg()
sugg.suggest_remedy(non_canc_pred_real)

