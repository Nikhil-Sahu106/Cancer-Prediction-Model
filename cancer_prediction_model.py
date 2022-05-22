import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data =  {
  "Inputs": {
    "data": [
      {
        "radius_mean": 0.0,
        "texture_mean": 0.0,
        "perimeter_mean": 0.0,
        "area_mean": 0.0,
        "smoothness_mean": 0.0,
        "compactness_mean": 0.0,
        "concavity_mean": 0.0,
        "concave points_mean": 0.0,
        "symmetry_mean": 0.0,
        "fractal_dimension_mean": 0.0,
        "radius_se": 0.0,
        "texture_se": 0.0,
        "perimeter_se": 0.0,
        "area_se": 0.0,
        "smoothness_se": 0.0,
        "compactness_se": 0.0,
        "concavity_se": 0.0,
        "concave points_se": 0.0,
        "symmetry_se": 0.0,
        "fractal_dimension_se": 0.0,
        "radius_worst": 0.0,
        "texture_worst": 0.0,
        "perimeter_worst": 0.0,
        "area_worst": 0.0,
        "smoothness_worst": 0.0,
        "compactness_worst": 0.0,
        "concavity_worst": 0.0,
        "concave points_worst": 0.0,
        "symmetry_worst": 0.0,
        "fractal_dimension_worst": 0.0
      }
    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}

body = str.encode(json.dumps(data))

url = 'http://2023be7f-db65-425b-87aa-1435069602e6.centralindia.azurecontainer.io/score'
api_key = 'Uy5WOIOsxj2GEsLK6L0BjDBc51hst8yV' # Replace this with the API key for the web service

# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))