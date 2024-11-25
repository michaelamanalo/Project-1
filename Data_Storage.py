import json 


class DataStorage:
  def save(libary):
    with open ('Library.json','w') as file:
      file = json.dump(data,file, indent = 4)

  def load(library):
    with open ('Libray.json','r') as file:
      data = json.load(file)
      return (data)
