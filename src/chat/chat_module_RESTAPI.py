from flask import Flask # request object can be used inside resource
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app) # wrap our app in an Api
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
#Only do the below command once, we do not want to reinitialize it over and over again

class ChatModel(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(100), nullable=False)
    sender_id = db.Column(db.Integer, nullable=False)
    reciever_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(500), nullable=False)
    attachment_video_url = db.Column(db.String(500), nullable=True)
    attachment_audio_url = db.Column(db.String(500), nullable=True)
    attachment_image_url = db.Column(db.String(500), nullable=True)
    attachment_file_url = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"Chat(time stamp = {timestamp}, sender id = {sender_id}, reciever_id = {reciever_id}, text = {text}, attachement of video url = {attachment_video_url}, attachement of audio url = {attachment_audio_url}, attachement of image url = {attachment_image_url}, attachement of file url = {attachment_file_url})"

#db.create_all()


chat_put_args = reqparse.RequestParser()
chat_put_args.add_argument("timestamp", type=str, help="Timestamp of the chat is required", required=True)
chat_put_args.add_argument("sender_id", type=int, help="Sender ID of the chat is required", required=True)
chat_put_args.add_argument("reciever_id", type=int, help="Reciever ID of the chat is required", required=True)
chat_put_args.add_argument("text", type=str, help="Text message is required", required=True)
chat_put_args.add_argument("attachment_video_url", type=str, help="Not required", required=False)
chat_put_args.add_argument("attachment_audio_url", type=str, help="Not required", required=False)
chat_put_args.add_argument("attachment_image_url", type=str, help="Not required", required=False)
chat_put_args.add_argument("attachment_file_url", type=str, help="Not required", required=False)

#Update code
chat_update_args = reqparse.RequestParser()
chat_update_args.add_argument("timestamp", type=str, help="Timestamp of the chat is required", required=True)
chat_update_args.add_argument("sender_id", type=int, help="Sender ID of the chat is required", required=True)
chat_update_args.add_argument("reciever_id", type=int, help="Reciever ID of the chat is required", required=True)
chat_update_args.add_argument("text", type=str, help="Text message is required", required=True)
chat_update_args.add_argument("attachment_video_url", type=str, help="Not required", required=False)
chat_update_args.add_argument("attachment_audio_url", type=str, help="Not required", required=False)
chat_update_args.add_argument("attachment_image_url", type=str, help="Not required", required=False)
chat_update_args.add_argument("attachment_file_url", type=str, help="Not required", required=False)


resource_fields = {
    'chat_id': fields.Integer,
    'timestamp': fields.String,
    'sender_id': fields.Integer,
    'reciever_id': fields.Integer,
    'text': fields.String,
    'attachment_video_url': fields.String,
    'attachment_audio_url': fields.String,
    'attachment_image_url': fields.String,
    'attachment_file_url': fields.String,
}

#a class that is resource which has methods we can overwrite
class Chat(Resource):
    @marshal_with(resource_fields)
    def get(self, chatID):
        result = ChatModel.query.filter_by(chat_id=chatID).first()
        if not result:
            abort(404, message="Could not find chat with that id")
        return result
    @marshal_with(resource_fields)
    def post(self, chatID):
        args = chat_put_args.parse_args()
        result = ChatModel.query.filter_by(chat_id=chatID).first()
        if result:
            abort(409, message="Chat Id taken...")
        chat = ChatModel(chat_id=chatID, timestamp=args['timestamp'], sender_id=args['sender_id'], reciever_id=args['reciever_id'], text=args['text'], attachment_video_url=args['attachment_video_url'], attachment_audio_url=args['attachment_audio_url'], attachment_image_url=args['attachment_image_url'], attachment_file_url=args['attachment_file_url'])
        db.session.add(chat)
        db.session.commit()
        return chat, 201

    @marshal_with(resource_fields)
    def put(self, chatID):
        args = chat_update_args.parse_args()
        result = ChatModel.query.filter_by(chat_id=chatID).first()
        if not result:
            abort(404, message="Chat doesn't exist, cannot update")
        if args['timestamp']:
            result.timestamp = args['timestamp']
        if args['sender_id']:
            result.sender_id = args['sender_id']
        if args['reciever_id']:
            result.reciever_id = args['reciever_id']
        if args['text']:
            result.text = args['text']
        if args['attachment_video_url']:
            result.attachment_video_url = args['attachment_video_url']
        if args['attachment_audio_url']:
            result.attachment_audio_url = args['attachment_audio_url']
        if args['attachment_image_url']:
            result.attachment_image_url = args['attachment_image_url']
        if args['attachment_file_url']:
            result.attachment_file_url = args['attachment_file_url']

        db.session.commit()
        return result

    def delete(self, chatID):
        result = ChatModel.query.filter_by(chat_id=chatID).first()
        if not result:
            abort(404, message="Could not find device with that id")
        db.session.delete(result)
        db.session.commit()
        return '', 204


api.add_resource(Chat, "/chat/<int:chatID>")


if __name__ == "__main__":
    app.run(debug=True)
    #start our server, start our Flask application
    #In debug mode
