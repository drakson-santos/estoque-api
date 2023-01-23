import uuid

class UniqueId:

    @classmethod
    def get_unique_id(cls, type="uuid"):
        if type == "uuid":
            return str(uuid.uuid4())
