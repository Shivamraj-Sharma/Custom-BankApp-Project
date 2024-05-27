from Util.DBconnection import DBConnection

class CommonServices(DBConnection):
    def authenticate(self, LoginID, Password):
        self.cursor.execute("SELECT * FROM LoginCredentials WHERE LoginID = ?", (LoginID),)
        credentials = self.cursor.fetchall()
        if len(credentials) == 0:
            return False
        else:
            password = credentials[2]
            if password == Password:
                return True
        return False

    def check_role(self, LoginID):
        self.cursor.execute("SELECT * FROM LoginCredentials WHERE LoginID = ?", (LoginID),)
        credentials = self.cursor.fetchall()
        role = credentials[3]
        if role == "Admin":
            return "A"
        UserID = str(credentials[1])
        return UserID