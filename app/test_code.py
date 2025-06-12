class Report:
    def __init__(self, data):
        self.data = data

    def calculate_salary(self):
        total = 0
        for d in self.data:
            if d["role"] == "manager":
                total += d["hours"] * 50
            else:
                total += d["hours"] * 30
        return total

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self.data))

    def send_email(self, email):
        print(f"Sending {self.data} to {email}")

    def print_html(self):
        html = "<html><body><ul>"
        for d in self.data:
            html += f"<li>{d['name']} - {d['hours']}</li>"
        html += "</ul></body></html>"
        print(html)

data = [
    {"name": "Alice", "hours": 40, "role": "dev"},
    {"name": "Bob", "hours": 50, "role": "manager"}
]

report = Report(data)
print(report.calculate_salary())
report.save_to_file("out.txt")
report.send_email("admin@example.com")
report.print_html()
