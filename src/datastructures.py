
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []


    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 9999)

    def add_member(self, member):
        if "id" not in member:
            member ["id"]=self._generateId()

       
        self._members.append({
            "id": member["id"],
            "first_name": member["first_name"],
            "age": member ["age"],
            "lucky_numbers": member["lucky_numbers"]
            }
        )

    def delete_member(self, id):
        for member in self._members:
            if member["id"]==id:
                self._members.remove(member)
                return ({"done": True})
        return ({"done": False})   

        # fill this method and update the return


    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member ["id"] == int(id):
                return member
        return ({"message":"member do not exist"})    
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
