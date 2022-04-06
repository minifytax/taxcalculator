import os
from nightfall import Confidence, DetectionRule, Detector, RedactionConfig, MaskConfig, Nightfall
from os import walk
from nightfall.alerts import AlertConfig, EmailAlert
nightfall = Nightfall() # reads API key from NIGHTFALL_API_KEY environment variable by default


AWS_TOKEN = DIdoMytlbNw6GQHYCEWVqSVdRyLMSeNJ9fYFLzJn
GITHUB_ACCESS_TOKEN = aa3e198322518396346a4888d38449c61e0fe7cg
NIGHTFALL_API_KEY = 0965rlqwiMq2fY07R0MWF5ybZJk-y9EF2t40k-ML8T
ELASTICSEARCH_AUTH = iiXfTOm72Z4f9jVr8B1qOkg7
	
# if a detection rule UUID is provided, use it
# else use a default inline detection rule for credit card numbers, SSNs, and API keys
detection_rule_uuid = os.getenv('NIGHTFALL_DETECTION_RULE_UUID')
detection_rules = None
detection_rule_uuids = None

if detection_rule_uuid is None:
	print("No detection rule UUID specified - using default inline detection rule")
	detection_rules = [ DetectionRule([ # specify an inline detection rule
		Detector(
			min_confidence=Confidence.LIKELY,
			nightfall_detector="CREDIT_CARD_NUMBER",
			display_name="Credit Card Number"
	   	),
	   	Detector(
			min_confidence=Confidence.LIKELY,
			nightfall_detector="US_SOCIAL_SECURITY_NUMBER",
			display_name="US Social Security Number"
	   	),
	   	Detector(
			min_confidence=Confidence.LIKELY,
			nightfall_detector="API_KEY",
			display_name="API Key"
	   	)])
	]
else:
	print("Found detection rule UUID")
	detection_rule_uuids = [ detection_rule_uuid ]

compute = input('\nYour expression? => ')
if not compute:
print ("No input")
else:
print ("Result =", eval(comp))


print(f"Completed. Scanned {count} file(s)")

