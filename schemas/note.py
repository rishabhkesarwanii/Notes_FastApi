"""
Schema for notes
"""
def noteEntity(item) -> dict:
    """
    This will take a single item and change mongoose object to a dict format
    """
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "desc":item["desc"],
        "important":item["important"]
    }

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]