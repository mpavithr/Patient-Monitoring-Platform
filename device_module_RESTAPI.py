from flask import Flask # request object can be used inside resource
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app) # wrap our app in an Api
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
#Only do the below command once, we do not want to reinitialize it over and over again

class DeviceModel(db.Model):
    device_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    firmware_version = db.Column(db.Float, nullable=False)
    date_of_purchase = db.Column(db.String(200), nullable=False)
    serial_number = db.Column(db.Integer, nullable=False)
    mac_address = db.Column(db.String(100), nullable=True)
    machineID = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Device(name = {name}, firmware version = {firmware_version}, date of purchase = {date_of_purchase}, serial number = {serial_number}, MAC address = {mac_address}, machine ID = {machineID})"

class PatientDataModel(db.Model):
    measurement_id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, nullable=False)
    patient_id = db.Column(db.Integer, nullable=False)
    assigner_id = db.Column(db.Integer, nullable=False)
    machineID = db.Column(db.Integer, nullable=False)
    date_assigned = db.Column(db.String(200), nullable=False)
    date_returned = db.Column(db.String(200), nullable=False)
    measurement = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Device(device id = {device_id}, patient_id = {patient_id}, assigner_id = {assigner_id}, machineID = {machineID}, date assigned = {date_assigned}, date returned = {date_returned}, measurement = {measurement})"

#db.create_all()


device_put_args = reqparse.RequestParser()
device_put_args.add_argument("name", type=str, help="Name of the device is required", required=True)
device_put_args.add_argument("firmware_version", type=float, help="firmware version is required", required=True)
device_put_args.add_argument("date_of_purchase", type=str, help="date and time the device was purchased", required=True)
device_put_args.add_argument("serial_number", type=int, help="serial number is required", required=True)
device_put_args.add_argument("mac_address", type=str, help="MAC Address is required", required=False)
device_put_args.add_argument("machineID", type=int, help="Machine ID is required", required=True)
#Update code
device_update_args = reqparse.RequestParser()
device_update_args.add_argument("name", type=str, help="Name of the device is required")
device_update_args.add_argument("firmware_version", type=float, help="firmware version is required")
device_update_args.add_argument("date_of_purchase", type=str, help="date and time the device was purchased")
device_update_args.add_argument("serial_number", type=int, help="serial number is required")
device_update_args.add_argument("mac_address", type=str, help="MAC Address is required")
device_update_args.add_argument("machineID", type=int, help="Machine ID is required")

patient_data_put_args = reqparse.RequestParser()
patient_data_put_args.add_argument("device_id", type=int, help="ID of the device is required", required=True)
patient_data_put_args.add_argument("patient_id", type=int, help="User ID of the patient is required", required=True)
patient_data_put_args.add_argument("assigner_id", type=int, help="User ID of the assigner is required", required=True)
patient_data_put_args.add_argument("machineID", type=int, help="Machine ID of the assigner is required", required=True)
patient_data_put_args.add_argument("date_assigned", type=str, help="date assigned is required", required=True)
patient_data_put_args.add_argument("date_returned", type=str, help="date returned is required", required=False)
patient_data_put_args.add_argument("measurement", type=float, help="Measurement is required", required=True)
#Update code
patient_data_update_args = reqparse.RequestParser()
patient_data_update_args.add_argument("device_id", type=int, help="ID of the device is required")
patient_data_update_args.add_argument("patient_id", type=int, help="User ID of the patient is required")
patient_data_update_args.add_argument("assigner_id", type=int, help="User ID of the assigner is required")
patient_data_update_args.add_argument("machineID", type=int, help="Machine ID of the assigner is required")
patient_data_update_args.add_argument("date_assigned", type=str, help="date assigned is required")
patient_data_update_args.add_argument("date_returned", type=str, help="date returned is required")
patient_data_update_args.add_argument("measurement", type=float, help="Measurement is required")

resource_fields = {
    'device_id': fields.Integer,
    'name': fields.String,
    'firmware_version': fields.Float,
    'date_of_purchase': fields.String,
    'serial_number': fields.Integer,
    'mac_address': fields.String,
    'machineID': fields.Integer
}

resource_fields2 = {
    'measurement_id': fields.Integer,
    'device_id': fields.Integer,
    'patient_id': fields.Integer,
    'assigner_id': fields.Integer,
    'machineID': fields.Integer,
    'date_assigned': fields.String,
    'date_returned': fields.String,
    'measurement': fields.Float
}

#a class that is resource which has methods we can overwrite
class Device(Resource):
    @marshal_with(resource_fields)
    def get(self, deviceID):
        result = DeviceModel.query.filter_by(device_id=deviceID).first()
        if not result:
            abort(404, message="Could not find device with that id")
        return result
    @marshal_with(resource_fields)
    def post(self, deviceID):
        args = device_put_args.parse_args()
        result = DeviceModel.query.filter_by(device_id=deviceID).first()
        if result:
            abort(409, message="Device Id taken...")
        device = DeviceModel(device_id=deviceID, name=args['name'], firmware_version=args['firmware_version'], date_of_purchase=args['date_of_purchase'], serial_number=args['serial_number'], mac_address=args['mac_address'], machineID=args['machineID'])
        db.session.add(device)
        db.session.commit()
        return device, 201

    @marshal_with(resource_fields)
    def put(self, deviceID):
        args = device_update_args.parse_args()
        result = DeviceModel.query.filter_by(device_id=deviceID).first()
        if not result:
            abort(404, message="Device doesn't exist, cannot update")
        if args['name']:
            result.name = args['name']
        if args['firmware_version']:
            result.firmware_version = args['firmware_version']
        if args['date_of_purchase']:
            result.date_of_purchase = args['date_of_purchase']
        if args['serial_number']:
            result.serial_number = args['serial_number']
        if args['mac_address']:
            result.mac_address = args['mac_address']
        if args['machineID']:
            result.machineID = args['machineID']

        db.session.commit()
        return result

    def delete(self, deviceID):
        result = DeviceModel.query.filter_by(device_id=deviceID).first()
        if not result:
            abort(404, message="Could not find device with that id")
        db.session.delete(result)
        db.session.commit()
        return '', 204

class Measurement(Resource):
    @marshal_with(resource_fields2)
    def get(self, measurementID):
        result = PatientDataModel.query.filter_by(measurement_id=measurementID).first()
        if not result:
            abort(404, message="Could not find any measurement data with that ID")
        return result

    @marshal_with(resource_fields2)
    def post(self, measurementID):
        args = patient_data_put_args.parse_args()
        result = PatientDataModel.query.filter_by(measurement_id=measurementID).first()
        if result:
            abort(409, message="Measurement Id taken...")
        patient_data = PatientDataModel(measurement_id = measurementID, device_id=args['device_id'], patient_id=args['patient_id'], assigner_id=args['assigner_id'], machineID=args['machineID'], date_assigned=args['date_assigned'], date_returned=args['date_returned'], measurement=args['measurement'])
        db.session.add(patient_data)
        db.session.commit()
        return patient_data, 201

    @marshal_with(resource_fields2)
    def put(self, measurementID):
        args = patient_data_update_args.parse_args()
        result = PatientDataModel.query.filter_by(measurement_id=measurementID).first()
        if not result:
            abort(404, message="Measurement data for that particular ID doesn't exist")
        if args['device_id']:
            result.device_id = args['device_id']
        if args['patient_id']:
            result.patient_id = args['patient_id']
        if args['assigner_id']:
            result.assigner_id = args['assigner_id']
        if args['machineID']:
            result.machineID = args['machineID']
        if args['date_assigned']:
            result.date_assigned = args['date_assigned']
        if args['date_returned']:
            result.date_returned = args['date_returned']
        if args['measurement']:
            result.measurement = args['measurement']

        db.session.commit()
        return result

    def delete(self, measurementID):
        result = PatientDataModel.query.filter_by(measurement_id=measurementID).first()
        if not result:
            abort(404, message="Could not find measurement with that id")
        db.session.delete(result)
        db.session.commit()
        return '', 204

    
api.add_resource(Device, "/device/<int:deviceID>")
api.add_resource(Measurement, "/measurement/<int:measurementID>")


if __name__ == "__main__":
    app.run(debug=True)
    #start our server, start our Flask application
    #In debug mode
