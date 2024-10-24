from crewai import Agent, Task, Crew, Process
from crewai.flow.flow import Flow, listen, start
import os
import json
from datetime import datetime
import dotenv
import asyncio
from Crew.crew import crew
from Sheets_Conn.quick_start import collect_and_save_data, insert_data_into_first_empty_row
# Load environment variables
dotenv.load_dotenv()

class Flow(Flow):

    @start()
    def update_data(self):
        collect_and_save_data()
        return "Dados corretamente atualizados!"

    @listen(update_data)
    def filter_data(self):
        with open('Data/data.json', 'r') as json_file:
            data = json.load(json_file)
        
        today = datetime.now().strftime("%d/%m/%Y")
        filtered_data = [entry for entry in data if entry["Date_Time"].startswith(today)]
        # Save the filtered data to a new JSON file
        with open('Data/filtered_data.json', 'w') as json_file:
            json.dump(filtered_data, json_file, indent=4)

        return 
    
    @listen(filter_data)
    def analyze_data(self):
        crew_output = crew.kickoff()
        return crew_output
    
    @listen(analyze_data)
    def send_summary(self, crew_output):
        insert_data_into_first_empty_row([datetime.now().strftime("%d/%m/%Y %H:%M"), str(crew_output)])
        return crew_output


def main():
    flow = Flow()
    asyncio.run(flow.kickoff())
    return "Resumo enviado com sucesso!"


if __name__ == "__main__":
    main()




