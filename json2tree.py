import json

def contains_nest(indict):
    if isinstance(indict, dict):
        for key in indict:
            if isinstance(indict[key], dict) or isinstance(indict[key], list):
                return True
    return False

def json2tree(children, parent=None):
    if isinstance(children, dict):
        for child in children:
            if contains_nest(children):
                json2tree(children[child], child)
            else :
                print("nonest", child, children[child])
    elif isinstance(children, list):
        for child in children:
            print("list", child)
            try :
                json2tree(child)
            except Exception as e:
                print("list error", children, e)
    else :
        print("else", parent, children)

if __name__ == "__main__":
    json_str = """
        {
            "Title": "Example JSON",
            "Author": "AR",
            "Chapters": [
                {
                    "Title": "Chapter 1",
                    "Pages": 3
                },
                {
                    "Title": "Chapter 2",
                    "Pages": 33
                },
                {
                    "Title": "Chapter 3",
                    "Pages": 13
                }
            ],
            "Credits": "None"
        }
    """
    json2tree(json.loads(json_str))

    # else Title Example JSON
    # else Author AR
    # list {'Title': 'Chapter 1', 'Pages': 3}
    # nonest Title Chapter 1
    # nonest Pages 3
    # list {'Title': 'Chapter 2', 'Pages': 33}
    # nonest Title Chapter 2
    # nonest Pages 33
    # list {'Title': 'Chapter 3', 'Pages': 13}
    # nonest Title Chapter 3
    # nonest Pages 13
    # else Credits None
   
