from flask import Flask # request object can be used inside resource
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app) # wrap our app in an Api

device_put_args = reqparse.RequestParser()
device_put_args.add_argument("idDevice", type=int, help="The unique Device ID of device used is required", required=True)
device_put_args.add_argument("patientName", type=str, help="Name of the patient is required", required=True)
device_put_args.add_argument("date", type=str, help="Date the measurement was taken in MM/DD/YYYY format is required", required=True)
device_put_args.add_argument("time", type=str, help="Time the measurement was taken in HH:MM format is required", required=True)
device_put_args.add_argument("machineID", type=int, help="Type of equipment used is required (according to 1. Thermometer, 2.BP Monitor, 3.Oximeter, 4.Weighing Scale, 5.Glucometer, 6.Stadiometer)", required=True)
device_put_args.add_argument("measurement", type=float, help="Measurement is required", required=True)

#Update code
device_update_args = reqparse.RequestParser()
device_update_args.add_argument("idDevice", type=int, help="The unique Device ID of device used is required")
device_update_args.add_argument("patientName", type=str, help="Name of the patient is required")
device_update_args.add_argument("date", type=str, help="Date the measurement was taken in MM/DD/YYYY format is required")
device_update_args.add_argument("time", type=str, help="Time the measurement was taken in HH:MM format is required")
device_update_args.add_argument("machineID", type=int, help="Type of equipment used is required (according to 1. Thermometer, 2.BP Monitor, 3.Oximeter, 4.Weighing Scale, 5.Glucometer, 6.Stadiometer)")
device_update_args.add_argument("measurement", type=float, help="Measurement is required")

devices = {}

def abort_if_device_id_doesnt_exist(device_id):
    if device_id not in devices:
        abort(404, message="Device id is not valid...")

def abort_if_device_exists(device_id):
    if device_id in devices:
        abort(409, message="Device already exists with that ID")
#a class that is resource which has methods we can overwrite
class Device(Resource):
    def get(self, device_id):
        abort_if_device_id_doesnt_exist(device_id)
        return devices[device_id]

    def post(self, device_id):
        abort_if_device_exists(device_id)
        args = device_put_args.parse_args()
        devices[device_id] = args
        return devices[device_id], 201

    def put(self, device_id):
        args = device_update_args.parse_args()
        if device_id in devices:
            if args["idDevice"]:
                devices[device_id]["idDevice"] = args["idDevice"]
            if args["patientName"]:
                devices[device_id]["patientName"] = args["patientName"]
            if args["date"]:
                devices[device_id]["date"] = args["date"]
            if args["time"]:
                devices[device_id]["time"] = args["time"]
            if args["machineID"]:
                devices[device_id]["machineID"] = args["machineID"]
            if args["measurement"]:
                devices[device_id]["measurement"] = args["measurement"]
        return devices[device_id], 200


    def delete(self, device_id):
        abort_if_device_id_doesnt_exist(device_id)
        del devices[device_id]
        return '', 204

    
api.add_resource(Device, "/device/<int:device_id>")

    
if __name__ == "__main__":
    app.run(debug=True)
    #start our server, start our Flask application
    #In debug mode
