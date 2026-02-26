import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io
import base64

def generate_histogram(df, column):
    """Generate a histogram for `column` and return base64 PNG bytes string."""
    plt.close('all')
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df[column].dropna(), bins=30, color='steelblue')
    ax.set_title(f'Histogram of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=120)
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')
class TitanicAgent:
    def __init__(self, data):
        self.data = data

    def process_query(self, query, api_key=None):
        # Process the user's query and return a dict with text/image
        query = query.lower()
        response = {"answer": "", "image": None}

        import re
        if "surviv" in query or "alive" in query or "die" in query:
            response["answer"] = self.get_survival_rate()
        elif "histogram" in query and re.search(r'\bage(s)?\b', query):
            response["image"] = generate_histogram(self.data, 'Age')
            response["answer"] = "Here is the histogram of passenger ages."
        elif re.search(r'\b(average|mean)\s+age(s)?\b', query):
            response["answer"] = self.get_average_age()
        elif "class" in query or "distribut" in query:
            response["answer"] = self.get_class_distribution()
        elif "male" in query or "female" in query or "gender" in query or "sex" in query:
            response["answer"] = self.get_gender_percentage()
        elif "fare" in query or "ticket" in query or "cost" in query or "price" in query:
            response["answer"] = self.get_average_fare()
        elif "embark" in query or "port" in query:
            response["answer"] = self.get_embarkation_counts()
        else:
            try:
                from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
                from langchain_groq import ChatGroq
                import os
                
                # Using the ChatGroq client
                llm = ChatGroq(
                    temperature=0, 
                    api_key=os.environ.get("GROQ_API_KEY", ""), 
                    model="llama-3.3-70b-versatile"
                )
                
                agent = create_pandas_dataframe_agent(llm, self.data, verbose=True, allow_dangerous_code=True)
                response["answer"] = agent.run(query)
            except Exception as e:
                response["answer"] = f"Failed to query LLM: {str(e)}"
            
        return response

    def get_survival_rate(self):
        survived_count = self.data[self.data['Survived'] == 1].shape[0]
        total_count = self.data.shape[0]
        survival_rate = (survived_count / total_count) * 100
        return f"The survival rate is {survival_rate:.2f}%."

    def get_average_age(self):
        average_age = self.data['Age'].mean()
        return f"The average age of passengers is {average_age:.2f} years."

    def get_class_distribution(self):
        class_distribution = self.data['Pclass'].value_counts().to_dict()
        return f"Class distribution: {class_distribution}."
        
    def get_gender_percentage(self):
        male_count = self.data[self.data['Sex'] == 'male'].shape[0]
        total_count = self.data.shape[0]
        male_percent = (male_count / total_count) * 100
        return f"{male_percent:.2f}% of passengers were male."
        
    def get_average_fare(self):
        average_fare = self.data['Fare'].mean()
        return f"The average ticket fare was £{average_fare:.2f}."
        
    def get_embarkation_counts(self):
        embark_counts = self.data['Embarked'].value_counts().to_dict()
        # Map port letters to names
        ports = {'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'}
        mapped_counts = {ports.get(k, k): v for k, v in embark_counts.items()}
        return f"Passengers embarked from the following ports: {mapped_counts}."