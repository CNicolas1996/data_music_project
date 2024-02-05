import json

class JSONSerializer:

    @staticmethod
    def to_json(obj):
        def default(obj):
            if hasattr(obj, '__dict__'):
                return obj.__dict__
            return obj

        return json.dumps(obj, default=default, indent=4)
