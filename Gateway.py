import sqlite3


class Gateway:

    def __init__(self):
        self.conn = sqlite3.connect('GetMeOut.sqlite3')
        self.cursor = self.conn.cursor()

    def flushTransportTable(self):
        self.cursor.execute("DELETE FROM upcoming_transport")
        self.conn.commit()
        self.cursor.execute("VACUUM")

    def saveTransportModel(self, upcomingTransportModel):
        # Insert a row of data
        self.cursor.execute("INSERT INTO upcoming_transport VALUES ("
                            + upcomingTransportModel.vehicleLabel + ", "
                            + "'" + upcomingTransportModel.arrivingTime + "', "
                            + upcomingTransportModel.routeNumber + ")"
                            )
        # Save (commit) the changes
        self.conn.commit()

        print('fuken saved')
