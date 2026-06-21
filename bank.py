
import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []

    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                data = json.load(fs)
        else:
            data = []
    except:
        data = []

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            json.dump(Bank.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)

        acc = alpha + num + spchar
        random.shuffle(acc)

        return "".join(acc)

    def Createaccount(self, name, age, email, pin):

        if age < 18:
            return {
                "success": False,
                "message": "Age must be at least 18"
            }

        if len(str(pin)) != 4:
            return {
                "success": False,
                "message": "PIN must contain 4 digits"
            }

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0
        }

        Bank.data.append(info)
        Bank.__update()

        return {
            "success": True,
            "message": "Account created successfully",
            "accountNo.": info["accountNo."]
        }

    def depositmoney(self, accnumber, pin, amount):

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber and i["pin"] == int(pin)
        ]

        if not userdata:
            return {"success": False, "message": "No user found"}

        userdata[0]["balance"] += amount

        Bank.__update()

        return {
            "success": True,
            "message": "Money deposited successfully",
            "balance": userdata[0]["balance"]
        }

    def withdrawmoney(self, accnumber, pin, amount):

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber and i["pin"] == int(pin)
        ]

        if not userdata:
            return {"success": False, "message": "No user found"}

        if userdata[0]["balance"] < amount:
            return {
                "success": False,
                "message": "Insufficient balance"
            }

        userdata[0]["balance"] -= amount

        Bank.__update()

        return {
            "success": True,
            "message": "Money withdrawn successfully",
            "balance": userdata[0]["balance"]
        }

    def showdetails(self, accnumber, pin):

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber and i["pin"] == int(pin)
        ]

        if not userdata:
            return {
                "success": False,
                "message": "User not found"
            }

        return {
            "success": True,
            "data": userdata[0]
        }

    def updatedetails(self, accnumber, pin, name="", email="", newpin=""):

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber and i["pin"] == int(pin)
        ]

        if not userdata:
            return {"success": False, "message": "User not found"}

        if name:
            userdata[0]["name"] = name

        if email:
            userdata[0]["email"] = email

        if newpin:
            userdata[0]["pin"] = int(newpin)

        Bank.__update()

        return {
            "success": True,
            "message": "Details updated successfully"
        }

    def Delete(self, accnumber, pin):

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber and i["pin"] == int(pin)
        ]

        if not userdata:
            return {
                "success": False,
                "message": "User not found"
            }

        Bank.data.remove(userdata[0])

        Bank.__update()

        return {
            "success": True,
            "message": "Account deleted successfully"
        }

