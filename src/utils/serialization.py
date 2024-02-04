import json


class JSONSerializable:

    def to_json(self):
        return json.dumps(self, indent=4)
