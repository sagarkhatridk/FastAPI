

def noteEntity(item) -> dict:
    print(item)
    return {
        "id": str(item["_id"]),
        "title":item['title'],
        "desc":item['desc'],
        "important":item['important'] | False
    }

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]