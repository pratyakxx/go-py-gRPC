from flask import Flask
from flask import jsonify

#gRPC Library
import grpc

#proto buffer compiler
import countries_pb2
import countries_pb2_grpc

app = Flask(__name__)

@app.route('/<countrie>')
def countrie(countrie):
    print("Start service")
    try:
      #connecting to goServer through gRPC
      channel = grpc.insecure_channel('localhost:3001')

      #initiating a stub
      stub = countries_pb2_grpc.CountryStub(channel)

      #creating a request and sending through the stub channel
      countryRequest = countries_pb2.CountryRequest(name=countrie)
      countryResponse = stub.search(countryRequest)

      #data from goServer in countryResponse
      return jsonify({
          "name": countryResponse.name,
          "alpha2Code": countryResponse.alpha2Code,
          "capital": countryResponse.capital,
          "subregion": countryResponse.subregion,
          "population": countryResponse.population,
          "nativeName": countryResponse.nativeName
      })
    except Exception as e:
      print(e)
      return e
if __name__ == '__main__':
    app.run()