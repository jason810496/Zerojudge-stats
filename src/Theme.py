
class Theme:
    THEME_DIC = {}

    @classmethod
    def Init(self):
        import json

        with open("Theme.json") as Json_file:
            self.THEME_DIC = json.load(Json_file)

    # add theme method

    #delete theme method
