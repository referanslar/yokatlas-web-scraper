from scraper.bachelor import Bachelor
import json, os

class App(Bachelor):
    def __init__(self) -> None:
        pass

    def get_bachelor_programs(self):
        if not os.path.exists("./data"):
            print("🔴 Not Found: data folder")
            print("🟠 Generating: data folder")
            os.makedirs("./data")
            print("🟢 Generated: data folder")
        else:
            print("🟢 Found: data folder")

        if not os.path.exists("./data/universities.json"):
            print("🔴 Not Found: universities.json")
            print("🟠 Generating: universities.json")
            
            universities = self.get_universities()
            with open("./data/universities.json", "w") as f:
                json.dump(universities, f, indent=4, ensure_ascii=False)

            print("🟢 Generated: universities.json")
        else:
            print("🟢 Found: universities.json")
    
        if not os.path.exists("./data/degree_ids.json"):
            print("🔴 Not Found: degree_ids.json")
            print("🟠 Generating: degree_ids.json")
            
            universities = [] 

            with open("./data/universities.json", "r") as f:
                universities = json.load(f)

            degree_ids = []

            for university in universities:
                degrees = self.get_degrees_by_university(university[1])

                for degree in degrees:
                    degree_ids.append(degree[1])

                print(f"🟣 Completed: {university[0]}")

            with open("./data/degree_ids.json", "w") as f:
                json.dump(degree_ids, f, indent=4, ensure_ascii=False)

            print("🟢 Generated: degree_ids.json")
        else:
            print("🟢 Found: degree_ids.json")

        if not os.path.exists("./data/degrees.json"):
            print("🔴 Not Found: degrees.json")
            print("🟠 Generating: degrees.json")
            
            degree_ids = []

            with open("./data/degree_ids.json", "r") as f:
                degree_ids = json.load(f)

            degrees = []

            for degree_id in degree_ids:
                degree_info = self.get_degree_info(degree_id)
                degrees.append(degree_info)

                print(f"🟣 Completed: {degree_info['osymprogramkodu']} - {degree_info['universite']} - {degree_info['program_title']}")

            with open("./data/degrees.json", "w") as f:
                json.dump(degrees, f, indent=4, ensure_ascii=False)

            print("🟢 Generated: degrees.json")
        else:
            print("🟢 Found: degrees.json")

        print()
        input("👋🏻 Bye! Press any key to exit...")
