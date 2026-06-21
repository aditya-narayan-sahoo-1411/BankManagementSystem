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
    except Exception:
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

        id = alpha + num + spchar
        random.shuffle(id)

        return "".join(id)

    # ---------------- CREATE ACCOUNT ----------------

    def Createaccount(self, name, age, email, pin):

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            return {
                "success": False,
                "message": "Sorry, you cannot create your account"
            }

        Bank.data.append(info)
        Bank.__update()

        return {
            "success": True,
            "message": "Account created successfully",
            "accountNo.": info["accountNo."]
        }

    # ---------------- DEPOSIT MONEY ----------------

    def depositmoney(self, accnumber, pin, amount):

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber and i["pin"] == int(pin)
        ]

        if not userdata:
            return {
                "success": False,
                "message": "Sorry, no data found"
            }

        if amount > 10000 or amount < 0:
            return {
                "success": False,
                "message": "Deposit amount should be between 0 and 10000"
            }

        userdata[0]["balance"] += amount

        Bank.__update()

        return {
            "success": True,
            "message": "Amount deposited successfully",
            "balance": userdata[0]["balance"]
        }

    # ---------------- WITHDRAW MONEY ----------------

    def withdrawmoney(self, accnumber, pin, amount):

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber and i["pin"] == int(pin)
        ]

        if not userdata:
            return {
                "success": False,
                "message": "Sorry, no data found"
            }

        if userdata[0]["balance"] < amount:
            return {
                "success": False,
                "message": "Sorry, you don't have that much money"
            }

        userdata[0]["balance"] -= amount

        Bank.__update()

        return {
            "success": True,
            "message": "Amount withdrawn successfully",
            "balance": userdata[0]["balance"]
        }

    # ---------------- SHOW DETAILS ----------------

    def showdetails(self, accnumber, pin):

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber and i["pin"] == int(pin)
        ]

        if not userdata:
            return {
                "success": False,
                "message": "No user found"
            }

        return {
            "success": True,
            "data": userdata[0]
        }

    # ---------------- UPDATE DETAILS ----------------

    def updatedetails(self, accnumber, pin, name="", email="", newpin=""):

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber and i["pin"] == int(pin)
        ]

        if not userdata:
            return {
                "success": False,
                "message": "No such user found"
            }

        if name != "":
            userdata[0]["name"] = name

        if email != "":
            userdata[0]["email"] = email

        if newpin != "":
            if len(str(newpin)) != 4:
                return {
                    "success": False,
                    "message": "PIN must be 4 digits"
                }

            userdata[0]["pin"] = int(newpin)

        Bank.__update()

        return {
            "success": True,
            "message": "Details updated successfully"
        }

    # ---------------- DELETE ACCOUNT ----------------

    def Delete(self, accnumber, pin):

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber and i["pin"] == int(pin)
        ]

        if not userdata:
            return {
                "success": False,
                "message": "Sorry, no such data exists"
            }

        index = Bank.data.index(userdata[0])

        Bank.data.pop(index)

        Bank.__update()

        return {
            "success": True,
            "message": "Account deleted successfully"
        }