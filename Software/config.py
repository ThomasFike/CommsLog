import json
from pathlib import Path


class Config():
    path = "./config.json"

    def __init__(self):
        if (Path(self.path).exists()):
            pass
        else:
            self.createConfigFile()
        with open(Path(self.path)) as json_data_file:
            self.configData = json.load(json_data_file)
        self.database = self.configData['database']
        self.RxStation = self.configData['RxStation']

    def createConfigFile(self):
        f = open(Path(self.path), "w")
        f.write(
            "{\n    \"database\": \"./Database.json\",\n    \"RxStation\": \"Net Control\"\n}")
        f.close()

    def update(self):
        self.configData['database'] = self.database
        self.configData['RxStation'] = self.RxStation
        with open(Path(self.path), 'w') as outfile:
            json.dump(self.configData, outfile, indent=4)

    def configure(self):
        print("Weclome to the configurator!")
        print(f"Database: {self.database}")
        if input("Would you like to change the database [Y/n]? ").lower() == 'y':
            self.database = input("New Database Path: ")
        print(f"Rx Station: {self.RxStation}")
        if input("Would you like to change the Rx Station [Y/n]? ").lower() == 'y':
            self.RxStation = input("New Rx Station: ")
        if input("Do you want to update your config file [Y/n]? ").lower() == 'y':
            self.update()
        print("Configuration Complete!")
