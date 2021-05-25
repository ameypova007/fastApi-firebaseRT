from models import InputData

def result(data : InputData):
    print(type(data.id))
    return ({"id":data.id,"name":data.name,"skills":data.skills})