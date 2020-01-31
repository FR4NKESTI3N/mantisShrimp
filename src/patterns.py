# From theheadofabroom's answer : https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
def singleton(type_):
    instances = {}
    def getInstance(*args, **kwargs):
        if type_ not in instances:
            instances[type_] = type_(*args, **kwargs)
        return instances[type_]
    return getInstance
