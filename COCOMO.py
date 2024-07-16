import os
import pandas as pd

class COCOMOCalculator:
    def __init__(self, directory, file_types=(".py", ".ipynb")):
        self.directory = directory
        self.file_types = file_types

    def count_lines_and_calculate_cost(self):
        total_lines = 0

        for root, _, files in os.walk(self.directory):
            for file in files:
                if any(file.endswith(ft) for ft in self.file_types):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        lines_of_code = len([line for line in lines if line.strip() and not line.strip().startswith("#")])
                        total_lines += lines_of_code

        return total_lines

    @staticmethod
    def cocomo(kloc, project_type="organic"):
        """
        Calcola lo sforzo di sviluppo in mesi-persona utilizzando il modello COCOMO.
        
        Parametri:
        kloc (float): Migliaia di righe di codice.
        project_type (str): Tipo di progetto. Può essere "organic", "semi-detached" o "embedded".
        
        Ritorna:
        float: Sforzo di sviluppo in mesi-persona.
        """
        # Costanti COCOMO per i vari tipi di progetti
        constants = {
            "organic": (2.4, 1.05),
            "semi-detached": (3.0, 1.12),
            "embedded": (3.6, 1.20)
        }
        
        if project_type not in constants:
            raise ValueError("Tipo di progetto non valido. Scegliere tra 'organic', 'semi-detached' o 'embedded'.")
        
        a, b = constants[project_type]
        effort = a * (kloc ** b)
        return effort

    def count_projects(self):
        # Conta il numero di cartelle (progetti) nella directory principale
        return len([name for name in os.listdir(self.directory) if os.path.isdir(os.path.join(self.directory, name))])

    def count_lines_of_code(self, directory):
        total_lines = 0
        for root, _, files in os.walk(directory):
            for file in files:
                if any(file.endswith(ft) for ft in self.file_types):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        lines_of_code = len([line for line in lines if line.strip() and not line.strip().startswith("#")])
                        total_lines += lines_of_code
            break  # Stop os.walk from going into subdirectories
        return total_lines

        
    def analyze_projects(self):
        project_data = []
        for project in os.listdir(self.directory):
            project_path = os.path.join(self.directory, project)
            if os.path.isdir(project_path):
                total_lines = self.count_lines_of_code(project_path)
                project_data.append({"Project": project, "Lines of Code": total_lines})
        df = pd.DataFrame(project_data)
        return df

    def estimate_all_projects(self,project_type):
        df = self.analyze_projects()
        df["Sforzo stimato (mesi-persona)"] = df["Lines of Code"].apply(lambda x: self.cocomo(x / 1000, project_type))
        df["Sforzo stimato (anni-persona)"] = df["Sforzo stimato (mesi-persona)"] / 12
        return df
"""
# ESEMPIO di calcolo del costo mesi-persona con il metodo COCOMO per tutti i Workflows

if __name__ == "__main__":
    directory = "C:/JupyterLab/Workflows"
    project_type = "organic"
    file_types = (".py", ".ipynb")

    calculator = COCOMOCalculator(directory, file_types)
    total_lines = calculator.count_lines_and_calculate_cost()
    kloc = total_lines / 1000
    effort = calculator.cocomo(kloc, project_type)
    num_projects = calculator.count_projects()

    print(f"Numero di progetti: {num_projects}")
    print(f"Totale linee di codice: {total_lines}")
    print(f"Sforzo di sviluppo stimato (metodo COCOMO): {int(effort)} mesi-persona, cioè {int(effort/12)} anni-persona")
"""
